#!/usr/bin/env python
"""
Batch Document Processor

This module provides functionality for batch processing multiple documents
with MegaParse, using parallel processing and tracking costs.
"""

import os
import sys
import time
import json
import argparse
import logging
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import List, Dict, Any, Optional, Tuple, Callable

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("batch_processing.log")
    ]
)
logger = logging.getLogger("batch_processor")

# Add parent directory to path to allow importing custom modules
parent_dir = str(Path(__file__).parent.parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import custom parsers
from custom.parsers.cost_optimized_parser import parse_document
from custom.parsers.early_exit_parser import process_with_early_exit
from custom.utils.cost_tracker import CostTracker, estimate_token_usage
from custom.utils.complexity_analyzer import calculate_document_complexity


# Define supported file extensions
SUPPORTED_EXTENSIONS = [
    '.pdf', '.docx', '.doc', '.pptx', '.ppt', 
    '.xlsx', '.xls', '.txt', '.rtf', '.csv'
]


def is_supported_file(file_path: str) -> bool:
    """Check if a file is supported by MegaParse."""
    return Path(file_path).suffix.lower() in SUPPORTED_EXTENSIONS


def find_documents(
    directory: str, 
    recursive: bool = False,
    include_exts: Optional[List[str]] = None
) -> List[str]:
    """
    Find all supported documents in a directory.
    
    Args:
        directory (str): Directory to search
        recursive (bool): Whether to search subdirectories
        include_exts (List[str], optional): File extensions to include
        
    Returns:
        List[str]: List of document paths
    """
    if include_exts is None:
        include_exts = SUPPORTED_EXTENSIONS
    
    documents = []
    search_dir = Path(directory)
    
    if not search_dir.exists():
        logger.error(f"Directory not found: {directory}")
        return []
    
    if recursive:
        # Search all subdirectories
        for root, _, files in os.walk(search_dir):
            for file in files:
                file_path = Path(root) / file
                if file_path.suffix.lower() in include_exts:
                    documents.append(str(file_path))
    else:
        # Search only the specified directory
        for file in search_dir.iterdir():
            if file.is_file() and file.suffix.lower() in include_exts:
                documents.append(str(file))
    
    return documents


def process_document(
    file_path: str,
    parser_type: str = 'auto',
    complexity_threshold: float = 0.5,
    output_dir: Optional[str] = None
) -> Dict[str, Any]:
    """
    Process a single document with the specified parser.
    
    Args:
        file_path (str): Path to the document
        parser_type (str): Type of parser to use ('auto', 'standard', 'cost_optimized', 'early_exit')
        complexity_threshold (float): Threshold for early exit parser
        output_dir (str, optional): Directory to save output files
        
    Returns:
        Dict: Processing result
    """
    try:
        logger.info(f"Processing {file_path} with {parser_type} parser")
        
        start_time = time.time()
        
        # Determine which parser to use
        if parser_type == 'auto':
            # If auto, analyze the document to determine the best parser
            best_parser = determine_best_parser(file_path)
            logger.info(f"Auto-selected parser: {best_parser}")
            parser_type = best_parser
        
        # Process with the selected parser
        if parser_type == 'standard':
            from megaparse import MegaParse
            parser = MegaParse()
            content = parser.load(file_path)
            result = {
                "file_path": file_path,
                "content": content,
                "method_used": "standard",
                "processing_time": time.time() - start_time,
                "api_tokens_used": 0
            }
        elif parser_type == 'cost_optimized':
            result = parse_document(file_path)
        elif parser_type == 'early_exit':
            result = process_with_early_exit(file_path, complexity_threshold)
        else:
            raise ValueError(f"Unknown parser type: {parser_type}")
        
        # Save results if output directory is specified
        if output_dir:
            output_path = save_results(file_path, result, output_dir)
            result["output_path"] = output_path
        
        result["processing_time"] = time.time() - start_time
        
        logger.info(f"Completed processing {file_path} in {result['processing_time']:.2f}s")
        return result
    
    except Exception as e:
        logger.error(f"Error processing {file_path}: {str(e)}")
        return {
            "file_path": file_path,
            "error": str(e),
            "method_used": parser_type,
            "processing_time": time.time() - start_time,
            "success": False
        }


def determine_best_parser(file_path: str) -> str:
    """
    Analyze a document to determine the best parser to use.
    
    Args:
        file_path (str): Path to the document
        
    Returns:
        str: Recommended parser type
    """
    # For PDFs, we can do detailed analysis
    if file_path.lower().endswith('.pdf'):
        try:
            import pypdf
            
            # Extract text from first few pages
            pages = []
            with open(file_path, 'rb') as file:
                pdf = pypdf.PdfReader(file)
                num_pages = len(pdf.pages)
                
                # Only analyze up to 5 pages for efficiency
                pages_to_analyze = min(num_pages, 5)
                
                for i in range(pages_to_analyze):
                    try:
                        text = pdf.pages[i].extract_text() or ""
                        pages.append({
                            "page_number": i + 1,
                            "content": text
                        })
                    except Exception:
                        # If extraction fails, assume complex page
                        pages.append({
                            "page_number": i + 1,
                            "content": "",
                            "complexity": 1.0
                        })
            
            # Calculate document complexity
            complexity_data = calculate_document_complexity(pages)
            
            # Return recommended parser
            return complexity_data["recommended_parser"]
        
        except Exception:
            # If analysis fails, default to cost_optimized
            return "cost_optimized"
    
    # For small text files, use standard parser
    elif file_path.lower().endswith('.txt'):
        try:
            file_size = os.path.getsize(file_path)
            if file_size < 10000:  # Less than 10KB
                return "standard"
        except Exception:
            pass
    
    # Default to cost_optimized for other file types
    return "cost_optimized"


def save_results(file_path: str, result: Dict[str, Any], output_dir: str) -> str:
    """
    Save processing results to output directory.
    
    Args:
        file_path (str): Original document path
        result (Dict): Processing result
        output_dir (str): Directory to save output files
        
    Returns:
        str: Path to saved content file
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get base filename without extension
    base_name = Path(file_path).stem
    
    # Save content to text file
    content_file = Path(output_dir) / f"{base_name}_parsed.txt"
    with open(content_file, "w", encoding="utf-8") as f:
        f.write(result["content"])
    
    # Save metadata to JSON
    metadata_file = Path(output_dir) / f"{base_name}_metadata.json"
    with open(metadata_file, "w", encoding="utf-8") as f:
        # Remove content from metadata to avoid duplication
        metadata = {k: v for k, v in result.items() if k != "content"}
        json.dump(metadata, f, indent=2)
    
    return str(content_file)


def process_batch(
    documents: List[str],
    parser_type: str = 'auto',
    max_workers: int = 2,
    complexity_threshold: float = 0.5,
    output_dir: Optional[str] = None
) -> Dict[str, Any]:
    """
    Process a batch of documents in parallel.
    
    Args:
        documents (List[str]): List of document paths
        parser_type (str): Type of parser to use
        max_workers (int): Maximum number of parallel workers
        complexity_threshold (float): Threshold for early exit parser
        output_dir (str, optional): Directory to save output files
        
    Returns:
        Dict: Batch processing summary
    """
    if not documents:
        return {
            "success": False,
            "error": "No documents to process",
            "total_documents": 0,
            "successful": 0,
            "failed": 0,
            "total_time": 0,
            "results": []
        }
    
    # Create output directory if specified
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    start_time = time.time()
    results = []
    successful = 0
    failed = 0
    total_tokens = 0
    
    # Process documents in parallel
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_path = {
            executor.submit(
                process_document, 
                doc,
                parser_type, 
                complexity_threshold,
                output_dir
            ): doc for doc in documents
        }
        
        # Process results as they complete
        for future in as_completed(future_to_path):
            doc_path = future_to_path[future]
            try:
                result = future.result()
                results.append(result)
                
                if "error" in result and result.get("success", True) is False:
                    failed += 1
                    logger.error(f"Failed to process {doc_path}: {result['error']}")
                else:
                    successful += 1
                    if "api_tokens_used" in result:
                        total_tokens += result["api_tokens_used"]
                    
                    logger.info(f"Successfully processed {doc_path}")
            
            except Exception as e:
                failed += 1
                logger.error(f"Exception processing {doc_path}: {str(e)}")
                results.append({
                    "file_path": doc_path,
                    "error": str(e),
                    "success": False
                })
    
    # Calculate summary statistics
    total_time = time.time() - start_time
    
    # Estimate cost
    # Average cost of $0.006 per 1000 tokens (gpt-4o-mini output rate)
    estimated_cost = (total_tokens / 1000) * 0.006
    
    # Create summary
    summary = {
        "success": True,
        "total_documents": len(documents),
        "successful": successful,
        "failed": failed,
        "total_time": total_time,
        "average_time_per_document": total_time / max(len(documents), 1),
        "total_tokens": total_tokens,
        "estimated_cost": estimated_cost,
        "parser_type": parser_type,
        "complexity_threshold": complexity_threshold,
        "results": results
    }
    
    # Save summary if output directory is specified
    if output_dir:
        summary_file = Path(output_dir) / "batch_summary.json"
        with open(summary_file, "w", encoding="utf-8") as f:
            # Create a copy without the full results to avoid huge files
            summary_copy = {k: v for k, v in summary.items() if k != "results"}
            # Add simplified results
            summary_copy["results"] = [
                {
                    "file_path": r["file_path"],
                    "success": "error" not in r,
                    "method_used": r.get("method_used", "unknown"),
                    "processing_time": r.get("processing_time", 0),
                    "tokens_used": r.get("api_tokens_used", 0)
                }
                for r in results
            ]
            json.dump(summary_copy, f, indent=2)
        
        logger.info(f"Batch summary saved to {summary_file}")
    
    return summary


def main():
    """Command-line interface for the batch processor."""
    parser = argparse.ArgumentParser(
        description="Process multiple documents with MegaParse"
    )
    parser.add_argument(
        "input_path", 
        help="Path to a document or directory containing documents"
    )
    parser.add_argument(
        "--recursive", "-r", 
        action="store_true", 
        help="Search subdirectories recursively"
    )
    parser.add_argument(
        "--output", "-o", 
        help="Directory to save parsed documents"
    )
    parser.add_argument(
        "--parser", "-p", 
        choices=["auto", "standard", "cost_optimized", "early_exit"],
        default="auto",
        help="Parser type to use"
    )
    parser.add_argument(
        "--complexity", "-c", 
        type=float,
        default=0.5,
        help="Complexity threshold for early exit parser (0.0-1.0)"
    )
    parser.add_argument(
        "--max-workers", "-w", 
        type=int,
        default=2,
        help="Maximum number of parallel workers"
    )
    parser.add_argument(
        "--extensions", "-e", 
        help="Comma-separated list of file extensions to process (e.g., .pdf,.docx)"
    )
    
    args = parser.parse_args()
    
    # Process extensions if provided
    if args.extensions:
        extensions = [ext.strip() if ext.startswith('.') else f'.{ext.strip()}' 
                     for ext in args.extensions.split(',')]
    else:
        extensions = SUPPORTED_EXTENSIONS
    
    # Find documents to process
    input_path = args.input_path
    if os.path.isdir(input_path):
        logger.info(f"Searching for documents in {input_path}")
        documents = find_documents(input_path, args.recursive, extensions)
        logger.info(f"Found {len(documents)} documents to process")
    elif os.path.isfile(input_path):
        if Path(input_path).suffix.lower() in extensions:
            documents = [input_path]
            logger.info(f"Processing single file: {input_path}")
        else:
            logger.error(f"Unsupported file type: {input_path}")
            sys.exit(1)
    else:
        logger.error(f"Input path not found: {input_path}")
        sys.exit(1)
    
    if not documents:
        logger.error(f"No supported documents found in {input_path}")
        sys.exit(1)
    
    # Process the documents
    try:
        logger.info(f"Starting batch processing with {args.max_workers} workers")
        summary = process_batch(
            documents=documents,
            parser_type=args.parser,
            max_workers=args.max_workers,
            complexity_threshold=args.complexity,
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
        
        if args.output:
            print(f"\nResults saved to {args.output}")
            print(f"Summary report: {Path(args.output) / 'batch_summary.json'}")
    
    except Exception as e:
        logger.error(f"Error during batch processing: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
