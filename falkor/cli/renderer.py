"""Rich console renderer for Falkor - Beautiful terminal UI."""

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text
from rich.syntax import Syntax
from rich.live import Live
from rich.spinner import Spinner
from rich.table import Table
from typing import Optional


class FalkorRenderer:
    """Beautiful CLI rendering with Rich."""

    def __init__(self):
        """Initialize the renderer."""
        self.console = Console()

    def render_banner(self, version: str, model: str, models_count: int):
        """Render the big beautiful Falkor banner.
        
        Args:
            version: Falkor version
            model: Active model name
            models_count: Number of available models
        """
        # Get terminal width
        terminal_width = self.console.width
        
        # Choose banner style based on terminal width
        if terminal_width >= 100:
            # Full ASCII art banner (wide terminals)
            banner = self._render_full_banner(version)
        elif terminal_width >= 60:
            # Compact banner (medium terminals)
            banner = self._render_compact_banner(version)
        else:
            # Simple text banner (narrow terminals)
            banner = self._render_simple_banner(version)
        
        # Create info panel (basic ASCII only)
        info = Text()
        info.append(">> Model: ", style="bold")
        info.append(f"{model}\n", style="green")
        info.append(">> Available: ", style="bold")
        info.append(f"{models_count} models\n", style="cyan")
        info.append(">> Commands: ", style="bold")
        info.append("Type ", style="dim")
        info.append("/help", style="yellow")
        info.append(" for help or ", style="dim")
        info.append("exit", style="yellow")
        info.append(" to quit", style="dim")
        
        # Print banner
        self.console.print(Panel(
            banner,
            border_style="bright_blue",
            padding=(1, 2)
        ))
        
        # Print info
        self.console.print(Panel(
            info,
            border_style="dim",
            padding=(0, 2)
        ))
        self.console.print()

    def _render_full_banner(self, version: str) -> Text:
        """Render full ASCII art banner (for wide terminals >= 100 cols).
        
        Args:
            version: Falkor version
            
        Returns:
            Formatted Text object
        """
        banner = Text()
        banner.append("\n")
        
        # Pure ASCII art FALKOR (NO Unicode - works everywhere!)
        falkor_art = [
            "  ########    #    ##       ##  ##  ####  ####  ",
            "  ##         # #   ##       ## ##  ##  ## ##  ## ",
            "  #####     #####  ##       ####   ##  ## ####   ",
            "  ##       ##   ## ##       ## ##  ##  ## ## ##  ",
            "  ##       ##   ## ######## ##  ##  ####  ##  ## ",
        ]
        
        # Color gradient: cyan -> blue -> magenta
        colors = ["cyan", "bright_cyan", "blue", "bright_blue", "magenta"]
        
        for i, line in enumerate(falkor_art):
            color = colors[i % len(colors)]
            banner.append(f"{line}\n", style=f"bold {color}")
        
        banner.append("\n")
        banner.append("      >> Your Local Knowledge Assistant <<\n", style="bold yellow")
        banner.append(f"                  v{version}\n\n", style="dim")
        
        return banner

    def _render_compact_banner(self, version: str) -> Text:
        """Render compact banner (for medium terminals >= 60 cols).
        
        Args:
            version: Falkor version
            
        Returns:
            Formatted Text object
        """
        banner = Text()
        banner.append("\n")
        
        # Smaller ASCII art (basic characters only)
        falkor_compact = [
            "  ####    #    ##    ##  ## ",
            "  ##     # #   ##    ## ##  ",
            "  ###   #####  ##    ####   ",
            "  ##   ##   ## ##    ## ##  ",
            "  ##   ##   ## ##### ##  ## ",
        ]
        
        colors = ["cyan", "bright_cyan", "blue", "bright_blue", "magenta"]
        
        for i, line in enumerate(falkor_compact):
            color = colors[i % len(colors)]
            banner.append(f"{line}\n", style=f"bold {color}")
        
        banner.append("\n")
        banner.append("   >> Knowledge Assistant <<\n", style="bold yellow")
        banner.append(f"          v{version}\n\n", style="dim")
        
        return banner

    def _render_simple_banner(self, version: str) -> Text:
        """Render simple text banner (for narrow terminals < 60 cols).
        
        Args:
            version: Falkor version
            
        Returns:
            Formatted Text object
        """
        banner = Text()
        banner.append("\n")
        banner.append("  ========================\n", style="cyan")
        banner.append("  ", style="cyan")
        banner.append("   F A L K O R", style="bold bright_blue")
        banner.append("   \n", style="cyan")
        banner.append("  ========================\n", style="cyan")
        banner.append("\n")
        banner.append("   Knowledge Assistant\n", style="yellow")
        banner.append(f"   v{version}\n", style="dim")
        banner.append("\n")
        
        return banner

    def render_markdown(self, content: str, style: str = "green"):
        """Render markdown content.
        
        Args:
            content: Markdown text
            style: Color style for text
        """
        md = Markdown(content, code_theme="monokai")
        self.console.print(md)

    def render_code(self, code: str, language: str = "python"):
        """Render syntax-highlighted code.
        
        Args:
            code: Code to render
            language: Programming language
        """
        syntax = Syntax(code, language, theme="monokai", line_numbers=True)
        self.console.print(syntax)

    def render_user_prompt(self) -> str:
        """Render user input prompt.
        
        Returns:
            Formatted prompt string
        """
        return "\n[bold cyan]You:[/bold cyan] "

    def render_assistant_prefix(self):
        """Render assistant response prefix."""
        self.console.print("[bold green]🐉 Falkor:[/bold green] ", end="")

    def render_thinking(self, message: str = "Thinking..."):
        """Show thinking spinner.
        
        Args:
            message: Status message
            
        Returns:
            Live context manager for updating
        """
        spinner = Spinner("dots", text=f"[yellow]{message}[/yellow]")
        return Live(spinner, console=self.console, transient=True)

    def render_error(self, error: str, title: str = "Error"):
        """Render error message.
        
        Args:
            error: Error message
            title: Error title
        """
        self.console.print(Panel(
            f"[red]{error}[/red]",
            title=f"[red]❌ {title}[/red]",
            border_style="red",
            padding=(1, 2)
        ))

    def render_success(self, message: str, title: str = "Success"):
        """Render success message.
        
        Args:
            message: Success message
            title: Success title
        """
        self.console.print(Panel(
            f"[green]{message}[/green]",
            title=f"[green]✅ {title}[/green]",
            border_style="green",
            padding=(1, 2)
        ))

    def render_help(self):
        """Render help menu."""
        table = Table(title="🐉 Falkor Commands", border_style="cyan")
        table.add_column("Command", style="yellow", no_wrap=True)
        table.add_column("Description", style="white")
        
        table.add_row("/help", "Show this help menu")
        table.add_row("/model", "List available models")
        table.add_row("/model <name>", "Switch to a different model")
        table.add_row("/clear", "Clear the screen")
        table.add_row("/history", "Show conversation history")
        table.add_row("exit, quit, bye", "Exit Falkor")
        
        self.console.print()
        self.console.print(table)
        self.console.print()

    def clear_screen(self):
        """Clear the terminal screen."""
        self.console.clear()

    def print(self, *args, **kwargs):
        """Wrapper for console.print."""
        self.console.print(*args, **kwargs)
