#!/usr/bin/env python
"""
Main CLI entrypoint for MegaParse Optimized

This module provides the main command line interface for the
cost-optimized MegaParse extensions.
"""

import os
import sys
import argparse
import logging
from pathlib import Path
from typing import List, Optional

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("megaparse-optimized")


def main():
    """Main entry point for the MegaParse Optimized CLI."""
    parser = argparse.ArgumentParser(
        description="MegaParse Optimized - Cost-efficient document parsing"
    )
    
    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # "parse" command
    parse_parser = subparsers.add_parser(
        "parse", help="Parse a single document"
    )
    parse_parser.add_argument(
        "file_path", help="Path to the document to parse"
    )
    parse_parser.add_argument(
        "--method", "-m",
        choices=["auto", "standard", "cost_optimized", "early_exit"],
        default="auto",
        help="Parsing method to use (default: auto)"
    )
    parse_parser.add_argument(
        "--output", "-o",
        help="Path to save the parsed content (default: print to console)"
    )
    parse_parser.add_argument(
        "--complexity", "-c",
        type=float,
        default=0.5,
        help="Complexity threshold for early exit parser (0.0-1.0, default: 0.5)"
    )
    
    # "batch" command
    batch_parser = subparsers.add_parser(
        "batch", help="Process multiple documents in batch"
    )
    batch_parser.add_argument(
        "input_path", help="Path to directory containing documents"
    )
    batch_parser.add_argument(
        "--recursive", "-r",
        action="store_true",
        help="Search subdirectories recursively"
    )
    batch_parser.add_argument(
        "--output", "-o",
        default="results",
        help="Directory to save parsed documents (default: ./results)"
    )
    batch_parser.add_argument(
        "--method", "-m",
        choices=["auto", "standard", "cost_optimized", "early_exit"],
        default="auto",
        help="Parsing method to use (default: auto)"
    )
    batch_parser.add_argument(
        "--workers", "-w",
        type=int,
        default=2,
        help="Maximum number of parallel workers (default: 2)"
    )
    batch_parser.add_argument(
        "--extensions", "-e",
        default=".pdf,.docx,.pptx",
        help="Comma-separated list of file extensions to process (default: .pdf,.docx,.pptx)"
    )
    
    # "analyze" command
    analyze_parser = subparsers.add_parser(
        "analyze", help="Analyze a document's complexity without parsing"
    )
    analyze_parser.add_argument(
        "file_path", help="Path to the document to analyze"
    )
    
    # "cost" command
    cost_parser = subparsers.add_parser(
        "cost", help="View cost summary information"
    )
    cost_parser.add_argument(
        "--days", "-d",
        type=int,
        default=30,
        help="Number of days to include in the summary (default: 30)"
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # If no command specified, print help
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Handle different commands
    if args.command == "parse":
        cmd_parse(args.file_path, args.method, args.output, args.complexity)
    elif args.command == "batch":
        cmd_batch(args.input_path, args.recursive, args.output, 
                 args.method, args.workers, args.extensions)
    elif args.command == "analyze":
        cmd_analyze(args.file_path)
    elif args.command == "cost":
        cmd_cost(args.days)


def cmd_parse(file_path: str, method: str, output: Optional[str], complexity: float):
    """Handle the 'parse' command."""
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        sys.exit(1)
    
    try:
        # Import here to avoid circular imports
        if method == "standard":
            from megaparse import MegaParse
            parser = MegaParse()
            result = {"content": parser.load(file_path), "method_used": "standard"}
        elif method == "cost_optimized" or method == "auto":
            from custom.parsers.cost_optimized_parser import parse_document
            result = parse_document(file_path)
        elif method == "early_exit":
            from custom.parsers.early_exit_parser import process_with_early_exit
            result = process_with_early_exit(file_path, complexity)
        else:
            logger.error(f"Unknown parsing method: {method}")
            sys.exit(1)
        
        # Handle output
        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(result["content"])
            logger.info(f"Parsed content saved to {output}")
            
            # Also save metadata
            import json
            metadata_file = f"{Path(output).stem}_metadata.json"
            with open(metadata_file, "w", encoding="utf-8") as f:
                metadata = {k: v for k, v in result.items() if k != "content"}
                json.dump(metadata, f, indent=2)
            logger.info(f"Metadata saved to {metadata_file}")
        else:
            # Print to console
            print("\n=== Parsing Results ===")
            print(f"Method used: {result['method_used']}")
            if "api_tokens_used" in result:
                print(f"API tokens used: {result['api_tokens_used']}")
                if result['api_tokens_used'] > 0:
                    cost = result['api_tokens_used'] * 0.000006  # $0.006 per 1000 tokens
                    print(f"Estimated cost: ${cost:.4f}")
            
            print("\n=== Document Content ===\n")
            print(result["content"])
    
    except Exception as e:
        logger.error(f"Error parsing document: {str(e)}")
        sys.exit(1)


def cmd_batch(input_path: str, recursive: bool, output: str, 
             method: str, workers: int, extensions: str):
    """Handle the 'batch' command."""
    try:
        # Import here to avoid circular imports
        from custom.batch.batch_processor import process_batch, find_documents
        
        # Process extensions
        ext_list = [ext.strip() if ext.startswith('.') else f'.{ext.strip()}' 
                   for ext in extensions.split(',')]
        
        # Find documents
        documents = find_documents(input_path, recursive, ext_list)
        
        if not documents:
            logger.error(f"No matching documents found in {input_path}")
            sys.exit(1)
        
        logger.info(f"Found {len(documents)} documents to process")
        
        # Process documents
        summary = process_batch(
            documents=documents,
            parser_type=method,
            max_workers=workers,
            output_dir=output
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
        
        print(f"\nResults saved to: {os.path.abspath(output)}")
    
    except Exception as e:
        logger.error(f"Error during batch processing: {str(e)}")
        sys.exit(1)


def cmd_analyze(file_path: str):
    """Handle the 'analyze' command."""
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        sys.exit(1)
    
    try:
        # Import analysis utilities
        from custom.utils.complexity_analyzer import calculate_document_complexity
        
        print(f"\n=== Analyzing Document: {file_path} ===\n")
        
        # For PDFs, we can do more detailed analysis
        if file_path.lower().endswith('.pdf'):
            import pypdf
            
            # Extract text from pages
            pages = []
            with open(file_path, 'rb') as file:
                pdf = pypdf.PdfReader(file)
                num_pages = len(pdf.pages)
                
                print(f"Document has {num_pages} pages")
                
                for i in range(num_pages):
                    try:
                        text = pdf.pages[i].extract_text() or ""
                        pages.append({
                            "page_number": i + 1,
                            "content": text
                        })
                    except Exception as e:
                        print(f"Error extracting text from page {i+1}: {e}")
                        pages.append({
                            "page_number": i + 1,
                            "content": "",
                            "complexity": 1.0
                        })
            
            # Calculate document complexity
            complexity_data = calculate_document_complexity(pages)
            
            # Show page-by-page complexity
            print("\nPage-by-Page Complexity:")
            for page in pages:
                if "complexity" not in page:
                    from custom.utils.complexity_analyzer import analyze_page_complexity
                    page["complexity"] = analyze_page_complexity(page["content"])
                
                complexity = page["complexity"]
                rating = "Simple" if complexity < 0.3 else "Moderate" if complexity < 0.7 else "Complex"
                print(f"  Page {page['page_number']}: {complexity:.2f} - {rating}")
            
            # Show overall document stats
            print(f"\nAverage complexity: {complexity_data['avg_complexity']:.2f}")
            print(f"Maximum complexity: {complexity_data['max_complexity']:.2f}")
            print(f"Complex pages: {complexity_data['complex_pages']} of {complexity_data['total_pages']}")
            print(f"Complex page ratio: {complexity_data['complex_page_ratio']:.1%}")
            print(f"Recommended parser: {complexity_data['recommended_parser']}")
            
            # Cost estimation
            if complexity_data['recommended_parser'] == 'standard':
                print("\nEstimated API cost: $0.00 (standard parser sufficient)")
            elif complexity_data['recommended_parser'] == 'early_exit':
                complex_pages = complexity_data['complex_pages']
                cost = complex_pages * 0.01  # Rough estimate: $0.01 per complex page
                print(f"\nEstimated API cost: ${cost:.2f} (early-exit parser recommended)")
                print(f"Estimated cost if using vision for all pages: ${complexity_data['total_pages'] * 0.01:.2f}")
                print(f"Potential cost saving: ${(complexity_data['total_pages'] - complex_pages) * 0.01:.2f}")
            else:
                cost = complexity_data['total_pages'] * 0.01  # Rough estimate: $0.01 per page
                print(f"\nEstimated API cost: ${cost:.2f} (vision parser recommended)")
        
        else:
            # For non-PDF files, do basic analysis
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                try:
                    content = f.read()
                except Exception:
                    logger.error("Failed to read file content")
                    content = ""
            
            from custom.utils.complexity_analyzer import analyze_page_complexity
            complexity = analyze_page_complexity(content)
            
            rating = "Simple" if complexity < 0.3 else "Moderate" if complexity < 0.7 else "Complex"
            print(f"Document complexity: {complexity:.2f} - {rating}")
            
            if complexity < 0.3:
                print("Recommended parser: standard (no API cost)")
            elif complexity < 0.7:
                print("Recommended parser: cost_optimized (moderate API cost)")
            else:
                print("Recommended parser: vision (higher API cost)")
    
    except Exception as e:
        logger.error(f"Error analyzing document: {str(e)}")
        sys.exit(1)


def cmd_cost(days: int):
    """Handle the 'cost' command."""
    try:
        # Import cost tracker
        from custom.utils.cost_tracker import CostTracker
        
        tracker = CostTracker()
        summary = tracker.get_summary(days)
        
        if not summary.get("total_cost"):
            print(f"\nNo cost data found for the last {days} days.")
            return
        
        print(f"\n=== Cost Summary (Last {days} days) ===")
        print(f"Total API cost: ${summary['total_cost']:.2f}")
        print(f"Total tokens used: {summary['total_tokens']}")
        print(f"Documents processed: {summary['file_count']}")
        print(f"Average cost per document: ${summary['average_cost_per_file']:.4f}")
        
        # Print cost by model
        if summary.get("model_costs"):
            print("\nCost by Model:")
            for model, cost in summary["model_costs"].items():
                print(f"  {model}: ${cost:.2f}")
        
        # Print cost by parser type
        if summary.get("parser_costs"):
            print("\nCost by Parser Type:")
            for parser, cost in summary["parser_costs"].items():
                print(f"  {parser}: ${cost:.2f}")
        
        # Date range
        start = summary.get("date_range", {}).get("start")
        end = summary.get("date_range", {}).get("end")
        if start and end:
            print(f"\nDate range: {start} to {end}")
    
    except Exception as e:
        logger.error(f"Error retrieving cost data: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
