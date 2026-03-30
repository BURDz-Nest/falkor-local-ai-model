"""Test interactive menus (requires manual interaction)."""

from falkor.cli.interactive import InteractiveMenu

print("\n" + "="*60)
print("Testing Interactive Menus")
print("="*60)
print("\nThis will show you the interactive model selector.")
print("Use ARROW KEYS to navigate, ENTER to select, ESC to cancel.\n")

input("Press Enter to start the test...")

menu = InteractiveMenu()

# Test model selector
models = ["llama3.1:8b", "qwen2.5-coder:32b", "qwen2.5:7b", "qwen2.5:1.5b"]
current = "llama3.1:8b"

print("\n\nTest 1: Model Selector")
print("-" * 60)
selected = menu.select_model(models, current)

if selected:
    print(f"\n✅ You selected: {selected}")
else:
    print("\n❌ Cancelled")

print("\n\nTest 2: Command Menu")
print("-" * 60)
command = menu.show_command_menu()

if command:
    print(f"\n✅ You selected: {command}")
else:
    print("\n❌ Cancelled")

print("\n\nTest 3: Confirmation Dialog")
print("-" * 60)
confirmed = menu.confirm("Do you want to proceed?")

if confirmed:
    print("\n✅ You clicked Yes")
else:
    print("\n❌ You clicked No")

print("\n" + "="*60)
print("✅ Interactive menu tests complete!")
print("\nThese menus will be available in Falkor with:")
print("  /model  - Interactive model selector")
print("  /menu   - Interactive command menu")
print("="*60 + "\n")
