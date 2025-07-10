#!/usr/bin/env python
"""
Direct Vision Parser for MegaParse

This script bypasses the standard parser and uses only the vision-based parser
with GPT-4o-mini, which is ideal for complex documents like presentations.

Usage:
    python direct_vision_parser.py path/to/your/document.pdf

The script will:
1. Skip the standard parser entirely (avoiding the logging errors)
2. Use the vision-based parser with cost-optimized model directly
3. Output the parsed content and save results
"""

import os
import sys
import json
import time
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def parse_with_vision(file_path):
    """
    Parse document using only the vision parser
    
    Args:
        file_path (str): Path to the document to parse
        
    Returns:
        dict: Results containing parsed content and metadata
    """
    start_time = time.time()
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Document not found: {file_path}")
    
    print(f"\n=== Processing document with vision parser: {os.path.basename(file_path)} ===")
    
    try:
        # Import required modules
        from megaparse.parser.megaparse_vision import MegaParseVision
        from langchain_openai import ChatOpenAI
        
        # Check if OpenAI API key is set
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        # Initialize cost-optimized vision model
        print("Initializing vision model (gpt-4o-mini)...")
        model = ChatOpenAI(
            model="gpt-4o-mini",  # Using mini version to save costs
            api_key=os.getenv("OPENAI_API_KEY"),
            max_tokens=4000  # Limiting output tokens for further cost savings
        )
        
        # Process with vision model
        print("Processing document with vision parser...")
        vision_parser = MegaParseVision(model=model)
        vision_content = vision_parser.convert(file_path)
        
        # Estimate token usage
        estimated_tokens = len(vision_content.split()) * 1.3  # Rough estimate
        
        result = {
            "file_path": file_path,
            "content": vision_content,
            "method_used": "vision_parser_with_gpt4o_mini",
            "processing_time": round(time.time() - start_time, 2),
            "api_tokens_used": int(estimated_tokens)
        }
        
        print("✅ Vision parser succeeded!")
        
        return result
        
    except Exception as e:
        print(f"❌ Vision parsing failed with error: {str(e)}")
        raise

def main():
    # Verify command line arguments
    if len(sys.argv) < 2:
        print("Usage: python direct_vision_parser.py path/to/document.pdf")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # Start timing
    start_time = time.time()
    
    try:
        # Parse with vision-based approach
        result = parse_with_vision(file_path)
        
        # Print result metrics
        print(f"\n=== Results ===")
        print(f"Method used: {result['method_used']}")
        print(f"Processing time: {result['processing_time']:.2f} seconds")
        print(f"API tokens used (estimate): {result['api_tokens_used']}")
        
        # Add cost estimate
        cost = result['api_tokens_used'] * 0.000006  # $0.006 per 1000 tokens output
        print(f"Estimated cost: ${cost:.4f}")
        
        # Print content preview
        content_preview = result["content"][:500] + "..." if len(result["content"]) > 500 else result["content"]
        print("\n=== Content Preview ===")
        print(content_preview)
        
        # Total elapsed time
        elapsed = time.time() - start_time
        print(f"\nTotal time: {elapsed:.2f} seconds")
        
        # Automatically save result
        print("\nSaving results to file...")
        output_base = Path(file_path).stem
        
        # Save content to text file
        output_file = f"{output_base}_parsed.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result["content"])
        
        # Save metadata to JSON
        metadata_file = f"{output_base}_metadata.json"
        with open(metadata_file, "w", encoding="utf-8") as f:
            # Remove content from metadata to avoid duplication
            metadata = {k: v for k, v in result.items() if k != "content"}
            json.dump(metadata, f, indent=2)
        
        print(f"Content saved to {output_file}")
        print(f"Metadata saved to {metadata_file}")
    
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
