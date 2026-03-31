"""Test interactive menus (requires manual interaction)."""

from falkor.cli.interactive import InteractiveMenu

print("\n" + "="*60)
print("Testing Code Puppy-Style Interactive Model Selector")
print("="*60)
print("\nThis will show you the beautiful model selector.")
print("Just like in Code Puppy!\n")
print("Expected UI:")
print("  =============== Model Selection ===============")
print("  ")
print("    Select a model to use")
print("    Current model: llama3.1:8b")
print("  ")
print("  ================================================")
print("  ")
print("  Which model would you like to use?")
print("  ")
print("    ✓ qwen2.5-coder:32b      <- Selected (green checkmark)")
print("      llama3.1:8b (current)")
print("      qwen2.5:7b")
print("      qwen2.5:1.5b")
print("  ")
print("  (Use ↑↓ arrows, Enter to confirm, Esc to cancel)")
print("\n" + "="*60)

input("\nPress Enter to see the actual interactive selector...")

menu = InteractiveMenu()

# Test model selector
models = ["llama3.1:8b", "qwen2.5-coder:32b", "qwen2.5:7b", "qwen2.5:1.5b"]
current = "llama3.1:8b"

print("\n")
selected = menu.select_model(models, current)

if selected:
    print(f"\n✅ You selected: {selected}")
else:
    print("\n❌ Cancelled (pressed Esc)")

print("\n" + "="*60)
print("✅ Interactive model selector test complete!")
print("\nThis menu will be available in Falkor when you type:")
print("  /model")
print("\nThen use arrow keys to select a model!")
print("="*60 + "\n")
