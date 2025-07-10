#!/usr/bin/env python
"""
Cost-Optimized MegaParse Implementation

This script demonstrates how to implement a tiered approach to document parsing
that minimizes API token costs while maintaining high-quality results.

Usage:
    python cost_optimized_parser.py path/to/your/document.pdf

The script will:
1. First try the standard parser (zero API cost)
2. If needed, fall back to a vision-based parser with cost-optimized model
3. Output the parsed content and report which method was used
"""

import os
import sys
import json
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

# Define a function to check if the parsed content seems sufficient
def is_quality_sufficient(content, min_characters=100, min_words=20):
    """
    Check if the parsed content meets minimum quality standards.
    
    Args:
        content (str): The parsed content to evaluate
        min_characters (int): Minimum number of characters required
        min_words (int): Minimum number of words required
        
    Returns:
        bool: True if content seems to have sufficient quality
    """
    # Basic quality checks
    if not content or len(content) < min_characters:
        print(f"Content too short: {len(content) if content else 0} characters")
        return False
        
    word_count = len(content.split())
    if word_count < min_words:
        print(f"Too few words detected: {word_count} words")
        return False
        
    # Check if content has mostly garbage or extraction errors
    error_indicators = [
        "failed to extract", 
        "cannot parse", 
        "error processing",
        "[?]" * 5  # Multiple unknown character markers often indicate OCR failure
    ]
    
    for indicator in error_indicators:
        if indicator in content.lower():
            print(f"Found error indicator: '{indicator}'")
            return False
    
    # Additional check: Does it have some structure? (paragraphs, etc.)
    if "\n" not in content and len(content) > 500:
        print("Content lacks structure (no paragraphs found)")
        return False
        
    return True

def parse_document(file_path, quality_threshold=0.7):
    """
    Parse a document using a tiered approach to minimize costs.
    
    Args:
        file_path (str): Path to the document to parse
        quality_threshold (float): Threshold for determining if standard parsing is sufficient
        
    Returns:
        dict: Results containing parsed content and metadata about which method was used
    """
    start_time = time.time()
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Document not found: {file_path}")
    
    print(f"\n=== Processing document: {os.path.basename(file_path)} ===")
    
    result = {
        "file_path": file_path,
        "content": "",
        "method_used": "",
        "processing_time": 0,
        "quality_sufficient": False,
        "api_tokens_used": 0
    }
    
    # TIER 1: Try standard parser first (no API cost)
    try:
        print("Trying standard parser (no API cost)...")
        
        # Import MegaParse here to avoid errors if not installed
        from megaparse import MegaParse
        
        standard_parser = MegaParse()
        parsed_content = standard_parser.load(file_path)
        
        # Check quality of the standard parser results
        result["content"] = parsed_content
        result["quality_sufficient"] = is_quality_sufficient(parsed_content)
        
        if result["quality_sufficient"]:
            result["method_used"] = "standard_parser"
            print("✅ Standard parser succeeded with sufficient quality!")
        else:
            print("⚠️ Standard parser output deemed insufficient quality, will try vision parser...")
            # We'll continue to the vision parser
    
    except Exception as e:
        print(f"⚠️ Standard parsing failed with error: {str(e)}")
        # We'll continue to the vision parser
    
    # TIER 2: Only use vision parser if standard parser failed or produced low-quality results
    if not result.get("quality_sufficient"):
        try:
            print("Falling back to vision-based parsing with cost-optimized model...")
            
            # Import required modules
            from megaparse.parser.megaparse_vision import MegaParseVision
            from langchain_openai import ChatOpenAI
            
            # Check if OpenAI API key is set
            if not os.getenv("OPENAI_API_KEY"):
                raise ValueError("OPENAI_API_KEY not found in environment variables")
            
            # Initialize cost-optimized vision model (gpt-4o-mini is ~8x cheaper than gpt-4o)
            model = ChatOpenAI(
                model="gpt-4o-mini",  # Using mini version to save costs
                api_key=os.getenv("OPENAI_API_KEY"),
                max_tokens=4000  # Limiting output tokens for further cost savings
            )
            
            # Process with vision model
            vision_parser = MegaParseVision(model=model)
            vision_content = vision_parser.convert(file_path)
            
            # Note: In a production system, you would implement token counting
            # For now, we're making a rough estimate
            estimated_tokens = len(vision_content.split()) * 1.3  # Rough estimate
            
            result["content"] = vision_content
            result["method_used"] = "vision_parser_with_gpt4o_mini"
            result["api_tokens_used"] = int(estimated_tokens)
            result["quality_sufficient"] = True
            print("✅ Vision parser succeeded!")
            
        except Exception as e:
            print(f"❌ Vision parsing failed with error: {str(e)}")
            if result["content"]:
                print("Using standard parser results as fallback despite quality concerns")
                result["method_used"] = "standard_parser_fallback"
            else:
                raise Exception(f"Both standard and vision parsing failed: {str(e)}")
    
    # Calculate processing time
    result["processing_time"] = round(time.time() - start_time, 2)
    
    # Print summary
    print("\n=== Parsing Summary ===")
    print(f"Method used: {result['method_used']}")
    print(f"Processing time: {result['processing_time']} seconds")
    print(f"API tokens used (estimate): {result['api_tokens_used']}")
    
    # In a production system, you might want to log these metrics
    
    return result

def main():
    """Main function that handles command line arguments and runs the parser"""
    if len(sys.argv) < 2:
        print("Usage: python cost_optimized_parser.py path/to/document.pdf")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    try:
        result = parse_document(file_path)
        
        # Preview the first 500 characters of the content
        content_preview = result["content"][:500] + "..." if len(result["content"]) > 500 else result["content"]
        print("\n=== Content Preview ===")
        print(content_preview)
        
        # Auto-save the results instead of asking
        # Get the original filename without extension
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
