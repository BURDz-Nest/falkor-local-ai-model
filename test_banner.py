"""Test the beautiful Falkor banner."""

from falkor.cli.renderer import FalkorRenderer
from falkor import __version__

renderer = FalkorRenderer()
renderer.render_banner(
    version=__version__,
    model="llama3.1:8b",
    models_count=4
)

print("\n✅ Banner test complete!")
print("\nNow run: python main.py")
print("to see the full interactive Falkor! 🐉\n")
