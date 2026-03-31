# 🎯 How to Test the New Interactive /model Command

## Step-by-Step Test Instructions:

### 1. Start Falkor
```bash
cd ~/Desktop/Dump/Pupclone/dev/falkor
python main.py
```

### 2. What You Should See:

**OLD Prompt (before):**
```
You: _
```

**NEW Prompt (now):**
```
[llama3.1:8b] (~/Desktop/Dump/Pupclone/dev/falkor)
You: _
```

✅ **If you see the NEW prompt** = You're running the updated code!
❌ **If you see the OLD prompt** = You might be in the wrong directory

---

### 3. Test Interactive Model Selector:

Type exactly this:
```
/model
```

Then press **Enter**

**OLD Behavior (before):**
- Would show a table of models
- You'd have to type `/model llama3.1:8b` manually

**NEW Behavior (now):**
- Shows an interactive dialog box
- Looks like this:

```
┌─ Select Model ────────────────────────────────────┐
│                                                   │
│  Use arrow keys to navigate, Enter to select...  │
│                                                   │
│  ( ) llama3.1:8b (current)                       │
│  ( ) qwen2.5-coder:32b                           │
│  ( ) qwen2.5:7b                                  │
│  ( ) qwen2.5:1.5b                                │
│                                                   │
│  [Select] [Cancel]                                │
└───────────────────────────────────────────────────┘
```

- Use **↑↓ arrow keys** to move
- Press **Enter** to select
- Press **Esc** to cancel

---

### 4. Verify It Works:

After selecting a model with arrow keys + Enter, you should see:

```
╭─ Model Changed ──────────────────────╮
│ ✅ Switched from llama3.1:8b to      │
│    qwen2.5-coder:32b                 │
╰──────────────────────────────────────╯
```

And your next prompt should show the new model:
```
[qwen2.5-coder:32b] (~/Desktop/Dump/Pupclone/dev/falkor)
You: _
```

---

## Troubleshooting:

### Problem: I still see the old prompt format
**Solution:**
```bash
# Make sure you're in the right directory
cd ~/Desktop/Dump/Pupclone/dev/falkor
pwd  # Should show: .../Pupclone/dev/falkor

# Clear Python cache
find . -name "*.pyc" -delete
find . -name __pycache__ -type d -rm -rf

# Run again
python main.py
```

### Problem: /model doesn't show a dropdown
**Solution:**
- Make sure you have `prompt_toolkit` installed:
```bash
pip install prompt_toolkit
```

### Problem: Terminal looks weird/broken
**Solution:**
- Your terminal might not support interactive dialogs
- Try a different terminal (iTerm2, standard Terminal.app, etc.)

---

## Quick Visual Check:

**Run this to see the current code version:**
```bash
cd ~/Desktop/Dump/Pupclone/dev/falkor
grep -A 3 "if user_input.lower() == \"/model\"" falkor/cli/app.py
```

**You should see:**
```python
if user_input.lower() == "/model":
    # Interactive model selector dropdown!
    selected = self.menu.select_model(models, self.model)
    if selected and selected != self.model:
```

✅ If you see "Interactive model selector dropdown!" = You have the new code  
❌ If you see something else = Wrong version

---

## What EXACTLY Changed:

| Feature | Before | After |
|---------|--------|-------|
| **Prompt** | `You: _` | `[llama3.1:8b] (~/path)\nYou: _` |
| **Model Switch** | Type `/model llama3.1:8b` | Type `/model` → Arrow keys → Enter |
| **Model List** | Table display | Interactive dropdown |
| **Directory** | Not shown | Shows in prompt |

---

**Try it now and tell me:**
1. What does your prompt look like?
2. When you type `/model` and press Enter, what do you see?
3. Can you use arrow keys to navigate?
