#!/usr/bin/env python
"""
MegaParse Example Usage

This script demonstrates how to use MegaParse to parse different types of documents.
Make sure you have installed all dependencies and set up your API keys in the .env file.
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Check if API keys are set
required_keys = ["OPENAI_API_KEY"]
missing_keys = [key for key in required_keys if not os.getenv(key)]
if missing_keys:
    print(f"Error: Missing required API keys: {', '.join(missing_keys)}")
    print("Please set these in your .env file")
    sys.exit(1)

# Import MegaParse only after checking environment
try:
    from megaparse import MegaParse
    from langchain_openai import ChatOpenAI
except ImportError:
    print("Error: MegaParse package not found. Make sure you've installed it correctly.")
    print("Run: pip install -e .")
    sys.exit(1)

def main():
    # Initialize MegaParse
    print("Initializing MegaParse...")
    megaparse = MegaParse()
    
    # Get document path from command line or use default
    if len(sys.argv) > 1:
        document_path = sys.argv[1]
    else:
        print("No document path provided. Please specify a document path.")
        print("Usage: python example.py /path/to/document.pdf")
        sys.exit(1)
    
    # Check if file exists
    if not os.path.exists(document_path):
        print(f"Error: File not found: {document_path}")
        sys.exit(1)
    
    print(f"Parsing document: {document_path}")
    
    # Parse the document
    try:
        result = megaparse.load(document_path)
        print("\nParsing successful!")
        print("\n----- Document Content -----\n")
        print(result)
        print("\n---------------------------\n")
    except Exception as e:
        print(f"Error parsing document: {e}")
        sys.exit(1)
    
    # Demonstration of MegaParse Vision if preferred
    use_vision = input("Would you like to try MegaParse Vision as well? (y/n): ").lower() == 'y'
    if use_vision:
        try:
            print("\nInitializing MegaParse Vision...")
            from megaparse.parser.megaparse_vision import MegaParseVision
            
            model = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
            parser = MegaParseVision(model=model)
            
            print(f"Parsing document with Vision: {document_path}")
            vision_result = parser.convert(document_path)
            
            print("\nVision parsing successful!")
            print("\n----- Vision Document Content -----\n")
            print(vision_result)
            print("\n---------------------------\n")
        except Exception as e:
            print(f"Error using MegaParse Vision: {e}")

if __name__ == "__main__":
    main()
