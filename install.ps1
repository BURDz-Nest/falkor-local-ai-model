# Falkor Local AI Assistant - Installation Script
# For Windows (PowerShell)

# Requires PowerShell 5.1 or higher
#Requires -Version 5.1

# Configuration
$REQUIRED_PYTHON_VERSION = "3.11"
$DEFAULT_MODEL = "gemma2:2b"
$INSTALL_DIR = "$env:USERPROFILE\.falkor"
$SCRIPTS_DIR = "$env:USERPROFILE\AppData\Local\Microsoft\WindowsApps"

# Color functions
function Write-Header {
    Write-Host ""
    Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Blue
    Write-Host "  🐉 Falkor Local AI Assistant - Installer" -ForegroundColor Blue
    Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Blue
    Write-Host ""
}

function Write-Success {
    param([string]$Message)
    Write-Host "✓ $Message" -ForegroundColor Green
}

function Write-Error-Custom {
    param([string]$Message)
    Write-Host "✗ $Message" -ForegroundColor Red
}

function Write-Info {
    param([string]$Message)
    Write-Host "ℹ $Message" -ForegroundColor Cyan
}

function Write-Warning-Custom {
    param([string]$Message)
    Write-Host "⚠ $Message" -ForegroundColor Yellow
}

# Check if command exists
function Test-Command {
    param([string]$Command)
    $null -ne (Get-Command $Command -ErrorAction SilentlyContinue)
}

# Compare versions
function Test-VersionGreaterOrEqual {
    param(
        [string]$Version,
        [string]$RequiredVersion
    )
    
    [version]$v1 = $Version
    [version]$v2 = $RequiredVersion
    
    return $v1 -ge $v2
}

# Check Python installation
function Test-Python {
    Write-Info "Checking Python installation..."
    
    if (Test-Command python) {
        $pythonVersion = (python --version 2>&1) -replace 'Python ', ''
        Write-Info "Found Python $pythonVersion"
        
        # Extract major.minor version
        $versionParts = $pythonVersion -split '\.' 
        $majorMinor = "$($versionParts[0]).$($versionParts[1])"
        
        if (Test-VersionGreaterOrEqual -Version $majorMinor -RequiredVersion $REQUIRED_PYTHON_VERSION) {
            Write-Success "Python version is sufficient (>= $REQUIRED_PYTHON_VERSION)"
            return $true
        } else {
            Write-Error-Custom "Python $REQUIRED_PYTHON_VERSION or higher is required"
            Write-Info "Current version: $pythonVersion"
            return $false
        }
    } else {
        Write-Error-Custom "Python is not installed or not in PATH"
        return $false
    }
}

# Install Python instructions
function Show-PythonInstallInstructions {
    Write-Warning-Custom "Python $REQUIRED_PYTHON_VERSION or higher is required"
    Write-Host ""
    Write-Info "Download Python from:"
    Write-Host "  https://www.python.org/downloads/" -ForegroundColor Cyan
    Write-Host ""
    Write-Info "Make sure to check 'Add Python to PATH' during installation!"
    Write-Host ""
    
    $continue = Read-Host "Continue without Python? (y/N)"
    if ($continue -ne 'y' -and $continue -ne 'Y') {
        exit 1
    }
}

# Check Ollama installation
function Test-Ollama {
    Write-Info "Checking Ollama installation..."
    
    if (Test-Command ollama) {
        Write-Success "Ollama found"
        return $true
    } else {
        Write-Warning-Custom "Ollama not found"
        return $false
    }
}

