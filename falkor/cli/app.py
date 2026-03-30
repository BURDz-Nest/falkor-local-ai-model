"""Main CLI application for Falkor."""

from falkor.models.ollama_client import OllamaClient, OllamaConnectionError
from falkor.cli.renderer import FalkorRenderer
from falkor import __version__


class FalkorApp:
    """Main Falkor CLI application."""

    def __init__(self, model: str = "llama3.1:8b", max_history: int = 20):
        """Initialize Falkor app.
        
        Args:
            model: Default model to use
            max_history: Maximum messages to keep in history (default: 20)
        """
        self.model = model
        self.max_history = max_history
        self.client = OllamaClient()
        self.renderer = FalkorRenderer()
        self.conversation_history = []

    def run(self):
        """Run the main CLI loop."""
        # Check Ollama connection first
        try:
            models = self.client.list_models()
        except OllamaConnectionError as e:
            self.renderer.render_error(
                str(e) + "\n\nPlease start Ollama and try again.",
                title="Connection Error"
            )
            return
        
        # Show beautiful banner
        self.renderer.render_banner(
            version=__version__,
            model=self.model,
            models_count=len(models)
        )
        
        # Main chat loop
        while True:
            try:
                # Get user input with styled prompt
                user_input = self.renderer.console.input(self.renderer.render_user_prompt()).strip()
                
                if not user_input:
                    continue
                
                # Check for commands
                if user_input.lower() == "/help":
                    self.renderer.render_help()
                    continue
                
                if user_input.lower() == "/clear":
                    self.renderer.clear_screen()
                    continue
                
                if user_input.lower() == "/model":
                    self._show_models(models)
                    continue
                
                if user_input.lower().startswith("/model "):
                    new_model = user_input[7:].strip()
                    self._switch_model(new_model, models)
                    continue
                
                # Check for exit command
                if user_input.lower() in ["exit", "quit", "bye"]:
                    self.renderer.print("\n[yellow]👋 Goodbye! Thanks for chatting with Falkor![/yellow]\n")
                    break
                
                # Add to conversation history
                self.conversation_history.append({
                    "role": "user",
                    "content": user_input
                })
                
                # Get response from Ollama with thinking indicator
                self.renderer.render_assistant_prefix()
                
                response = self.client.chat(
                    model=self.model,
                    messages=self.conversation_history
                )
                
                assistant_message = response["message"]["content"]
                
                # Render as markdown
                self.renderer.render_markdown(assistant_message)
                
                # Add response to history
                self.conversation_history.append({
                    "role": "assistant",
                    "content": assistant_message
                })
                
                # Trim history if too long (keep last max_history messages)
                if len(self.conversation_history) > self.max_history:
                    self.conversation_history = self.conversation_history[-self.max_history:]
                
            except KeyboardInterrupt:
                self.renderer.print("\n\n[yellow]👋 Goodbye! (Interrupted)[/yellow]")
                break
            except Exception as e:
                self.renderer.render_error(str(e))
                continue
        
        # Cleanup
        self.client.close()

    def _show_models(self, models: list):
        """Show available models.
        
        Args:
            models: List of model names
        """
        from rich.table import Table
        
        table = Table(title="📚 Available Models", border_style="cyan")
        table.add_column("Model", style="yellow")
        table.add_column("Status", style="white")
        
        for model in models:
            status = "✅ Active" if model == self.model else ""
            table.add_row(model, status)
        
        self.renderer.print()
        self.renderer.print(table)
        self.renderer.print()
        self.renderer.print(f"[dim]Switch models with:[/dim] [yellow]/model <name>[/yellow]")
        self.renderer.print()

    def _switch_model(self, new_model: str, models: list):
        """Switch to a different model.
        
        Args:
            new_model: Model name to switch to
            models: List of available models
        """
        if new_model not in models:
            self.renderer.render_error(
                f"Model '{new_model}' not found.\n\nAvailable models: {', '.join(models)}",
                title="Model Not Found"
            )
            return
        
        old_model = self.model
        self.model = new_model
        self.renderer.render_success(
            f"Switched from {old_model} to {new_model}",
            title="Model Changed"
        )


def main():
    """Entry point for CLI."""
    app = FalkorApp()
    app.run()


if __name__ == "__main__":
    main()
