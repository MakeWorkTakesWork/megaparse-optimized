#!/usr/bin/env python3
"""
Simple PDF Parser

This script provides a simple way to parse PDF files and extract their content.
It uses PyPDF for text extraction and saves the output to a text file.

Usage:
    python simple_pdf_parser.py path/to/your/document.pdf
"""

import os
import sys
import json
import time
from pathlib import Path

def parse_pdf(file_path):
    """
    Parse a PDF document and extract its text content.
    
    Args:
        file_path (str): Path to the PDF document
        
    Returns:
        dict: Results containing parsed content and metadata
    """
    start_time = time.time()
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Document not found: {file_path}")
    
    print(f"\n=== Processing document: {os.path.basename(file_path)} ===")
    
    result = {
        "file_path": file_path,
        "content": "",
        "processing_time": 0,
    }
    
    try:
        # Import PyPDF
        import pypdf
        
        # Open the PDF file
        print("Parsing PDF with PyPDF...")
        text_content = []
        
        with open(file_path, 'rb') as file:
            pdf = pypdf.PdfReader(file)
            
            # Get the number of pages
            num_pages = len(pdf.pages)
            print(f"PDF has {num_pages} pages")
            
            # Extract text from each page
            for i in range(num_pages):
                page = pdf.pages[i]
                text = page.extract_text()
                text_content.append(text)
            
            # Join all the text
            result["content"] = "\n\n".join(text_content)
            
    except Exception as e:
        print(f"Error parsing PDF: {str(e)}")
        raise
    
    # Calculate processing time
    result["processing_time"] = round(time.time() - start_time, 2)
    
    # Print summary
    print("\n=== Parsing Summary ===")
    print(f"Processing time: {result['processing_time']} seconds")
    
    return result

def main():
    """Main function that handles command line arguments and runs the parser"""
    if len(sys.argv) < 2:
        print("Usage: python simple_pdf_parser.py path/to/document.pdf")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    try:
        result = parse_pdf(file_path)
        
        # Preview the first 500 characters of the content
        content_preview = result["content"][:500] + "..." if len(result["content"]) > 500 else result["content"]
        print("\n=== Content Preview ===")
        print(content_preview)
        
        # Save the results
        file_base = os.path.splitext(os.path.basename(file_path))[0]
        output_path = f"{file_base}_parsed.txt"
        
        # Save content to text file
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(result["content"])
        
        # Save metadata to JSON
        metadata = {k: v for k, v in result.items() if k != "content"}
        with open(f"{file_base}_metadata.json", "w", encoding="utf-8") as f:
            json.dump(metadata, f, indent=2)
        
        print(f"Content saved to {output_path}")
        print(f"Metadata saved to {file_base}_metadata.json")
    
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
