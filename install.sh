#!/usr/bin/env bash
# Falkor Local AI Assistant - Installation Script
# For macOS and Linux

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
REQUIRED_PYTHON_VERSION="3.11"
DEFAULT_MODEL="gemma2:2b"
INSTALL_DIR="$HOME/.falkor"
BIN_DIR="$HOME/bin"

# Print functions
print_header() {
    echo ""
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}  🐉 Falkor Local AI Assistant - Installer${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Compare version numbers
version_ge() {
    printf '%s\n%s\n' "$2" "$1" | sort -V -C
}

# Check Python version
check_python() {
    print_info "Checking Python installation..."
    
    if command_exists python3; then
        PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
        print_info "Found Python $PYTHON_VERSION"
        
        if version_ge "$PYTHON_VERSION" "$REQUIRED_PYTHON_VERSION"; then
            print_success "Python version is sufficient (>= $REQUIRED_PYTHON_VERSION)"
            return 0
        else
            print_error "Python $REQUIRED_PYTHON_VERSION or higher is required"
            print_info "Current version: $PYTHON_VERSION"
            return 1
        fi
    else
        print_error "Python 3 is not installed"
        return 1
    fi
}

# Install Python (if needed)
install_python() {
    print_warning "Python $REQUIRED_PYTHON_VERSION or higher is required"
    echo ""
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        print_info "On macOS, you can install Python via:"
        echo "  1. Homebrew: brew install python@3.11"
        echo "  2. Official installer: https://www.python.org/downloads/"
    else
        print_info "On Linux, install via your package manager:"
        echo "  Ubuntu/Debian: sudo apt install python3.11"
        echo "  Fedora/RHEL: sudo dnf install python3.11"
        echo "  Arch: sudo pacman -S python"
    fi
    
    echo ""
    read -p "Would you like to continue without Python? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
}

# Check/Install Ollama
check_ollama() {
    print_info "Checking Ollama installation..."
    
    # Check common Ollama locations
    OLLAMA_CMD=""
    if command_exists ollama; then
        OLLAMA_CMD="ollama"
    elif [ -f "$HOME/bin/ollama" ]; then
        OLLAMA_CMD="$HOME/bin/ollama"
    elif [ -f "/usr/local/bin/ollama" ]; then
        OLLAMA_CMD="/usr/local/bin/ollama"
    fi
    
    if [ -n "$OLLAMA_CMD" ]; then
        print_success "Ollama found: $OLLAMA_CMD"
        return 0
    else
        print_warning "Ollama not found"
        return 1
    fi
}

# Install Ollama
install_ollama() {
    print_info "Installing Ollama..."
    
    if [[ "$OSTYPE" == "darwin"* ]]; then
        print_info "Downloading Ollama for macOS..."
        curl -fsSL https://ollama.com/install.sh | sh
    else
        print_info "Downloading Ollama for Linux..."
        curl -fsSL https://ollama.com/install.sh | sh
    fi
    
    if [ $? -eq 0 ]; then
        print_success "Ollama installed successfully"
        # Set OLLAMA_CMD for later use
        if command_exists ollama; then
            OLLAMA_CMD="ollama"
        elif [ -f "$HOME/bin/ollama" ]; then
            OLLAMA_CMD="$HOME/bin/ollama"
        fi
    else
        print_error "Failed to install Ollama"
        exit 1
    fi
}

# Clone or download Falkor
install_falkor() {
    print_info "Installing Falkor to $INSTALL_DIR..."
    
    # Remove existing installation
    if [ -d "$INSTALL_DIR" ]; then
        print_warning "Existing installation found"
        read -p "Remove and reinstall? (y/N) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            rm -rf "$INSTALL_DIR"
            print_success "Removed old installation"
        else
            print_error "Installation cancelled"
            exit 1
        fi
    fi
    
    # Create installation directory
    mkdir -p "$INSTALL_DIR"
    
    # Copy files (assuming script is run from repo root)
    if [ -d "falkor" ]; then
        print_info "Copying Falkor files..."
        cp -r falkor "$INSTALL_DIR/"
        cp main.py "$INSTALL_DIR/"
        cp requirements.txt "$INSTALL_DIR/" 2>/dev/null || echo "rich>=13.7.0\nhttpx>=0.27.0\nprompt-toolkit>=3.0.0" > "$INSTALL_DIR/requirements.txt"
        print_success "Files copied"
    else
        print_error "Falkor files not found. Are you running this from the repository?"
        exit 1
    fi
}

# Install Python dependencies
install_dependencies() {
    print_info "Installing Python dependencies..."
    
    cd "$INSTALL_DIR"
    
    # Try pip install
    if python3 -m pip install --user -q -r requirements.txt; then
        print_success "Dependencies installed"
    else
        print_error "Failed to install dependencies"
        exit 1
    fi
}

# Pull default model
pull_default_model() {
    print_info "Pulling default model: $DEFAULT_MODEL (~1.6GB)..."
    print_warning "This may take a few minutes depending on your connection"
    
    # Determine Ollama command
    if command_exists ollama; then
        OLLAMA_CMD="ollama"
    elif [ -f "$HOME/bin/ollama" ]; then
        OLLAMA_CMD="$HOME/bin/ollama"
    else
        print_error "Ollama command not found"
        return 1
    fi
    
    # Pull the model
    if $OLLAMA_CMD pull "$DEFAULT_MODEL"; then
        print_success "Model downloaded successfully"
    else
        print_warning "Failed to download model. You can do this later with:"
        print_info "  $OLLAMA_CMD pull $DEFAULT_MODEL"
    fi
}

# Setup falkor command
setup_command() {
    print_info "Setting up 'falkor' command..."
    
    # Create bin directory if needed
    mkdir -p "$BIN_DIR"
    
    # Create executable script
    cat > "$BIN_DIR/falkor" << 'EOF'
#!/usr/bin/env python3
"""Falkor - Your Local Knowledge Assistant."""
import sys
import os

# Add Falkor to Python path
FALKOR_DIR = os.path.expanduser("~/.falkor")
sys.path.insert(0, FALKOR_DIR)
os.chdir(FALKOR_DIR)

# Import and run
from falkor.cli.app import main

if __name__ == "__main__":
    main()
EOF
    
    # Make executable
    chmod +x "$BIN_DIR/falkor"
    
    print_success "Command created: $BIN_DIR/falkor"
    
    # Check if bin is in PATH
    if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
        print_warning "$BIN_DIR is not in your PATH"
        print_info "Add this to your ~/.zshrc or ~/.bashrc:"
        echo "  export PATH=\"\$HOME/bin:\$PATH\""
        echo ""
        print_info "Then reload: source ~/.zshrc"
    else
        print_success "$BIN_DIR is already in PATH"
    fi
}

# Create uninstall script
create_uninstall() {
    cat > "$INSTALL_DIR/uninstall.sh" << 'EOF'
#!/usr/bin/env bash
# Uninstall Falkor

echo "Uninstalling Falkor..."

# Remove installation
if [ -d "$HOME/.falkor" ]; then
    rm -rf "$HOME/.falkor"
    echo "✓ Removed ~/.falkor"
fi

# Remove command
if [ -f "$HOME/bin/falkor" ]; then
    rm "$HOME/bin/falkor"
    echo "✓ Removed ~/bin/falkor command"
fi

echo ""
echo "Falkor has been uninstalled."
echo "Note: Ollama and models were NOT removed."
echo "To remove Ollama: see https://ollama.com/"
echo ""
EOF
    
    chmod +x "$INSTALL_DIR/uninstall.sh"
    print_success "Created uninstall script: $INSTALL_DIR/uninstall.sh"
}

# Main installation flow
main() {
    print_header
    
    # Check Python
    if ! check_python; then
        install_python
    fi
    
    echo ""
    
    # Check Ollama
    if ! check_ollama; then
        read -p "Install Ollama now? (Y/n) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Nn]$ ]]; then
            install_ollama
        else
            print_warning "Skipping Ollama installation"
            print_info "You can install it later from: https://ollama.com/"
        fi
    fi
    
    echo ""
    
    # Install Falkor
    install_falkor
    
    echo ""
    
    # Install dependencies
    install_dependencies
    
    echo ""
    
    # Pull default model
    read -p "Download default model ($DEFAULT_MODEL ~700MB)? (Y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        pull_default_model
    else
        print_info "Skipping model download. You can pull models later with:"
        print_info "  ollama pull $DEFAULT_MODEL"
    fi
    
    echo ""
    
    # Setup command
    setup_command
    
    echo ""
    
    # Create uninstall script
    create_uninstall
    
    # Success message
    echo ""
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}  ✓ Falkor installed successfully!${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    print_info "To start Falkor, type:"
    echo -e "  ${BLUE}falkor${NC}"
    echo ""
    print_info "If 'command not found', reload your shell:"
    echo -e "  ${BLUE}source ~/.zshrc${NC}  # or ~/.bashrc"
    echo ""
    print_info "To uninstall:"
    echo -e "  ${BLUE}~/.falkor/uninstall.sh${NC}"
    echo ""
    print_info "Need help? Type '/help' in Falkor or visit:"
    echo "  https://github.com/BURDz-Nest/falkor-local-ai-model"
    echo ""
}

# Run main function
main
