# 🤖 Ollama Models Guide for Falkor

**Complete guide to managing models in Falkor**

---

## 🎯 Quick Start

### Default Model (Already Installed)

If you used the installer, you already have:

```
qwen2.5:1.5b (~700MB)
```

**Fast, lightweight, perfect for getting started!**

---

## 📥 Installing More Models

### Step 1: Pull the Model

Open a new terminal and run:

```bash
# Example: Pull llama3.1:8b
ollama pull llama3.1:8b
```

### Step 2: Restart Falkor

```bash
# Exit Falkor
exit

# Start again
falkor
```

### Step 3: Switch to New Model

In Falkor:

```
1. Type: /model
2. Press: Enter
3. Use: Arrow keys ↑↓ to select
4. Press: Enter to confirm
```

Done! You're now using the new model!

---

## 🌟 Recommended Models

### For Beginners (Fast & Small)

#### qwen2.5:1.5b (700MB) ⭐ DEFAULT
```bash
ollama pull qwen2.5:1.5b
```
- ✅ Super fast responses
- ✅ Small download
- ✅ Good for quick tasks
- ✅ Low RAM usage (~2GB)
- ⚠️ Not as smart as larger models

---

### For General Use (Balanced)

#### llama3.1:8b (4.7GB) ⭐ RECOMMENDED
```bash
ollama pull llama3.1:8b
```
- ✅ Great all-around model
- ✅ Good reasoning
- ✅ Fast enough
- ✅ Moderate RAM (~8GB)
- 👍 Best balance of speed & quality

#### qwen2.5:7b (4.7GB)
```bash
ollama pull qwen2.5:7b
```
- ✅ Excellent for conversations
- ✅ Fast responses
- ✅ Good code understanding
- ✅ Moderate RAM (~8GB)

---

### For Coding (Best Code Quality)

#### qwen2.5-coder:32b (19GB) ⭐ BEST FOR CODE
```bash
ollama pull qwen2.5-coder:32b
```
- ✅ Best code generation
- ✅ Excellent debugging
- ✅ Understands complex code
- ⚠️ Large download (19GB)
- ⚠️ High RAM usage (~20GB)
- ⚠️ Slower responses

#### qwen2.5-coder:7b (4.7GB)
```bash
ollama pull qwen2.5-coder:7b
```
- ✅ Good coding assistant
- ✅ Faster than 32b version
- ✅ Moderate RAM (~8GB)
- 👍 Great middle ground

---

### For Instructions (Following Directions)

#### mistral:7b (4.1GB)
```bash
ollama pull mistral:7b
```
- ✅ Excellent at following instructions
- ✅ Clear, structured responses
- ✅ Good for tasks
- ✅ Moderate RAM (~8GB)

---

## 📊 Model Comparison Table

| Model | Size | RAM | Speed | Quality | Best For |
|-------|------|-----|-------|---------|----------|
| **qwen2.5:1.5b** | 700MB | 2GB | ⚡⚡⚡ | ⭐⭐ | Quick tasks |
| **llama3.1:8b** | 4.7GB | 8GB | ⚡⚡ | ⭐⭐⭐⭐ | General use |
| **qwen2.5:7b** | 4.7GB | 8GB | ⚡⚡ | ⭐⭐⭐⭐ | Conversations |
| **qwen2.5-coder:7b** | 4.7GB | 8GB | ⚡⚡ | ⭐⭐⭐⭐ | Coding |
| **mistral:7b** | 4.1GB | 8GB | ⚡⚡ | ⭐⭐⭐⭐ | Instructions |
| **qwen2.5-coder:32b** | 19GB | 20GB | ⚡ | ⭐⭐⭐⭐⭐ | Pro coding |

---

## 💾 Disk Space Planning

### Minimal Setup (2GB free)
```
qwen2.5:1.5b only
```

### Recommended Setup (15GB free)
```
qwen2.5:1.5b     (700MB)   # Fast tasks
llama3.1:8b      (4.7GB)   # General use
qwen2.5-coder:7b (4.7GB)   # Coding
```

### Power User Setup (30GB+ free)
```
qwen2.5:1.5b        (700MB)   # Quick tests
llama3.1:8b         (4.7GB)   # General
qwen2.5-coder:32b   (19GB)    # Serious coding
mistral:7b          (4.1GB)   # Instructions
```

---

## 🛠️ Model Management Commands

### List Installed Models
```bash
ollama list
```

**Output:**
```
NAME                 SIZE      MODIFIED
qwen2.5:1.5b        935 MB    2 hours ago
llama3.1:8b         4.7 GB    1 day ago
```

