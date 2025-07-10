.PHONY: install setup dev test clean help

# Default target
help:
	@echo "Available commands:"
	@echo "  make install  - Run the installation script to set up MegaParse"
	@echo "  make setup    - Set up virtual environment and install dependencies"
	@echo "  make dev      - Start the MegaParse API server in development mode"
	@echo "  make test     - Run a simple test to verify installation"
	@echo "  make clean    - Remove virtual environment and temporary files"

# Run the installation script
install:
	./install.sh

# Set up virtual environment and install dependencies
setup:
	python -m venv venv
	. venv/bin/activate && pip install --upgrade pip && pip install -e .
	. venv/bin/activate && pip install -r requirements.lock
	@echo "Setup complete. Activate the virtual environment with: source venv/bin/activate"

# Start the development server
dev:
	. venv/bin/activate && cd libs/megaparse && python -m megaparse.api

# Run a test to verify installation
test:
	. venv/bin/activate && python -c "from megaparse import MegaParse; print('MegaParse installed successfully')"

# Clean up virtual environment and temporary files
clean:
	rm -rf venv
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "*.egg" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	find . -type d -name "build" -exec rm -rf {} +
