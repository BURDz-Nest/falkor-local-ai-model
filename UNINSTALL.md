# 🗑️ Uninstalling Falkor

**Complete guide to removing Falkor from your system**

---

## ⚡ Quick Uninstall

### macOS / Linux

```bash
~/.falkor/uninstall.sh
```

### Windows

```powershell
~/.falkor/uninstall.ps1
```

**That's it!** Falkor will be completely removed.

---

## 📝 What Gets Removed

### Automatically Removed

- ✅ `~/.falkor/` directory (all Falkor files)
- ✅ `~/bin/falkor` command (macOS/Linux)
- ✅ `falkor.bat` command (Windows)
- ✅ PATH modifications

### What Stays (Not Removed)

- ⏸️ **Ollama** - Separate application
- ⏸️ **Downloaded models** - Can be reused
- ⏸️ **Python** - System installation
- ⏸️ **Python packages** - User-installed

---

## 💾 Manual Uninstall

### If Uninstall Script is Missing

**macOS / Linux:**

```bash
# Remove Falkor directory
rm -rf ~/.falkor

# Remove command
rm ~/bin/falkor

# Done!
```

**Windows:**

```powershell
# Remove Falkor directory
Remove-Item -Path "$env:USERPROFILE\.falkor" -Recurse -Force

# Remove from PATH (optional)
# Open: Settings > System > About > Advanced system settings > Environment Variables
# Edit User PATH, remove: %USERPROFILE%\.falkor

# Done!
```

---

## 🧹 Complete Cleanup (Including Ollama)

### Remove Ollama

**macOS:**

```bash
# Stop Ollama service
killall ollama

# Remove Ollama
rm -rf /usr/local/bin/ollama
rm -rf ~/.ollama
```

**Linux:**

```bash
# Stop Ollama service
sudo systemctl stop ollama

# Remove Ollama
sudo rm /usr/local/bin/ollama
rm -rf ~/.ollama
```

**Windows:**

1. Open "Add or Remove Programs"
2. Search for "Ollama"
3. Click "Uninstall"
4. Follow prompts

---

### Remove Models Only

**Keep Ollama, remove all models:**

```bash
# List models
ollama list

# Remove each model
ollama rm qwen2.5:1.5b
ollama rm llama3.1:8b
ollama rm qwen2.5-coder:32b
# etc.
```

**Or remove all at once:**

```bash
# macOS/Linux
rm -rf ~/.ollama/models

# Windows
Remove-Item -Path "$env:USERPROFILE\.ollama\models" -Recurse -Force
```

---

## 📊 Disk Space Recovery

### How Much Space You'll Free

**Falkor only:**
- Code: ~1MB
- Python packages: ~50MB
- **Total: ~50MB**

**Ollama + Falkor:**
- Ollama: ~500MB
- Falkor: ~50MB
- **Total: ~550MB**

**Everything (Ollama + Models + Falkor):**
- Depends on models installed
- Small model (1.5b): ~700MB
- Medium models (7-8b): ~4.7GB each
- Large models (32b): ~19GB
- **Total: Varies (1GB - 30GB+)**

---

## ⚙️ Reinstalling Later

### To Reinstall Falkor

**Easy - Just run installer again:**

```bash
# macOS/Linux
curl -fsSL https://raw.githubusercontent.com/BURDz-Nest/falkor-local-ai-model/main/install.sh | bash

# Windows
irm https://raw.githubusercontent.com/BURDz-Nest/falkor-local-ai-model/main/install.ps1 | iex
```

**Your models will still be there!** (if you didn't remove Ollama)

---

## ⚠️ Before Uninstalling

### Save Your Work

Currently, Falkor doesn't save conversation history between sessions.

**Coming in v0.2.0:**
- Session save/load
- Export conversations

For now, nothing to save!

---

## 🔍 Verify Uninstall

### Check if Falkor is Gone

**Try running:**

```bash
falkor
```

**Expected result:**
```
command not found: falkor
```

**Check directory:**

```bash
# Should return "No such file or directory"
ls ~/.falkor
```

✅ If both fail, Falkor is successfully removed!

---

## 🔄 Partial Uninstall (Keep Models)

**Want to remove Falkor but keep models for other tools?**

```bash
# Just run the uninstall script
~/.falkor/uninstall.sh  # or .ps1 on Windows

# Ollama and models stay!
```

You can:
- Use Ollama directly: `ollama run llama3.1:8b`
- Use models with other tools
- Reinstall Falkor later

---

## ❓ Troubleshooting Uninstall

### "Uninstall script not found"

**Fix:** Use manual uninstall (see above)

---

### "Permission denied"

**macOS/Linux:**

```bash
# Make script executable
chmod +x ~/.falkor/uninstall.sh

# Run again
~/.falkor/uninstall.sh
```

**Windows:**

```powershell
# Run PowerShell as Administrator
# Then run:
~/.falkor/uninstall.ps1
```

---

### "Command still exists after uninstall"

**Fix:** Reload shell

```bash
# macOS/Linux
source ~/.zshrc  # or ~/.bashrc

# Windows: Close and reopen terminal
```

---

### "Models taking up too much space"

**Check model sizes:**

```bash
ollama list
```

**Remove unused models:**

```bash
# Remove specific model
ollama rm qwen2.5-coder:32b  # Frees 19GB!

# Check space again
ollama list
```

---

## 📝 Feedback

### Before You Go

**We'd love to know:**
- Why are you uninstalling?
- What could we improve?
- What features were missing?

**Open an issue on GitHub:**
https://github.com/BURDz-Nest/falkor-local-ai-model/issues

Your feedback helps make Falkor better! 🐉

---

## 🔗 Related Docs

- **[Installation](INSTALLATION.md)** - How to install Falkor
- **[README](README.md)** - Main documentation
- **[Models](MODELS.md)** - Managing models

---

## ✅ Uninstall Checklist

- [ ] Run uninstall script
- [ ] Verify `falkor` command is gone
- [ ] Check `~/.falkor` directory is removed
- [ ] (Optional) Remove Ollama
- [ ] (Optional) Remove models
- [ ] Reload shell / restart terminal

---

**Thanks for trying Falkor!** 🐉

*Come back anytime - installation is just one command away!*
