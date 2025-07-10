#!/bin/bash
set -e

# Print section header
echo "======================="
echo "MegaParse Installer"
echo "======================="

# Create and activate virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install basic dependencies
echo "Installing basic dependencies..."
pip install -e .

# Check operating system for system dependencies
OS="$(uname)"
if [[ "$OS" == "Darwin" ]]; then
    echo "MacOS detected, installing system dependencies..."
    
    # Check if Homebrew is installed
    if ! command -v brew &> /dev/null; then
        echo "Homebrew not found! Please install Homebrew first:"
        echo '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
        exit 1
    fi
    
    # Install dependencies
    echo "Installing poppler (for PDF processing)..."
    brew install poppler
    
    echo "Installing tesseract (for OCR)..."
    brew install tesseract
    
    echo "Installing libmagic (for file type detection)..."
    brew install libmagic
    
elif [[ "$OS" == "Linux" ]]; then
    echo "Linux detected, installing system dependencies..."
    
    # Check for apt (Debian/Ubuntu)
    if command -v apt-get &> /dev/null; then
        echo "Debian/Ubuntu detected, using apt..."
        sudo apt-get update
        sudo apt-get install -y poppler-utils tesseract-ocr libmagic-dev
    
    # Check for dnf (Fedora/RHEL)
    elif command -v dnf &> /dev/null; then
        echo "Fedora/RHEL detected, using dnf..."
        sudo dnf install -y poppler-utils tesseract libmagic
    
    # Check for pacman (Arch Linux)
    elif command -v pacman &> /dev/null; then
        echo "Arch Linux detected, using pacman..."
        sudo pacman -Sy poppler tesseract tesseract-data-eng file
    
    else
        echo "Unsupported Linux distribution. Please install the following packages manually:"
        echo "- poppler-utils (or equivalent)"
        echo "- tesseract-ocr"
        echo "- libmagic"
        echo "Then run this script again."
        exit 1
    fi

elif [[ "$OS" == "MINGW"* || "$OS" == "MSYS"* || "$OS" == "CYGWIN"* ]]; then
    echo "Windows detected. Please ensure you have the following installed:"
    echo "- Poppler for Windows: https://github.com/oschwartz10612/poppler-windows/releases/"
    echo "- Tesseract OCR: https://github.com/UB-Mannheim/tesseract/wiki"
    echo "Add them to your PATH environment variable and run this script again."
    echo "Press Enter to continue or Ctrl+C to exit and install these dependencies..."
    read -r
fi

# Create .env file from example if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "Please edit the .env file with your API keys."
fi

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.lock

# Install MegaParse 
echo "Installing MegaParse from local directory..."
mkdir -p libs
cd libs

# Clone and install MegaParse if not already present
if [ ! -d "megaparse" ]; then
    echo "Cloning MegaParse repository..."
    git clone https://github.com/quivrhq/megaparse megaparse
fi

# Enter directory and install
cd megaparse
pip install -e .
cd ../..

echo "======================="
echo "Installation Complete!"
echo "======================="
echo "To use MegaParse:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Edit your .env file with appropriate API keys"
echo "3. See example usage in the README.md"
echo "4. Run 'python3 -c \"from megaparse import MegaParse; print(\"MegaParse installed successfully\")\"' to verify installation"
