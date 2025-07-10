# MegaParse Installation Guide

This guide will help you install MegaParse and its dependencies using the GitHub MCP Server Tools.

## Prerequisites

- Python 3.11 or higher
- Git
- System dependencies (installed automatically by the script):
  - Poppler (for PDF processing)
  - Tesseract OCR (for image text extraction)
  - libmagic (for file type detection)

## Installation Steps

1. **Clone the Repository**

   The repository has already been cloned to your local directory.

2. **Run the Installation Script**

   ```bash
   cd /Users/johnsweazey/Documents/claude-files/megaparse
   ./install.sh
   ```

   This script will:
   - Create a Python virtual environment
   - Install required system dependencies based on your OS
   - Install Python dependencies from requirements.lock
   - Clone and install MegaParse from the GitHub repository
   - Set up a .env file for your API keys

3. **Configure API Keys**

   After running the installation script, edit the `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_key_here
   LLAMA_CLOUD_API_KEY=your_llama_key_here (optional)
   MEGAPARSE_API_KEY=your_megaparse_key_here (optional)
   ```

## Testing the Installation

1. **Activate the Virtual Environment**

   ```bash
   source venv/bin/activate
   ```

2. **Run the Example Script**

   ```bash
   python example.py /path/to/your/document.pdf
   ```

   This will parse the document using MegaParse and display the extracted content.

## Troubleshooting

### Common Issues:

1. **Missing System Dependencies**
   - If the script fails to install system dependencies, you may need to install them manually.
   - For MacOS: `brew install poppler tesseract libmagic`
   - For Ubuntu/Debian: `sudo apt-get install poppler-utils tesseract-ocr libmagic-dev`

2. **Python Version**
   - MegaParse requires Python 3.11+. Verify your Python version with `python --version`.

3. **API Key Issues**
   - Ensure your API keys are correctly entered in the .env file.
   - For OpenAI, verify that your API key is active and has sufficient credits.

4. **Package Installation Failures**
   - If pip fails to install packages, try upgrading pip: `pip install --upgrade pip`
   - Some packages may require specific system libraries. Check the error message for details.

## Using MegaParse in Your Projects

After successful installation, you can use MegaParse in your projects:

```python
from megaparse import MegaParse
from langchain_openai import ChatOpenAI

# Initialize MegaParse
megaparse = MegaParse()

# Parse a document
result = megaparse.load("/path/to/document.pdf")
print(result)

# Using MegaParse Vision (for multimodal models)
from megaparse.parser.megaparse_vision import MegaParseVision
import os

model = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
parser = MegaParseVision(model=model)
vision_result = parser.convert("/path/to/document.pdf")
print(vision_result)
```

## Starting the API Server

To run MegaParse as an API server:

```bash
cd /Users/johnsweazey/Documents/claude-files/megaparse
make dev
```

Then access the API documentation at http://localhost:8000/docs
