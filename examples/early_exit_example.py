#!/usr/bin/env python
"""
Early-Exit Parser Example

This example demonstrates how to use the early-exit parser
to efficiently process multi-page documents, analyzing each
page individually and only using the vision parser when necessary.
"""

import os
import sys
import time
import json
from pathlib import Path

# Add parent directory to path to allow importing custom modules
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import custom parser
from custom.parsers.early_exit_parser import process_with_early_exit


def main():
    # Verify command line arguments
    if len(sys.argv) < 2:
        print("Usage: python early_exit_example.py path/to/document.pdf [complexity_threshold]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # Optional complexity threshold
    complexity_threshold = 0.5
    if len(sys.argv) > 2:
        try:
            complexity_threshold = float(sys.argv[2])
            if not 0 <= complexity_threshold <= 1:
                raise ValueError("Threshold must be between 0.0 and 1.0")
        except ValueError:
            print("Error: Complexity threshold must be a number between 0.0 and 1.0")
            sys.exit(1)
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    print(f"\n=== Processing {os.path.basename(file_path)} with Early-Exit Parser ===")
    print(f"Complexity threshold: {complexity_threshold} (higher values use standard parser more often)\n")
    
    # Start timing
    start_time = time.time()
    
    try:
        # Process document with early-exit strategy
        result = process_with_early_exit(file_path, complexity_threshold)
        
        # Print processing summary
        print("\n=== Processing Summary ===")
        print(f"Total pages: {result['total_pages']}")
        print(f"Standard parsed pages: {result['standard_parsed_pages']}")
        print(f"Vision parsed pages: {result['vision_parsed_pages']}")
        print(f"Total tokens used: {result['total_tokens_used']}")
        print(f"Processing time: {result['processing_time']:.2f} seconds")
        
        # Add cost estimate if tokens were used
        if result['total_tokens_used'] > 0:
            # Rough cost estimate at gpt-4o-mini rates
            cost = result['total_tokens_used'] * 0.000006  # $0.006 per 1000 tokens output
            print(f"Estimated cost: ${cost:.4f}")
            
            # Compare to using vision parser for everything
            full_vision_cost = result['total_pages'] * 1000 * 0.000006  # Rough estimate
            print(f"Estimated cost if using vision for all pages: ${full_vision_cost:.4f}")
            print(f"Cost saving: {(1 - cost/full_vision_cost) * 100:.1f}%")
        
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
            output_file = f"{output_base}_early_exit.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(result["content"])
            
            # Save metadata to JSON
            metadata_file = f"{output_base}_early_exit_metadata.json"
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
