#!/usr/bin/env python
"""
MegaParse Setup Helper

This script automates the setup and testing of MegaParse with cost optimization.
It provides a user-friendly interface for installing and configuring MegaParse.
"""

import os
import sys
import subprocess
import argparse
import platform
from pathlib import Path

def print_section(title):
    """Print a section header"""
    print("\n" + "=" * 50)
    print(f" {title}")
    print("=" * 50)

def run_command(command, check=True):
    """Run a shell command and return the result"""
    try:
        result = subprocess.run(command, shell=True, check=check, 
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               text=True)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Exit code: {e.returncode}")
        print(f"Output: {e.output}")
        if check:
            raise
        return e

def check_system_dependencies():
    """Check if required system dependencies are installed"""
    print_section("Checking System Dependencies")
    
    missing_deps = []
    system = platform.system()
    
    if system == "Darwin":  # macOS
        # Check if brew is installed
        brew_result = run_command("which brew", check=False)
        if brew_result.returncode != 0:
            print("❌ Homebrew not found. Please install Homebrew:")
            print("   /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
            missing_deps.append("brew")
        
        # Check for poppler (for PDF processing)
        poppler_result = run_command("which pdfinfo", check=False)
        if poppler_result.returncode != 0:
            print("❌ Poppler not found (needed for PDF processing)")
            missing_deps.append("poppler")
        else:
            print("✅ Poppler installed")
            
        # Check for tesseract (for OCR)
        tesseract_result = run_command("which tesseract", check=False)
        if tesseract_result.returncode != 0:
            print("❌ Tesseract not found (needed for OCR)")
            missing_deps.append("tesseract")
        else:
            print("✅ Tesseract installed")
            
        # Check for libmagic (for file type detection)
        libmagic_result = run_command("brew list | grep libmagic", check=False)
        if libmagic_result.returncode != 0:
            print("❌ libmagic not found (needed for file type detection)")
            missing_deps.append("libmagic")
        else:
            print("✅ libmagic installed")
    
    elif system == "Linux":
        # Check for poppler-utils
        poppler_result = run_command("which pdfinfo", check=False)
        if poppler_result.returncode != 0:
            print("❌ poppler-utils not found (needed for PDF processing)")
            missing_deps.append("poppler-utils")
        else:
            print("✅ poppler-utils installed")
            
        # Check for tesseract
        tesseract_result = run_command("which tesseract", check=False)
        if tesseract_result.returncode != 0:
            print("❌ tesseract-ocr not found (needed for OCR)")
            missing_deps.append("tesseract-ocr")
        else:
            print("✅ tesseract-ocr installed")
            
        # Check for libmagic
        libmagic_result = run_command("ldconfig -p | grep libmagic", check=False)
        if libmagic_result.returncode != 0:
            print("❌ libmagic not found (needed for file type detection)")
            missing_deps.append("libmagic")
        else:
            print("✅ libmagic installed")
    
    elif system == "Windows":
        print("Windows detected. Please ensure you have the following installed:")
        print("- Poppler for Windows: https://github.com/oschwartz10612/poppler-windows/releases/")
        print("- Tesseract OCR: https://github.com/UB-Mannheim/tesseract/wiki")
        # We can't easily check for these on Windows, so we'll assume they're missing
        missing_deps = ["poppler", "tesseract"]
    
    return missing_deps

def install_system_dependencies(missing_deps):
    """Install missing system dependencies"""
    if not missing_deps:
        return True
    
    print_section("Installing System Dependencies")
    
    system = platform.system()
    
    if system == "Darwin":  # macOS
        if "brew" in missing_deps:
            print("Please install Homebrew manually and then run this script again")
            return False
        
        # Install missing dependencies
        for dep in missing_deps:
            print(f"Installing {dep}...")
            result = run_command(f"brew install {dep}", check=False)
            if result.returncode != 0:
                print(f"❌ Failed to install {dep}")
                return False
            print(f"✅ Installed {dep}")
    
    elif system == "Linux":
        # Determine package manager
        apt_result = run_command("which apt-get", check=False)
        dnf_result = run_command("which dnf", check=False)
        pacman_result = run_command("which pacman", check=False)
        
        if apt_result.returncode == 0:
            # Debian/Ubuntu
            print("Using apt package manager")
            
            # Map our dependency names to package names
            package_map = {
                "poppler-utils": "poppler-utils",
                "tesseract-ocr": "tesseract-ocr",
                "libmagic": "libmagic-dev"
            }
            
            # Update package lists
            run_command("sudo apt-get update", check=False)
            
            # Install packages
            for dep in missing_deps:
                pkg_name = package_map.get(dep, dep)
                print(f"Installing {pkg_name}...")
                result = run_command(f"sudo apt-get install -y {pkg_name}", check=False)
                if result.returncode != 0:
                    print(f"❌ Failed to install {pkg_name}")
                    return False
                print(f"✅ Installed {pkg_name}")
        
        elif dnf_result.returncode == 0:
            # Fedora/RHEL
            print("Using dnf package manager")
            
            # Map our dependency names to package names
            package_map = {
                "poppler-utils": "poppler-utils",
                "tesseract-ocr": "tesseract",
                "libmagic": "file-devel"
            }
            
            # Install packages
            for dep in missing_deps:
                pkg_name = package_map.get(dep, dep)
                print(f"Installing {pkg_name}...")
                result = run_command(f"sudo dnf install -y {pkg_name}", check=False)
                if result.returncode != 0:
                    print(f"❌ Failed to install {pkg_name}")
                    return False
                print(f"✅ Installed {pkg_name}")
        
        elif pacman_result.returncode == 0:
            # Arch Linux
            print("Using pacman package manager")
            
            # Map our dependency names to package names
            package_map = {
                "poppler-utils": "poppler",
                "tesseract-ocr": "tesseract",
                "libmagic": "file"
            }
            
            # Update package lists
            run_command("sudo pacman -Sy", check=False)
            
            # Install packages
            for dep in missing_deps:
                pkg_name = package_map.get(dep, dep)
                print(f"Installing {pkg_name}...")
                result = run_command(f"sudo pacman -S --noconfirm {pkg_name}", check=False)
                if result.returncode != 0:
                    print(f"❌ Failed to install {pkg_name}")
                    return False
                print(f"✅ Installed {pkg_name}")
        
        else:
            print("Unsupported Linux distribution. Please install dependencies manually:")
            for dep in missing_deps:
                print(f"- {dep}")
            return False
    
    elif system == "Windows":
        print("Please install the following dependencies manually:")
        print("- Poppler for Windows: https://github.com/oschwartz10612/poppler-windows/releases/")
        print("- Tesseract OCR: https://github.com/UB-Mannheim/tesseract/wiki")
        print("Then add them to your PATH environment variable.")
        return False
    
    return True

def setup_virtual_environment():
    """Set up a Python virtual environment"""
    print_section("Setting Up Virtual Environment")
    
    # Check if virtual environment already exists
    if os.path.exists("venv"):
        print("Virtual environment already exists")
        recreate = input("Do you want to recreate it? (y/n): ").lower().startswith('y')
        if recreate:
            print("Removing existing virtual environment...")
            if platform.system() == "Windows":
                run_command("rmdir /s /q venv", check=False)
            else:
                run_command("rm -rf venv", check=False)
        else:
            print("Using existing virtual environment")
            return True
    
    # Create virtual environment
    print("Creating virtual environment...")
    result = run_command("python -m venv venv", check=False)
    if result.returncode != 0:
        print("❌ Failed to create virtual environment")
        return False
    
    print("✅ Virtual environment created")
    return True

def install_python_dependencies():
    """Install Python dependencies in the virtual environment"""
    print_section("Installing Python Dependencies")
    
    # Determine activate command based on platform
    if platform.system() == "Windows":
        activate_cmd = "venv\\Scripts\\activate"
    else:
        activate_cmd = "source venv/bin/activate"
    
    # Upgrade pip
    print("Upgrading pip...")
    run_command(f"{activate_cmd} && python -m pip install --upgrade pip", check=False)
    
    # Install dependencies
    print("Installing MegaParse dependencies...")
    result = run_command(f"{activate_cmd} && pip install -r requirements.lock", check=False)
    if result.returncode != 0:
        print("❌ Failed to install dependencies from requirements.lock")
        # Try installing just the basic dependencies
        print("Attempting to install basic dependencies...")
        run_command(f"{activate_cmd} && pip install pypdf langchain-openai python-dotenv", check=False)
    else:
        print("✅ Installed dependencies from requirements.lock")
    
    # Install development dependencies
    print("Installing development tools...")
    run_command(f"{activate_cmd} && pip install pytest black pylint", check=False)
    
    return True

def check_api_keys():
    """Check if required API keys are set"""
    print_section("Checking API Keys")
    
    # Load .env file if it exists
    from dotenv import load_dotenv
    load_dotenv()
    
    # Check OpenAI API key
    openai_key = os.environ.get("OPENAI_API_KEY")
    if not openai_key:
        print("❌ OPENAI_API_KEY not found in environment variables")
        print("Please add your OpenAI API key to the .env file")
        
        # Create .env file if it doesn't exist
        if not os.path.exists(".env"):
            with open(".env", "w") as f:
                f.write("OPENAI_API_KEY=\n")
            print("Created .env file - please add your API key")
        
        return False
    else:
        print("✅ OPENAI_API_KEY found")
    
    return True

def test_installation():
    """Test the MegaParse installation"""
    print_section("Testing Installation")
    
    # Determine activate command based on platform
    if platform.system() == "Windows":
        activate_cmd = "venv\\Scripts\\activate"
    else:
        activate_cmd = "source venv/bin/activate"
    
    # Try importing MegaParse
    print("Testing MegaParse import...")
    result = run_command(f"{activate_cmd} && python -c \"from megaparse import MegaParse; print('MegaParse imported successfully')\"", check=False)
    
    if result.returncode != 0:
        print("❌ Failed to import MegaParse")
        print("You may need to clone and install the MegaParse repository manually:")
        print("git clone https://github.com/quivrhq/megaparse libs/megaparse")
        print(f"{activate_cmd} && cd libs/megaparse && pip install -e .")
        return False
    else:
        print("✅ MegaParse imported successfully")
    
    return True

def setup_cost_optimization():
    """Set up and test the cost optimization features"""
    print_section("Setting Up Cost Optimization")
    
    # Determine activate command based on platform
    if platform.system() == "Windows":
        activate_cmd = "venv\\Scripts\\activate"
    else:
        activate_cmd = "source venv/bin/activate"
    
    # Test cost_optimized_parser.py
    print("Testing cost-optimized parser...")
    result = run_command(f"{activate_cmd} && python -c \"from cost_optimized_parser import parse_document; print('Cost-optimized parser imported successfully')\"", check=False)
    
    if result.returncode != 0:
        print("❌ Failed to import cost-optimized parser")
    else:
        print("✅ Cost-optimized parser imported successfully")
    
    # Test early_exit_parser.py
    print("Testing early-exit parser...")
    result = run_command(f"{activate_cmd} && python -c \"from early_exit_parser import process_with_early_exit; print('Early-exit parser imported successfully')\"", check=False)
    
    if result.returncode != 0:
        print("❌ Failed to import early-exit parser")
    else:
        print("✅ Early-exit parser imported successfully")
    
    # Test batch_processor.py
    print("Testing batch processor...")
    result = run_command(f"{activate_cmd} && python -c \"import batch_processor; print('Batch processor imported successfully')\"", check=False)
    
    if result.returncode != 0:
        print("❌ Failed to import batch processor")
    else:
        print("✅ Batch processor imported successfully")
    
    return True

def create_example_command_file():
    """Create a file with example commands for using MegaParse with cost optimization"""
    print_section("Creating Example Commands")
    
    with open("example_commands.txt", "w") as f:
        f.write("# MegaParse Cost-Optimized Usage Examples\n\n")
        
        f.write("# Activate the virtual environment\n")
        if platform.system() == "Windows":
            f.write("venv\\Scripts\\activate\n\n")
        else:
            f.write("source venv/bin/activate\n\n")
        
        f.write("# Basic usage with cost optimization\n")
        f.write("python cost_optimized_parser.py path/to/your/document.pdf\n\n")
        
        f.write("# Early-exit parser (processes each page separately)\n")
        f.write("python early_exit_parser.py path/to/your/document.pdf\n\n")
        
        f.write("# Batch processing for multiple documents\n")
        f.write("python batch_processor.py path/to/document/directory --output results\n\n")
        
        f.write("# Batch processing with recursion (includes subdirectories)\n")
        f.write("python batch_processor.py path/to/document/directory --output results --recursive\n\n")
        
        f.write("# Process a document with standard parser only (no API cost)\n")
        if platform.system() == "Windows":
            f.write("python -c \"from megaparse import MegaParse; print(MegaParse().load('path/to/document.pdf'))\"\n\n")
        else:
            f.write("python -c \"from megaparse import MegaParse; print(MegaParse().load('path/to/document.pdf'))\"\n\n")
    
    print(f"Example commands saved to example_commands.txt")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Set up MegaParse with cost optimization")
    parser.add_argument("--check-only", action="store_true", help="Only check dependencies without installing")
    parser.add_argument("--quick", action="store_true", help="Quick setup without tests")
    args = parser.parse_args()
    
    print_section("MegaParse Cost-Optimized Setup")
    print("This script will set up MegaParse with cost optimization features.")
    
    # Check system dependencies
    missing_deps = check_system_dependencies()
    
    if args.check_only:
        print("\nCheck-only mode: Not installing dependencies")
        sys.exit(0)
    
    # Install system dependencies if needed
    if missing_deps:
        success = install_system_dependencies(missing_deps)
        if not success:
            print("\n❌ Failed to install all system dependencies")
            print("Please install the missing dependencies manually and run this script again")
            sys.exit(1)
    
    # Set up virtual environment
    if not setup_virtual_environment():
        print("\n❌ Failed to set up virtual environment")
        sys.exit(1)
    
    # Install Python dependencies
    if not install_python_dependencies():
        print("\n❌ Failed to install all Python dependencies")
        print("You may need to install some dependencies manually")
    
    # Check API keys
    if not check_api_keys():
        print("\n⚠️ API key check failed")
        print("Please ensure your OpenAI API key is set in the .env file")
    
    if not args.quick:
        # Test installation
        if not test_installation():
            print("\n⚠️ Installation test failed")
            print("You may need to set up MegaParse manually")
        
        # Set up cost optimization
        if not setup_cost_optimization():
            print("\n⚠️ Cost optimization setup incomplete")
    
    # Create example commands
    create_example_command_file()
    
    print_section("Setup Complete")
    print("MegaParse with cost optimization has been set up.")
    print("See example_commands.txt for usage examples.")
    
    print("\nTo use MegaParse with cost optimization:")
    print("1. Activate the virtual environment:")
    if platform.system() == "Windows":
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("2. Run the cost-optimized parser:")
    print("   python cost_optimized_parser.py path/to/your/document.pdf")

if __name__ == "__main__":
    main()
