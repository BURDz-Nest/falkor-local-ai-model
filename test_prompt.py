"""Test the enhanced prompt display."""

import os
from falkor.cli.app import FalkorApp

# Create app
app = FalkorApp()

# Test prompt generation
print("Testing enhanced prompt...\n")
print("Example prompts:")
print("="*60)

# Test in different directories
original_dir = os.getcwd()

# Current directory
app.current_dir = os.getcwd()
app.model = "llama3.1:8b"
print("\n1. Current directory:")
app.renderer.console.print(app._get_prompt())

# Home directory
app.current_dir = os.path.expanduser("~")
print("\n2. Home directory:")
app.renderer.console.print(app._get_prompt())

# Long path
app.current_dir = "/Users/f0s00xq/Desktop/Dump/Pupclone/dev/falkor/very/long/nested/path/example"
print("\n3. Long path (should truncate):")
app.renderer.console.print(app._get_prompt())

# Different model
app.model = "qwen2.5-coder:32b"
app.current_dir = original_dir
print("\n4. Different model:")
app.renderer.console.print(app._get_prompt())

print("\n" + "="*60)
print("\n✅ Prompt test complete!")
print("\nThe prompt now shows:")
print("  [model] (directory)")
print("  You: _")
print("\nRun 'python main.py' to see it in action!\n")
