"""Main CLI application for Falkor."""

import os
from falkor.models.ollama_client import OllamaClient, OllamaConnectionError
from falkor.cli.renderer import FalkorRenderer
from falkor.cli.interactive import InteractiveMenu
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
        self.menu = InteractiveMenu()
        self.conversation_history = []
        self.current_dir = os.getcwd()

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
                # Show enhanced prompt with model + directory
                self._show_prompt()
                # Get user input (console.input doesn't support Rich markup, so we use plain input)
                user_input = input().strip()
                
                if not user_input:
                    continue
                
                # Check for commands
                if user_input.lower() == "/help":
                    self.renderer.render_help()
                    continue
                
                if user_input.lower() == "/clear":
                    self.renderer.clear_screen()
                    continue
                
                if user_input.lower() == "/history":
                    self._show_history()
                    continue
                
                if user_input.lower() == "/model":
                    # Interactive model selector dropdown!
                    selected = self.menu.select_model(models, self.model)
                    if selected and selected != self.model:
                        self._switch_model(selected, models)
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

    def _show_prompt(self):
        """Display enhanced prompt with model and directory."""
        # Update current directory (in case it changed)
        self.current_dir = os.getcwd()
        
        # Shorten directory path for display
        home = os.path.expanduser("~")
        if self.current_dir.startswith(home):
            display_dir = "~" + self.current_dir[len(home):]
        else:
            display_dir = self.current_dir
        
        # Limit directory length
        if len(display_dir) > 40:
            display_dir = "..." + display_dir[-37:]
        
        # Print formatted prompt: [model] (directory)
        from rich.text import Text
        
        self.renderer.console.print()
        
        # Build prompt using Text object for proper escaping
        prompt_line = Text()
        prompt_line.append("[", style="bold magenta")
        prompt_line.append(self.model, style="bold magenta")
        prompt_line.append("] ", style="bold magenta")
        prompt_line.append(f"({display_dir})", style="dim")
        
        self.renderer.console.print(prompt_line)
        self.renderer.console.print("[bold cyan]You:[/bold cyan] ", end="")

    def _switch_model(self, new_model: str, models: list):
        """Switch to a different model.
        
        Args:
            new_model: Model name to switch to
            models: List of available models (not used, kept for compatibility)
        """
        old_model = self.model
        self.model = new_model
        self.renderer.render_success(
            f"Switched from {old_model} to {new_model}",
            title="Model Changed"
        )

    def _show_history(self):
        """Show conversation history."""
        if not self.conversation_history:
            self.renderer.print("\n[yellow]No conversation history yet.[/yellow]\n")
            return
        
        from rich.panel import Panel
        from rich.text import Text
        
        self.renderer.print("\n[bold cyan]Conversation History:[/bold cyan]\n")
        
        for i, msg in enumerate(self.conversation_history, 1):
            role = msg["role"]
            content = msg["content"]
            
            if role == "user":
                style = "cyan"
                prefix = "You"
            else:
                style = "green"
                prefix = "Falkor"
            
            # Truncate long messages
            if len(content) > 100:
                content = content[:97] + "..."
            
            self.renderer.console.print(
                f"[bold {style}]{i}. {prefix}:[/bold {style}] {content}"
            )
        
        self.renderer.print(f"\n[dim]Total messages: {len(self.conversation_history)}[/dim]\n")


def main():
    """Entry point for CLI."""
    app = FalkorApp()
    app.run()


if __name__ == "__main__":
    main()
