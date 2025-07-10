#!/usr/bin/env python
"""
Cost-Optimized MegaParse Example

This example demonstrates how to use the cost-optimized parser
to efficiently parse documents while minimizing API costs.
"""

import os
import sys
import time
from pathlib import Path
from dotenv import load_dotenv

# Add parent directory to path to allow importing custom modules
sys.path.insert(0, str(Path(__file__).parent.parent))

# Load environment variables
load_dotenv()

# Import custom parser
from custom.parsers.cost_optimized_parser import parse_document


def main():
    # Verify command line arguments
    if len(sys.argv) < 2:
        print("Usage: python cost_optimized_example.py path/to/document.pdf")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    print(f"\n=== Processing {os.path.basename(file_path)} with Cost-Optimized Parser ===\n")
    
    # Start timing
    start_time = time.time()
    
    try:
        # Parse with cost-optimized approach
        result = parse_document(file_path)
        
        # Print result metrics
        print(f"\n=== Results ===")
        print(f"Method used: {result['method_used']}")
        print(f"Processing time: {result['processing_time']:.2f} seconds")
        print(f"API tokens used (estimate): {result['api_tokens_used']}")
        
        # Add cost estimate if tokens were used
        if result['api_tokens_used'] > 0:
            # Rough cost estimate at gpt-4o-mini rates
            cost = result['api_tokens_used'] * 0.000006  # $0.006 per 1000 tokens output
            print(f"Estimated cost: ${cost:.4f}")
        
        # Print content preview
        content_preview = result["content"][:500] + "..." if len(result["content"]) > 500 else result["content"]
        print("\n=== Content Preview ===")
        print(content_preview)
        
        # Total elapsed time
        elapsed = time.time() - start_time
        print(f"\nTotal time: {elapsed:.2f} seconds")
        
        # Optionally save result
        save_option = input("\nSave results to file? (y/n): ")
        if save_option.lower().startswith('y'):
            output_base = Path(file_path).stem
            
            # Save content to text file
            output_file = f"{output_base}_parsed.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(result["content"])
            
            # Save metadata to JSON
            import json
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
