"""Interactive menus for Falkor using prompt_toolkit."""

from typing import List, Optional
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import radiolist_dialog, button_dialog
from rich.console import Console
from rich.table import Table


class InteractiveMenu:
    """Interactive menu system for Falkor."""

    def __init__(self):
        self.console = Console()

    def select_model(self, models: List[str], current_model: str) -> Optional[str]:
        """Show interactive model selector with arrow keys.
        
        Args:
            models: List of available model names
            current_model: Currently active model
            
        Returns:
            Selected model name or None if cancelled
        """
        # Create values list for radiolist (value, label) tuples
        values = []
        for model in models:
            if model == current_model:
                label = f"{model} (current)"
            else:
                label = model
            values.append((model, label))
        
        result = radiolist_dialog(
            title="Select Model",
            text="Use arrow keys to navigate, Enter to select, Esc to cancel:",
            values=values,
            default=current_model
        ).run()
        
        return result

    def confirm(self, message: str, title: str = "Confirm") -> bool:
        """Show yes/no confirmation dialog.
        
        Args:
            message: Confirmation message
            title: Dialog title
            
        Returns:
            True if confirmed, False otherwise
        """
        result = button_dialog(
            title=title,
            text=message,
            buttons=[
                ('Yes', True),
                ('No', False),
            ],
        ).run()
        
        return result if result is not None else False

    def show_command_menu(self) -> Optional[str]:
        """Show interactive command menu.
        
        Returns:
            Selected command or None if cancelled
        """
        commands = [
            ('/help', 'Show help menu'),
            ('/model', 'Switch models'),
            ('/clear', 'Clear screen'),
            ('/history', 'Show conversation history'),
            ('exit', 'Exit Falkor'),
        ]
        
        result = radiolist_dialog(
            title="Commands",
            text="Select a command:",
            values=commands
        ).run()
        
        return result
