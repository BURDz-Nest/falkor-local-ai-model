#!/usr/bin/env python
"""Diagnostic script to show what Falkor SHOULD display."""

from rich.console import Console
from rich.panel import Panel
import os

console = Console()

print("\n" + "="*70)
print("FALKOR DIAGNOSTIC - What You Should See")
print("="*70 + "\n")

# Show what the enhanced prompt looks like
console.print("[bold yellow]1. Enhanced Prompt (NEW):[/bold yellow]\n")

current_dir = os.getcwd()
home = os.path.expanduser("~")
if current_dir.startswith(home):
    display_dir = "~" + current_dir[len(home):]
else:
    display_dir = current_dir

if len(display_dir) > 40:
    display_dir = "..." + display_dir[-37:]

sample_prompt = f"[bold magenta][llama3.1:8b][/bold magenta] [dim]({display_dir})[/dim]\n[bold cyan]You:[/bold cyan] "
console.print(sample_prompt)

print("\n" + "-"*70 + "\n")

console.print("[bold yellow]2. Old Prompt (BEFORE):[/bold yellow]\n")
console.print("[bold cyan]You:[/bold cyan] ")

print("\n" + "="*70)
print("\nCOMPARISON:")
print("  OLD: Just 'You:'")
print("  NEW: Shows [model] (directory) before 'You:'")
print("\n" + "="*70)

print("\n[bold green]✅ If you see the NEW prompt when running Falkor,[/bold green]")
print("[bold green]   you have the updated code![/bold green]\n")

print("\n" + "="*70)
print("\nTO TEST:")
print("  1. Run: python main.py")
print("  2. Check if prompt shows [model] (directory)")
print("  3. Type: /model")
print("  4. Press Enter")
print("  5. You should see an interactive dropdown menu!")
print("\n" + "="*70 + "\n")
