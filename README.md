# 🐉 Falkor - Your Local AI Assistant

**A beautiful, fast, local AI chat application powered by Ollama.**

Falkor brings ChatGPT-like experience to your local machine - no cloud, no API keys, complete privacy!

---

## ✨ Features

- 🌊 **Streaming responses** - Token-by-token typewriter effect
- 🎨 **Beautiful UI** - Code Puppy-inspired interface
- 🚀 **Fast & Local** - All processing on your machine
- 🔒 **100% Private** - Your data never leaves your computer
- 🎯 **Easy model switching** - Interactive model selector
- 💬 **Conversation history** - Maintains context automatically
- 📱 **Cross-platform** - Works on macOS, Linux, and Windows

---

## 🚀 Quick Start

### macOS / Linux

**One-line installation:**

```bash
curl -fsSL https://raw.githubusercontent.com/BURDz-Nest/falkor-local-ai-model/main/install.sh | bash
```

**Or manual installation:**

```bash
# Clone the repository
git clone https://github.com/BURDz-Nest/falkor-local-ai-model.git
cd falkor-local-ai-model

# Run installer
bash install.sh
```

### Windows

**PowerShell installation:**

```powershell
# Download and run installer
irm https://raw.githubusercontent.com/BURDz-Nest/falkor-local-ai-model/main/install.ps1 | iex
```

**Or manual installation:**

```powershell
# Clone the repository
git clone https://github.com/BURDz-Nest/falkor-local-ai-model.git
cd falkor-local-ai-model

# Run installer
.\install.ps1
```

---

## 📋 Requirements

### Automatic (Installer handles these)

- **Python 3.11+** (installer checks/prompts)
- **Ollama** (installer installs if needed)
- **Default model** `gemma2:2b` (~1.6GB, installer downloads)

### Manual Requirements

If installing manually:

1. **Python 3.11+**
   - macOS: `brew install python@3.11`
   - Linux: `apt install python3.11` / `dnf install python3.11`
   - Windows: https://www.python.org/downloads/

2. **Ollama**
   - All platforms: https://ollama.com/download

3. **Python packages**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

### Start Falkor

After installation, just type:

```bash
falkor
```

### First Time

You'll see:

```
╔═══════════════════════════════════════════════════════╗
║      ########    #    ##       ##  ##  ####  ####     ║
║      ##         # #   ##       ## ##  ##  ## ##  ##   ║
║      #####     #####  ##       ####   ##  ## ####     ║
║      ##       ##   ## ##       ## ##  ##  ## ## ##    ║
║      ##       ##   ## ######## ##  ##  ####  ##  ##   ║
║                                                       ║
║         >> Your Local Knowledge Assistant <<         ║
╚═══════════════════════════════════════════════════════╝

[gemma2:2b] (~/projects)
You: _
```

### Commands

| Command | Description |
|---------|-------------|
| `/help` | Show all commands |
| `/model` | Switch models (interactive dropdown) |
| `/history` | Show conversation history |
| `/clear` | Clear screen |
| `exit` | Quit Falkor |

### Interactive Model Selector

Type `/model` to see:

```
=============== Model Selection ===============

  Select a model to use
  Current model: gemma2:2b

================================================

  ✓ gemma2:2b (current)
    llama3.1:8b
    qwen2.5-coder:32b

(Use ↑↓ arrows, Enter to confirm, Esc to cancel)
```

---

## 🎯 Getting More Models

### Quick Guide

```bash
# Fast & lightweight (700MB)
ollama pull qwen2.5:1.5b

# General purpose (4.7GB) - RECOMMENDED
ollama pull llama3.1:8b

# Best for coding (19GB)
ollama pull qwen2.5-coder:32b

# Balanced (4.7GB)
ollama pull qwen2.5:7b

# Instruction following (4.1GB)
ollama pull mistral:7b
```

### After Pulling a Model

1. Restart Falkor (type `exit` then `falkor`)
2. Type `/model` to see your new model
3. Use arrow keys to select it

**For complete model guide, see [MODELS.md](MODELS.md)**

---

## 🛠️ Troubleshooting

### "Command not found: falkor"

**macOS/Linux:**
```bash
source ~/.zshrc  # or ~/.bashrc
```

**Windows:**
- Restart PowerShell/Terminal
- Or run directly: `python ~/.falkor/main.py`

### "Cannot connect to Ollama"

```bash
# Check if Ollama is running
ollama list

# If not installed
# macOS/Linux: https://ollama.com/download
# Windows: https://ollama.com/download/windows
```

### "Model not found"

```bash
# Pull the model first
ollama pull qwen2.5:1.5b

# Then restart Falkor
```

### Slow Responses

- Try a smaller model: `ollama pull qwen2.5:1.5b`
- Close other applications
- Check CPU/RAM usage

---

## 🗑️ Uninstall

### macOS / Linux

```bash
~/.falkor/uninstall.sh
```

### Windows

```powershell
~/.falkor/uninstall.ps1
```

**Note**: This removes Falkor but keeps Ollama and models.

---

## 📚 Documentation

### User Guides
- **[Installation Guide](INSTALLATION.md)** - Complete installation walkthrough
- **[Models Guide](MODELS.md)** - How to manage Ollama models
- **[Uninstall Guide](UNINSTALL.md)** - How to remove Falkor

### Developer Docs
- **[Project Status](PROJECT_STATUS.md)** - Roadmap & features
- **[Streaming](STREAMING.md)** - How streaming works
- **[Testing Guide](TESTING_GUIDE.md)** - How to test

---

## 🏗️ Architecture

```
falkor/
├── cli/
│   ├── app.py           # Main application
│   ├── renderer.py      # Rich UI rendering
│   └── interactive.py   # Interactive menus
├── models/
│   └── ollama_client.py # Ollama API client
└── main.py              # Entry point
```

**Total code**: ~750 lines (all files under 300 lines!)  
**Dependencies**: Rich, httpx, prompt-toolkit  
**License**: MIT

---

## 🎨 Code Quality

- ✅ **DRY** - No code duplication
- ✅ **SOLID** - Single responsibility
- ✅ **Type hints** - 100% coverage
- ✅ **Docstrings** - Comprehensive
- ✅ **Error handling** - Robust
- ✅ **Small files** - All under 300 lines

---

## 🤝 Contributing

This is a private team repository. For access, contact the repository owner.

### Development Setup

```bash
# Clone repository
git clone https://github.com/BURDz-Nest/falkor-local-ai-model.git
cd falkor-local-ai-model

# Install dependencies
pip install -r requirements.txt

# Run locally
python main.py
```

---

## 📝 Version History

### v0.1.0 (Current)
- ✅ Core chat functionality
- ✅ Streaming responses
- ✅ Interactive model selector
- ✅ Beautiful UI
- ✅ Cross-platform support
- ✅ One-line installers

### Coming Soon (v0.2.0)
- 🔄 Help Agent (built-in Falkor assistant)
- 🔄 Session persistence
- 🔄 Export conversations
- 🔄 Configuration system

---

## ⚖️ License

MIT License - See [LICENSE](LICENSE) for details

---

## 🙏 Acknowledgments

- **Ollama** - Local LLM runtime
- **Rich** - Beautiful terminal UI
- **Code Puppy** - UI inspiration

---

## 📞 Support

- **Issues**: Open an issue on GitHub
- **Questions**: Use `/help` in Falkor
- **Documentation**: See docs/ folder

---

**Built with ❤️ for local AI enthusiasts**

🐉 *"Your knowledge, your machine, your control"*
