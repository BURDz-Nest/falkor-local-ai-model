"""Test responsive banner rendering."""

from falkor.cli.renderer import FalkorRenderer
from falkor import __version__
from rich.console import Console

print("\n" + "="*80)
print("TESTING RESPONSIVE BANNER RENDERING")
print("="*80)

print("\n1️⃣  WIDE TERMINAL (100+ columns) - Full ASCII Art:")
print("-" * 80)
renderer_wide = FalkorRenderer()
renderer_wide.console = Console(width=120)  # Simulate wide terminal
banner_wide = renderer_wide._render_full_banner(__version__)
renderer_wide.console.print(banner_wide)

print("\n" + "="*80)
print("\n2️⃣  MEDIUM TERMINAL (60-99 columns) - Compact:")
print("-" * 60)
renderer_medium = FalkorRenderer()
renderer_medium.console = Console(width=70)  # Simulate medium terminal
banner_medium = renderer_medium._render_compact_banner(__version__)
renderer_medium.console.print(banner_medium)

print("\n" + "="*80)
print("\n3️⃣  NARROW TERMINAL (<60 columns) - Simple Text:")
print("-" * 40)
renderer_narrow = FalkorRenderer()
renderer_narrow.console = Console(width=40)  # Simulate narrow terminal
banner_narrow = renderer_narrow._render_simple_banner(__version__)
renderer_narrow.console.print(banner_narrow)

print("\n" + "="*80)
print("\n✅ All three banner styles rendered!")
print("\n📏 Current terminal width:", Console().width, "columns")
print("\nResize your terminal and run 'python main.py' to see the adaptive banner!\n")
