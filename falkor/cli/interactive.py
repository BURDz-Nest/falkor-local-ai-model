"""Interactive menus for Falkor using prompt_toolkit."""

from typing import List, Optional
from prompt_toolkit.shortcuts import radiolist_dialog
from rich.console import Console


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
