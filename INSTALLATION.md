# 📦 Falkor Installation Guide

**Complete guide for installing Falkor on any platform.**

---

## 🚀 Quick Install (Recommended)

### macOS / Linux

**One command:**

```bash
curl -fsSL https://raw.githubusercontent.com/BURDz-Nest/falkor-local-ai-model/main/install.sh | bash
```

**What it does:**
1. ✅ Checks Python 3.11+
2. ✅ Installs Ollama (if needed)
3. ✅ Downloads Falkor
4. ✅ Installs dependencies
5. ✅ Pulls default model (gemma2:2b ~1.6GB)
6. ✅ Sets up `falkor` command

**Time**: 5-10 minutes

---

### Windows

**PowerShell (Run as User - not Admin):**

```powershell
irm https://raw.githubusercontent.com/BURDz-Nest/falkor-local-ai-model/main/install.ps1 | iex
```

**What it does:**
1. ✅ Checks Python 3.11+
2. ✅ Guides through Ollama installation
3. ✅ Downloads Falkor
4. ✅ Installs dependencies
5. ✅ Pulls default model
6. ✅ Sets up `falkor` command

**Time**: 10-15 minutes (Ollama download)

---

## 📝 Manual Installation

### Prerequisites

#### 1. Python 3.11+

**Check if installed:**
```bash
python3 --version  # or python --version on Windows
```

**Install if needed:**

- **macOS**: `brew install python@3.11`
- **Linux Ubuntu/Debian**: `sudo apt install python3.11`
- **Linux Fedora**: `sudo dnf install python3.11`
- **Windows**: https://www.python.org/downloads/
  - ⚠️ **Important**: Check "Add Python to PATH" during install!

---

#### 2. Ollama

**Check if installed:**
```bash
ollama list
```

**Install if needed:**

- **macOS/Linux**:
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

- **Windows**:
  1. Download from: https://ollama.com/download/windows
  2. Run installer
  3. Restart terminal

---

### Step-by-Step Installation

#### Step 1: Clone Repository

**Private repository - you'll need access!**

```bash
# With GitHub CLI (recommended)
gh repo clone BURDz-Nest/falkor-local-ai-model
cd falkor-local-ai-model

# Or with SSH
git clone git@github.com:BURDz-Nest/falkor-local-ai-model.git
cd falkor-local-ai-model

# Or with HTTPS (will prompt for credentials)
git clone https://github.com/BURDz-Nest/falkor-local-ai-model.git
cd falkor-local-ai-model
```

#### Step 2: Run Installer

**macOS/Linux:**
```bash
bash install.sh
```

**Windows:**
```powershell
.\install.ps1
```

#### Step 3: Follow Prompts

The installer will:
- Check Python
- Check/install Ollama
- Install Falkor to `~/.falkor`
- Install Python packages
- Download default model
- Setup `falkor` command

#### Step 4: Test Installation

```bash
falkor
```

You should see the Falkor banner!

---

## 🔧 Advanced Installation

### Custom Installation Directory

Edit the installer scripts:

**macOS/Linux** (`install.sh`):
```bash
INSTALL_DIR="/path/to/custom/location"
```

**Windows** (`install.ps1`):
```powershell
$INSTALL_DIR = "C:\path\to\custom\location"
```

### Skip Model Download

When prompted:
```
Download default model (gemma2:2b ~1.6GB)? (Y/n)
```

Press `n` to skip. Download later:
```bash
ollama pull qwen2.5:1.5b
```

### Manual Dependencies Install

```bash
cd ~/.falkor
pip install -r requirements.txt
```

---

## 📦 What Gets Installed?

### Files & Directories

```
~/.falkor/                   # Main installation directory
├── falkor/                  # Python package
│   ├── cli/                 # CLI application
│   └── models/              # Ollama client
├── main.py                  # Entry point
├── requirements.txt         # Python dependencies
└── uninstall.sh/.ps1        # Uninstaller

~/bin/falkor                 # Command (macOS/Linux)
~/.falkor/falkor.bat         # Command (Windows)
```

### Python Packages

- `rich>=13.7.0` - Terminal UI
- `httpx>=0.27.0` - HTTP client
- `prompt-toolkit>=3.0.0` - Interactive menus
- `pydantic>=2.0.0` - Data validation
- `PyYAML>=6.0.0` - Config files

### Ollama Models

- `gemma2:2b` (~1.6GB) - Default model (Google, great quality)
- Additional models optional (see README)

---

## ⚙️ Configuration

### Default Settings

- **Installation**: `~/.falkor`
- **Default model**: `gemma2:2b`
- **Max history**: 20 messages
- **Ollama URL**: `http://localhost:11434`

### Customization

