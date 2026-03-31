"""Debug: Show exactly what _show_prompt produces."""

from falkor.cli.app import FalkorApp
from rich.console import Console

console = Console()
app = FalkorApp()

print("\n" + "="*60)
print("DEBUG: Testing _show_prompt method")
print("="*60 + "\n")

print("App model:", app.model)
print("App current_dir:", app.current_dir)
print("\nCalling _show_prompt():\n")

app._show_prompt()
print("\n\n" + "="*60)
print("\nIf you see [llama3.1:8b] in magenta above, it works!")
print("If you only see the directory, there's still a bug.")
print("="*60 + "\n")
