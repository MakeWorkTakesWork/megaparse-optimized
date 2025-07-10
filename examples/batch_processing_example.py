#!/usr/bin/env python
"""
Batch Processing Example

This example demonstrates how to use the batch processor to efficiently
process multiple documents with cost optimization.
"""

import os
import sys
import argparse
from pathlib import Path

# Add parent directory to path to allow importing custom modules
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import batch processor
from custom.batch.batch_processor import process_batch, find_documents


def main():
    parser = argparse.ArgumentParser(
        description="Process multiple documents with cost-optimized MegaParse"
    )
    parser.add_argument(
        "input_path", 
        help="Path to a directory containing documents"
    )
    parser.add_argument(
        "--recursive", "-r", 
        action="store_true", 
        help="Search subdirectories recursively"
    )
    parser.add_argument(
        "--output", "-o", 
        default="results",
        help="Directory to save parsed documents"
    )
    parser.add_argument(
        "--parser", "-p", 
        choices=["auto", "standard", "cost_optimized", "early_exit"],
        default="auto",
        help="Parser type to use (default: auto)"
    )
    parser.add_argument(
        "--workers", "-w", 
        type=int,
        default=2,
        help="Maximum number of parallel workers (default: 2)"
    )
    parser.add_argument(
        "--extensions", "-e", 
        default=".pdf,.docx,.pptx",
        help="Comma-separated list of file extensions to process (default: .pdf,.docx,.pptx)"
    )
    
    args = parser.parse_args()
    
    # Process extensions
    extensions = [ext.strip() if ext.startswith('.') else f'.{ext.strip()}' 
                 for ext in args.extensions.split(',')]
    
    print(f"\n=== Batch Document Processing ===")
    print(f"Searching for documents in: {args.input_path}")
    print(f"File extensions: {', '.join(extensions)}")
    print(f"Search in subdirectories: {'Yes' if args.recursive else 'No'}")
    print(f"Parser type: {args.parser}")
    print(f"Parallel workers: {args.workers}")
    print(f"Output directory: {args.output}")
    
    # Find documents
    documents = find_documents(args.input_path, args.recursive, extensions)
    
    if not documents:
        print(f"No matching documents found in {args.input_path}")
        return
    
    print(f"\nFound {len(documents)} documents to process:")
    for i, doc in enumerate(documents[:10], 1):
        print(f"  {i}. {Path(doc).name}")
    
    if len(documents) > 10:
        print(f"  ... and {len(documents) - 10} more")
    
    # Confirm processing
    confirm = input(f"\nProcess {len(documents)} documents? (y/n): ")
    if not confirm.lower().startswith('y'):
        print("Operation canceled")
        return
    
    # Process the documents
    print(f"\nStarting batch processing...")
    
    summary = process_batch(
        documents=documents,
        parser_type=args.parser,
        max_workers=args.workers,
        output_dir=args.output
    )
    
    # Print summary
    print("\n=== Batch Processing Summary ===")
    print(f"Total documents: {summary['total_documents']}")
    print(f"Successfully processed: {summary['successful']}")
    print(f"Failed: {summary['failed']}")
    print(f"Total processing time: {summary['total_time']:.2f} seconds")
    print(f"Average time per document: {summary['average_time_per_document']:.2f} seconds")
    print(f"Total tokens used: {summary['total_tokens']}")
    print(f"Estimated cost: ${summary['estimated_cost']:.4f}")
    
    # Print results location
    print(f"\nResults saved to: {os.path.abspath(args.output)}")
    print(f"Summary report: {os.path.join(os.path.abspath(args.output), 'batch_summary.json')}")


if __name__ == "__main__":
    main()
