#!/usr/bin/env python
"""Quick test to verify the interactive /model command works."""

from falkor.cli.interactive import InteractiveMenu

print("\n" + "="*60)
print("Testing Interactive Model Selector")
print("="*60)
print("\nWhen you run Falkor and type '/model', you should see")
print("this interactive dropdown menu:\n")

input("Press Enter to see the interactive dropdown... ")

menu = InteractiveMenu()
models = ["llama3.1:8b", "qwen2.5-coder:32b", "qwen2.5:7b", "qwen2.5:1.5b"]

print("\n[Simulating: You typed '/model' and pressed Enter]\n")

selected = menu.select_model(models, "llama3.1:8b")

if selected:
    print(f"\n✅ You selected: {selected}")
    print("\nIn Falkor, this would instantly switch your model!")
else:
    print("\n❌ You pressed Esc (cancelled)")

print("\n" + "="*60)
print("\nInstructions to run Falkor:")
print("  1. Run: python main.py")
print("  2. Notice the prompt shows: [model] (directory)")
print("  3. Type: /model")
print("  4. Press: Enter")
print("  5. Use: Arrow keys ↑↓")
print("  6. Press: Enter to select")
print("="*60 + "\n")