# Install Ollama
function Install-Ollama {
    Write-Info "Installing Ollama for Windows..."
    Write-Info "Opening Ollama download page..."
    
    # Open Ollama website
    Start-Process "https://ollama.com/download/windows"
    
    Write-Host ""
    Write-Warning-Custom "Please download and install Ollama from the opened browser window"
    Write-Info "After installation, restart this script."
    Write-Host ""
    
    $continue = Read-Host "Have you installed Ollama? (y/N)"
    if ($continue -ne 'y' -and $continue -ne 'Y') {
        Write-Info "Installation cancelled. Please install Ollama and run this script again."
        exit 1
    }
    
    # Verify installation
    if (Test-Command ollama) {
        Write-Success "Ollama installed successfully"
    } else {
        Write-Error-Custom "Ollama still not found. Please add it to PATH and restart."
        exit 1
    }
}

# Install Falkor files
function Install-Falkor {
    Write-Info "Installing Falkor to $INSTALL_DIR..."
    
    # Remove existing installation
    if (Test-Path $INSTALL_DIR) {
        Write-Warning-Custom "Existing installation found"
        $remove = Read-Host "Remove and reinstall? (y/N)"
        
        if ($remove -eq 'y' -or $remove -eq 'Y') {
            Remove-Item -Path $INSTALL_DIR -Recurse -Force
            Write-Success "Removed old installation"
        } else {
            Write-Error-Custom "Installation cancelled"
            exit 1
        }
    }
    
    # Create installation directory
    New-Item -ItemType Directory -Path $INSTALL_DIR -Force | Out-Null
    
    # Copy files (assuming script is run from repo root)
    if (Test-Path "falkor") {
        Write-Info "Copying Falkor files..."
        Copy-Item -Path "falkor" -Destination $INSTALL_DIR -Recurse -Force
        Copy-Item -Path "main.py" -Destination $INSTALL_DIR -Force
        
        if (Test-Path "requirements.txt") {
            Copy-Item -Path "requirements.txt" -Destination $INSTALL_DIR -Force
        } else {
            # Create minimal requirements.txt
            @"
rich>=13.7.0
httpx>=0.27.0
prompt-toolkit>=3.0.0
"@ | Out-File -FilePath "$INSTALL_DIR\requirements.txt" -Encoding UTF8
        }
        
        Write-Success "Files copied"
    } else {
        Write-Error-Custom "Falkor files not found. Are you running this from the repository?"
        exit 1
    }
}

# Install Python dependencies
function Install-Dependencies {
    Write-Info "Installing Python dependencies..."
    
    Push-Location $INSTALL_DIR
    
    try {
        python -m pip install --user -q -r requirements.txt
        Write-Success "Dependencies installed"
    } catch {
        Write-Error-Custom "Failed to install dependencies: $_"
        Pop-Location
        exit 1
    }
    
    Pop-Location
}

# Pull default model
function Install-DefaultModel {
    Write-Info "Pulling default model: $DEFAULT_MODEL (~1.6GB)..."
    Write-Warning-Custom "This may take a few minutes depending on your connection"
    
    try {
        ollama pull $DEFAULT_MODEL
        Write-Success "Model downloaded successfully"
    } catch {
        Write-Warning-Custom "Failed to download model. You can do this later with:"
        Write-Info "  ollama pull $DEFAULT_MODEL"
    }
}