---

### Pull (Download) a Model
```bash
ollama pull <model-name>
```

**Examples:**
```bash
ollama pull llama3.1:8b
ollama pull qwen2.5-coder:32b
ollama pull mistral:7b
```

---

### Remove a Model
```bash
ollama rm <model-name>
```

**Example:**
```bash
ollama rm qwen2.5:1.5b
```

⚠️ **Warning**: This permanently deletes the model. You'll need to re-download it.

---

### Check Model Details
```bash
ollama show <model-name>
```

**Example:**
```bash
ollama show llama3.1:8b
```

---

## 🔄 Switching Models in Falkor

### Method 1: Interactive Selector (Recommended)

1. Type: `/model`
2. Press: Enter
3. See beautiful dropdown:

```
=============== Model Selection ===============

  Select a model to use
  Current model: qwen2.5:1.5b

================================================

  ✓ llama3.1:8b
    qwen2.5:1.5b (current)
    qwen2.5-coder:7b

(Use ↑↓ arrows, Enter to confirm, Esc to cancel)
```

4. Arrow keys to select
5. Enter to confirm

---

### Method 2: Restart Falkor

```bash
exit
falkor
```

Falkor will use the same model you last selected.

---

## 🎯 Model Selection Guide

### "Which model should I use?"

**For chatting / questions:**
→ `llama3.1:8b` or `qwen2.5:7b`

**For coding:**
→ `qwen2.5-coder:7b` (fast) or `qwen2.5-coder:32b` (best)

**For quick tasks:**
→ `qwen2.5:1.5b`

**For following instructions:**
→ `mistral:7b`

**If you have limited RAM (<8GB):**
→ `qwen2.5:1.5b` only

**If you have lots of RAM (32GB+):**
→ All of them! Switch as needed

---

## 📁 Where Are Models Stored?

### macOS / Linux
```
~/.ollama/models/
```

### Windows
```
C:\Users\<username>\.ollama\models\
```

**Size on disk:**
- Each model takes its listed size
- No compression
- Safe to delete via `ollama rm`

---

## ⚡ Performance Tips

### Model is Slow?

1. **Use smaller model**
   ```bash
   ollama pull qwen2.5:1.5b
   ```

2. **Close other apps**
   - Free up RAM
   - Close browser tabs
   - Quit heavy apps

3. **Check system resources**
   - macOS: Activity Monitor
   - Linux: `htop`
   - Windows: Task Manager

---

### Model Uses Too Much RAM?

**RAM Usage by Model:**
- 1.5b models: ~2GB RAM
- 7-8b models: ~8GB RAM
- 32b models: ~20GB RAM

**Solutions:**
1. Use smaller model
2. Upgrade RAM
3. Don't run multiple models at once

---

## 🔍 Finding More Models

### Official Ollama Library

https://ollama.com/library

**Browse categories:**
- Code (Codellama, Starcoder)
- Chat (Llama, Mistral, Gemma)
- Specialized (Medical, Legal)

### Pull Any Model

```bash
# Format: ollama pull <model>:<size>
ollama pull codellama:13b
ollama pull gemma:7b
ollama pull phi:2.7b
```

---

## ❓ Troubleshooting

### "Model not found in Falkor"

**Fix:**
```bash
# 1. Pull the model
ollama pull llama3.1:8b

# 2. Restart Falkor
exit
falkor

# 3. Type /model to see it
```

---

### "Download is very slow"

**Causes:**
- Slow internet connection
- Large model (32b = 19GB)
- Ollama server load

**Solutions:**
- Be patient (large models take time)
- Try a smaller model first
- Download overnight

---

### "Out of disk space"

**Check space:**
```bash
# macOS/Linux
df -h ~

# Windows
dir
```

**Free up space:**
```bash
# Remove unused models
ollama list
ollama rm <unused-model>
```

---

### "Model stopped responding"

**Fix:**
1. Press Ctrl+C in Falkor
2. Try again
3. If still stuck, restart Falkor:
   ```bash
   exit
   falkor
   ```

---

## 📚 Learn More

- **Ollama Docs**: https://ollama.com/
- **Model Library**: https://ollama.com/library
- **Falkor Help**: Type `/help` in Falkor

---

## 🎯 Quick Reference

```bash
# List models
ollama list

# Pull model
ollama pull llama3.1:8b

# Remove model
ollama rm llama3.1:8b

# Switch in Falkor
/model
```

**That's all you need!** 🐉

---

**Pro tip**: Start with `llama3.1:8b` - it's the best all-around model!
