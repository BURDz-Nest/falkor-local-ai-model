"""Interactive menus for Falkor using prompt_toolkit."""

import html
import sys
from typing import List, Optional

from prompt_toolkit import Application
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout, Window
from prompt_toolkit.layout.controls import FormattedTextControl
from rich.console import Console


class InteractiveMenu:
    """Interactive menu system for Falkor (Code Puppy style!)."""

    def __init__(self):
        self.console = Console()

    def select_model(self, models: List[str], current_model: str) -> Optional[str]:
        """Show beautiful Code Puppy-style model selector with arrow keys.
        
        Args:
            models: List of available model names
            current_model: Currently active model
            
        Returns:
            Selected model name or None if cancelled
        """
        # Prepare choices with (current) markers
        choices = []
        current_index = 0
        for i, model in enumerate(models):
            if model == current_model:
                choices.append(f"{model} (current)")
                current_index = i
            else:
                choices.append(model)
        
        selected_index = [current_index]  # Mutable container
        result = [None]  # Mutable container for result

        def get_formatted_text():
            """Generate the formatted text for Code Puppy-style display."""
            lines = [
                "<b>=============== Model Selection ===============</b>",
                "",
                "<ansicyan><b>  Select a model to use</b></ansicyan>",
                f"<dim>  Current model: {html.escape(current_model)}</dim>",
                "",
                "<b>================================================</b>",
                "",
                "<b>Which model would you like to use?</b>",
                ""
            ]
            
            # Add choices with checkmark for selected (like Code Puppy!)
            for i, choice in enumerate(choices):
                safe_choice = html.escape(choice)
                if i == selected_index[0]:
                    # Green checkmark with green text
                    lines.append(f"<ansigreen>  ✓ {safe_choice}</ansigreen>")
                else:
                    # Plain text with space indent
                    lines.append(f"    {safe_choice}")
            
            lines.append("")
            lines.append(
                "<ansicyan>(Use ↑↓ arrows to select, Enter to confirm, Esc to cancel)</ansicyan>"
            )
            return HTML("\n".join(lines))

        # Key bindings
        kb = KeyBindings()

        @kb.add("up")
        @kb.add("c-p")  # Ctrl+P for Emacs users
        def move_up(event):
            selected_index[0] = (selected_index[0] - 1) % len(choices)
            event.app.invalidate()

        @kb.add("down")
        @kb.add("c-n")  # Ctrl+N for Emacs users
        def move_down(event):
            selected_index[0] = (selected_index[0] + 1) % len(choices)
            event.app.invalidate()

        @kb.add("enter")
        def accept(event):
            result[0] = models[selected_index[0]]  # Return actual model name
            event.app.exit()

        @kb.add("escape")
        @kb.add("c-c")  # Ctrl-C also cancels
        def cancel(event):
            result[0] = None
            event.app.exit()

        # Layout
        control = FormattedTextControl(get_formatted_text)
        layout = Layout(Window(content=control))

        # Application
        app = Application(
            layout=layout,
            key_bindings=kb,
            full_screen=False,
        )

        # Flush output before prompt_toolkit takes control
        sys.stdout.flush()
        sys.stderr.flush()

        # Run the app
        try:
            app.run()
        except KeyboardInterrupt:
            return None

        return result[0]
