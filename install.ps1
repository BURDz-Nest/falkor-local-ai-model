# Falkor Local AI Assistant - Full Installer
# For Windows (PowerShell)

# Requires PowerShell 5.1 or higher
#Requires -Version 5.1

# Configuration
$REQUIRED_PYTHON_VERSION = "3.11"
$DEFAULT_MODEL = "gemma2:2b"
$REPO_URL = "https://github.com/BURDz-Nest/falkor-local-ai-model.git"

# Allow overriding the install dir for testing
if ($null -eq $env:FALKOR_TEST_DIR) {
    $INSTALL_DIR = "$env:USERPROFILE\.falkor"
} else {
    $INSTALL_DIR = $env:FALKOR_TEST_DIR
    Write-Host "[TEST MODE] Installing to: $INSTALL_DIR" -ForegroundColor Yellow
}

# Color functions
function Write-Header {
    Write-Host ""
    Write-Host "=======================================================" -ForegroundColor Blue
    Write-Host "   Falkor Local AI Assistant - Installer" -ForegroundColor Blue
    Write-Host "=======================================================" -ForegroundColor Blue
    Write-Host ""
}

function Write-Success {
    param([string]$Message)
    Write-Host "[OK] $Message" -ForegroundColor Green
}

function Write-Error-Custom {
    param([string]$Message)
    Write-Host "[ERROR] $Message" -ForegroundColor Red
}

function Write-Info {
    param([string]$Message)
    Write-Host "[INFO] $Message" -ForegroundColor Cyan
}

function Write-Warning-Custom {
    param([string]$Message)
    Write-Host "[WARN] $Message" -ForegroundColor Yellow
}

# Check if command exists
function Test-Command-Exists {
    param([string]$Cmd)
    return $null -ne (Get-Command $Cmd -ErrorAction SilentlyContinue)
}

# Check Python installation
function Check-Python {
    Write-Info "Checking Python installation..."
    if (Test-Command-Exists python) {
        $version = (python --version 2>&1) -replace 'Python ', ''
        Write-Success "Found Python $version"
        return $true
    } else {
        Write-Error-Custom "Python is not installed or not in PATH."
        Write-Info "Please install Python 3.11+ from https://python.org"
        return $false
    }
}

# Check Ollama installation
function Check-Ollama {
    Write-Info "Checking Ollama..."
    if (Test-Command-Exists ollama) {
        Write-Success "Ollama is installed."
        return $true
    } else {
        Write-Warning-Custom "Ollama not found."
        Write-Info "Falkor requires Ollama to run local models."
        Write-Info "Download it from: https://ollama.com/download/windows"
        return $false
    }
}

# Clone or Update Falkor
function Sync-Falkor {
    Write-Info "Downloading Falkor from GitHub..."
    
    if (Test-Path $INSTALL_DIR) {
        Write-Info "Updating existing installation at $INSTALL_DIR..."
        if (Test-Path "$INSTALL_DIR\.git") {
            Push-Location $INSTALL_DIR
            git pull origin main
            Pop-Location
        } else {
            Write-Warning-Custom "Non-git directory found at $INSTALL_DIR. Reinstalling..."
            Remove-Item -Path $INSTALL_DIR -Recurse -Force
            git clone $REPO_URL $INSTALL_DIR
        }
    } else {
        Write-Info "Cloning repository to $INSTALL_DIR (branch: feature/windows-one-step-installer)..."
        if (Test-Command-Exists git) {
            git clone -b feature/windows-one-step-installer $REPO_URL $INSTALL_DIR
        } else {
            Write-Error-Custom "Git is not installed. Please install Git for Windows."
            exit 1
        }
    }
    
    if (-not (Test-Path "$INSTALL_DIR\main.py")) {
        Write-Error-Custom "Failed to download Falkor files."
        exit 1
    }
    Write-Success "Falkor files ready."
}

# Install Python dependencies
function Install-Deps {
    Write-Info "Installing Python dependencies..."
    try {
        python -m pip install --user -q -r "$INSTALL_DIR\requirements.txt"
        Write-Success "Dependencies installed."
    } catch {
        Write-Error-Custom "Failed to install dependencies."
    }
}

# Pull default model
function Pull-Model {
    if (Test-Command-Exists ollama) {
        Write-Info "Ensuring default model ($DEFAULT_MODEL) is available..."
        ollama pull $DEFAULT_MODEL
        Write-Success "Model ready."
    }
}

# Setup falkor command
function Setup-Command {
    Write-Info "Setting up 'falkor' command..."
    
    $batchContent = "@echo off`r`npython `"$INSTALL_DIR\main.py`" %*"
    $batchPath = "$INSTALL_DIR\falkor.bat"
    $batchContent | Out-File -FilePath $batchPath -Encoding ASCII -Force
    
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    if ($userPath -notlike "*$INSTALL_DIR*") {
        [Environment]::SetEnvironmentVariable("Path", "$userPath;$INSTALL_DIR", "User")
        Write-Success "Added to PATH (Restart terminal to use 'falkor' command)."
    } else {
        Write-Success "Falkor is already in PATH."
    }
}

# Main function
function Main {
    Write-Header
    
    if (-not (Check-Python)) { return }
    Check-Ollama
    
    Sync-Falkor
    Install-Deps
    Pull-Model
    Setup-Command

    Write-Host ""
    Write-Host "=======================================================" -ForegroundColor Green
    Write-Host "   Falkor installed successfully!" -ForegroundColor Green
    Write-Host "=======================================================" -ForegroundColor Green
    Write-Host ""
    Write-Info "1. Restart your PowerShell window."
    Write-Info "2. Type: falkor"
    Write-Host ""
}

# Execute
try {
    Main
} catch {
    Write-Host ""
    Write-Host "[ERROR] Installation failed: $_" -ForegroundColor Red
    Write-Host ""
    exit 1
}