# Setup falkor command
function Set-FalkorCommand {
    Write-Info "Setting up 'falkor' command..."
    
    # Create batch file wrapper
    $batchContent = @"
@echo off
python "$INSTALL_DIR\main.py" %*
"@
    
    $batchPath = "$INSTALL_DIR\falkor.bat"
    $batchContent | Out-File -FilePath $batchPath -Encoding ASCII -Force
    
    Write-Success "Command script created"
    
    # Add to PATH if not already there
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    
    if ($userPath -notlike "*$INSTALL_DIR*") {
        Write-Info "Adding Falkor to PATH..."
        [Environment]::SetEnvironmentVariable(
            "Path",
            "$userPath;$INSTALL_DIR",
            "User"
        )
        Write-Success "Added to PATH (restart terminal to use 'falkor' command)"
    } else {
        Write-Success "Falkor is already in PATH"
    }
    
    # Also create PowerShell script
    $psContent = @"
# Falkor launcher
python "$INSTALL_DIR\main.py" `$args
"@
    
    $psPath = "$INSTALL_DIR\falkor.ps1"
    $psContent | Out-File -FilePath $psPath -Encoding UTF8 -Force
}

# Create uninstall script
function New-UninstallScript {
    $uninstallContent = @'
# Uninstall Falkor

Write-Host "Uninstalling Falkor..." -ForegroundColor Yellow

# Remove installation
if (Test-Path "$env:USERPROFILE\.falkor") {
    Remove-Item -Path "$env:USERPROFILE\.falkor" -Recurse -Force
    Write-Host "✓ Removed ~/.falkor" -ForegroundColor Green
}

# Remove from PATH
$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($userPath -like "*$env:USERPROFILE\.falkor*") {
    $newPath = $userPath -replace "[;]?$env:USERPROFILE\\.falkor[;]?", ""
    [Environment]::SetEnvironmentVariable("Path", $newPath, "User")
    Write-Host "✓ Removed from PATH" -ForegroundColor Green
}

Write-Host ""
Write-Host "Falkor has been uninstalled." -ForegroundColor Green
Write-Host "Note: Ollama and models were NOT removed."
Write-Host "To remove Ollama: see https://ollama.com/"
Write-Host ""
'@
    
    $uninstallPath = "$INSTALL_DIR\uninstall.ps1"
    $uninstallContent | Out-File -FilePath $uninstallPath -Encoding UTF8 -Force
    
    Write-Success "Created uninstall script: $uninstallPath"
}

# Main installation flow
function Main {
    Write-Header
    
    # Check Python
    if (-not (Test-Python)) {
        Show-PythonInstallInstructions
    }
    
    Write-Host ""
    
    # Check Ollama
    if (-not (Test-Ollama)) {
        $install = Read-Host "Install Ollama now? (Y/n)"
        if ($install -ne 'n' -and $install -ne 'N') {
            Install-Ollama
        } else {
            Write-Warning-Custom "Skipping Ollama installation"
            Write-Info "You can install it later from: https://ollama.com/"
        }
    }
    
    Write-Host ""
    
    # Install Falkor
    Install-Falkor
    
    Write-Host ""
    
    # Install dependencies
    Install-Dependencies
    
    Write-Host ""
    
    # Pull default model
    $downloadModel = Read-Host "Download default model ($DEFAULT_MODEL ~1.6GB)? (Y/n)"
    if ($downloadModel -ne 'n' -and $downloadModel -ne 'N') {
        Install-DefaultModel
    } else {
        Write-Info "Skipping model download. You can pull models later with:"
        Write-Info "  ollama pull $DEFAULT_MODEL"
    }
    
    Write-Host ""
    
    # Setup command
    Set-FalkorCommand
    
    Write-Host ""
    
    # Create uninstall script
    New-UninstallScript
    
    # Success message
    Write-Host ""
    Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Green
    Write-Host "  ✓ Falkor installed successfully!" -ForegroundColor Green
    Write-Host "═══════════════════════════════════════════════════════" -ForegroundColor Green
    Write-Host ""
    Write-Info "To start Falkor, open a NEW PowerShell window and type:"
    Write-Host "  falkor" -ForegroundColor Cyan
    Write-Host ""
    Write-Info "Or run directly:"
    Write-Host "  python $INSTALL_DIR\main.py" -ForegroundColor Cyan
    Write-Host ""
    Write-Info "To uninstall:"
    Write-Host "  $INSTALL_DIR\uninstall.ps1" -ForegroundColor Cyan
    Write-Host ""
    Write-Info "Need help? Type '/help' in Falkor or visit:"
    Write-Host "  https://github.com/BURDz-Nest/falkor-local-ai-model"
    Write-Host ""
}

# Run main function
try {
    Main
} catch {
    Write-Host ""
    Write-Error-Custom "Installation failed: $_"
    Write-Host ""
    exit 1
}