Currently settings are hardcoded. Coming in v0.2.0:
- Config file: `~/.falkor/config.yaml`
- Environment variables
- Command-line flags

---

## 🛠️ Troubleshooting Installation

### Python Version Issues

**Error**: `Python 3.11 or higher is required`

**Fix**:
```bash
# Check version
python3 --version

# If too old, install newer Python
# macOS:
brew install python@3.11

# Linux:
sudo apt install python3.11

# Windows:
# Download from python.org
```

---

### Ollama Not Found

**Error**: `Cannot connect to Ollama`

**Fix**:
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Or manually:
# macOS/Linux: https://ollama.com/download
# Windows: https://ollama.com/download/windows
```

---

### Permission Denied

**Error**: `Permission denied`

**macOS/Linux Fix**:
```bash
# Make installer executable
chmod +x install.sh

# Run installer
bash install.sh
```

**Windows Fix**:
```powershell
# Enable script execution (one time)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Run installer
.\install.ps1
```

---

### Command Not Found: falkor

**macOS/Linux**:
```bash
# Reload shell
source ~/.zshrc  # or ~/.bashrc

# Or add ~/bin to PATH in ~/.zshrc:
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**Windows**:
- Close and reopen PowerShell
- PATH update requires new terminal

**Alternative (all platforms)**:
```bash
# Run directly
python ~/.falkor/main.py
```

---

### GitHub Access Denied

**Error**: `Repository not found or access denied`

**Fix**:
1. Make sure you have repository access
2. Use SSH key or GitHub token
3. Contact repository owner for access

**With GitHub CLI**:
```bash
# Login first
gh auth login

# Then clone
gh repo clone BURDz-Nest/falkor-local-ai-model
```

---

### Model Download Fails

**Error**: `Failed to pull model`

**Fix**:
```bash
# Retry manually
ollama pull qwen2.5:1.5b

# Check Ollama is running
ollama list

# If still fails, check internet connection
ping ollama.com
```

---

## 🗑️ Uninstallation

### Complete Removal

**macOS/Linux**:
```bash
~/.falkor/uninstall.sh
```

**Windows**:
```powershell
~/.falkor/uninstall.ps1
```

### What Gets Removed

- ✅ `~/.falkor/` directory
- ✅ `~/bin/falkor` command
- ✅ PATH modifications

### What Stays

- ⏸️ Ollama (separate application)
- ⏸️ Downloaded models
- ⏸️ Python installation
- ⏸️ Python packages (user-installed)

### Remove Ollama & Models

**To remove Ollama**:
- macOS/Linux: See https://ollama.com/
- Windows: Use "Add/Remove Programs"

**To remove models**:
```bash
ollama rm qwen2.5:1.5b
ollama rm llama3.1:8b
# etc.
```

---

## 🔄 Updating Falkor

### Method 1: Reinstall

```bash
# Uninstall
~/.falkor/uninstall.sh

# Pull latest code
cd falkor-local-ai-model
git pull origin main

# Reinstall
bash install.sh
```

### Method 2: Manual Update

```bash
# Pull latest code
cd falkor-local-ai-model
git pull origin main

# Copy updated files
cp -r falkor ~/.falkor/
cp main.py ~/.falkor/

# Update dependencies
cd ~/.falkor
pip install -U -r requirements.txt
```

### Coming Soon: Auto-Update

```bash
falkor --update  # Coming in v0.2.0
```

---

## 📊 Disk Space Requirements

### Minimum

- Falkor code: ~1MB
- Python packages: ~50MB
- Ollama: ~500MB
- Default model (gemma2:2b): ~1.6GB

**Total**: ~1.25GB

### Recommended

- Additional 5GB for more models
- 10GB+ for large models (70b)

---

## ✅ Post-Installation Checklist

- [ ] `python3 --version` shows 3.11+
- [ ] `ollama list` shows installed models
- [ ] `falkor` command works
- [ ] Falkor banner appears
- [ ] Can chat with default model
- [ ] `/model` command shows model list
- [ ] Streaming responses work

---

## 📞 Getting Help

### Installation Issues

1. Check this troubleshooting guide
2. Verify prerequisites (Python, Ollama)
3. Check GitHub Issues
4. Contact repository owner

### Usage Questions

1. Type `/help` in Falkor
2. Read [README.md](README.md)
3. Check [PROJECT_STATUS.md](PROJECT_STATUS.md)

---

## 🚀 Next Steps

After installation:

1. **Try Falkor**: `falkor`
2. **Get more models**: `ollama pull llama3.1:8b`
3. **Read docs**: Check the README
4. **Share with team**: Send install link!

---

**Installation time**: 5-15 minutes  
**Difficulty**: Easy  
**Support**: Full

🐉 **Welcome to Falkor!**
