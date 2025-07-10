#!/usr/bin/env python
"""
Early-Exit Parser Module

This module extends our cost-optimization strategy by implementing early exit for text-based pages.
It analyzes individual pages of a document to determine if they:
1. Are mostly text (use standard parser only)
2. Are complex/visual (require vision parser)

This approach further reduces API costs by only using vision models on pages that need them.
"""

import os
import sys
import json
import tempfile
import time
from pathlib import Path
from typing import List, Dict, Any, Tuple, Optional
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("early_exit_parser")

def analyze_page_complexity(page_content: str) -> float:
    """
    Analyze a page's content to determine its text vs. visual complexity
    
    Returns a score from 0.0 to 1.0, where:
    - 0.0 means highly textual (standard parser sufficient)
    - 1.0 means highly visual (vision parser needed)
    """
    # Basic heuristics for determining if a page is primarily text
    
    # 1. Check if we have a reasonable amount of text
    if not page_content or len(page_content) < 50:
        # Empty or very short content often means the page is visual or the parser failed
        return 0.9
    
    # 2. Check text-to-special-character ratio (tables often have many special characters)
    alpha_chars = sum(1 for c in page_content if c.isalnum() or c.isspace())
    total_chars = len(page_content)
    alpha_ratio = alpha_chars / max(total_chars, 1)
    
    # 3. Check for table indicators
    table_indicators = ["table", "column", "row", "|", "+--", "+--+", "----+"]
    has_table_indicators = any(indicator in page_content for indicator in table_indicators)
    
    # 4. Check for bullet points and formatting
    bullet_indicators = ["•", "○", "●", "■", "□", "◆", "◇", "▪", "▫", "►", "▻"]
    has_bullets = any(indicator in page_content for indicator in bullet_indicators)
    
    # 5. Check for image placeholders or captions
    image_indicators = ["[image]", "[figure]", "fig.", "figure", "image:", "photo:"]
    has_image_indicators = any(indicator in page_content.lower() for indicator in image_indicators)
    
    # Calculate complexity score - higher means more likely to need vision model
    complexity_score = 0.0
    
    # Low text ratio suggests images, diagrams, etc.
    if alpha_ratio < 0.7:
        complexity_score += 0.4
    
    # Tables benefit from vision models
    if has_table_indicators:
        complexity_score += 0.3
    
    # Bullet points might need formatting preservation
    if has_bullets:
        complexity_score += 0.1
    
    # Explicit image references suggest visual content
    if has_image_indicators:
        complexity_score += 0.3
    
    # Cap at 1.0
    return min(complexity_score, 1.0)

def split_document_by_page(file_path: str) -> List[Dict[str, Any]]:
    """
    Split a document into pages for individual analysis.
    This is a basic implementation - in production, you'd use a more robust splitter.
    
    Returns a list of page data with page number and extracted text.
    """
    try:
        # For PDF files, we'll use PyPDF or similar
        if file_path.lower().endswith('.pdf'):
            # This is a simplified version - in production, use a proper PDF parser
            import pypdf
            
            pages = []
            with open(file_path, 'rb') as file:
                pdf = pypdf.PdfReader(file)
                for i, page in enumerate(pdf.pages):
                    try:
                        text = page.extract_text() or ""
                        pages.append({
                            "page_number": i + 1,
                            "content": text,
                            "complexity": analyze_page_complexity(text)
                        })
                    except Exception as e:
                        logger.warning(f"Error extracting text from page {i+1}: {e}")
                        # If extraction fails, mark as complex (will use vision)
                        pages.append({
                            "page_number": i + 1,
                            "content": "",
                            "complexity": 1.0  # High complexity - use vision
                        })
            return pages
            
        # For other document types, we'll return a single "page"
        # In production, you'd implement proper splitting for each document type
        else:
            from cost_optimized_parser import parse_document
            
            # Parse with standard parser first
            result = parse_document(file_path)
            content = result.get("content", "")
            
            return [{
                "page_number": 1,
                "content": content,
                "complexity": analyze_page_complexity(content)
            }]
            
    except Exception as e:
        logger.error(f"Failed to split document {file_path}: {e}")
        # Return a placeholder that will trigger vision parsing
        return [{
            "page_number": 1,
            "content": "",
            "complexity": 1.0
        }]

def process_with_early_exit(file_path: str, complexity_threshold: float = 0.5) -> Dict[str, Any]:
    """
    Process a document with early exit strategy - only use vision parser on complex pages
    
    Args:
        file_path: Path to the document
        complexity_threshold: Threshold above which vision parser is used (0.0-1.0)
        
    Returns:
        Dict containing parsed content and metadata
    """
    start_time = time.time()
    
    # Import here to avoid circular imports
    from cost_optimized_parser import parse_document
    
    # Initialize result structure
    result = {
        "file_path": file_path,
        "content": "",
        "pages": [],
        "processing_time": 0,
        "total_pages": 0,
        "standard_parsed_pages": 0, 
        "vision_parsed_pages": 0,
        "total_tokens_used": 0
    }
    
    try:
        # Split document into pages
        logger.info(f"Splitting document {file_path} into pages")
        pages = split_document_by_page(file_path)
        result["total_pages"] = len(pages)
        
        if not pages:
            raise ValueError("No pages found in document")
        
        # Process each page based on complexity
        standard_content = []
        vision_content = []
        
        # Try to extract extension for temporary files
        file_ext = Path(file_path).suffix
        
        # Process pages based on complexity
        for i, page_data in enumerate(pages):
            page_num = page_data["page_number"]
            complexity = page_data["complexity"]
            
            # Track page details
            page_result = {
                "page_number": page_num,
                "complexity_score": complexity,
                "parser_used": ""
            }
            
            logger.info(f"Page {page_num}: Complexity score {complexity:.2f}")
            
            # Decide which parser to use based on complexity
            if complexity < complexity_threshold:
                # Use standard parser for this page
                logger.info(f"Page {page_num}: Using standard parser (low complexity)")
                page_result["parser_used"] = "standard"
                standard_content.append(page_data["content"])
                result["standard_parsed_pages"] += 1
                
            else:
                # Use vision parser for this page
                # For PDFs, we can extract just this page to a temp file
                if file_path.lower().endswith('.pdf'):
                    try:
                        import pypdf
                        
                        with tempfile.NamedTemporaryFile(suffix=file_ext, delete=False) as temp_file:
                            temp_path = temp_file.name
                            
                        # Create a new PDF with just this page
                        with open(file_path, 'rb') as file:
                            pdf = pypdf.PdfReader(file)
                            writer = pypdf.PdfWriter()
                            writer.add_page(pdf.pages[page_num - 1])
                            
                            with open(temp_path, 'wb') as output_file:
                                writer.write(output_file)
                        
                        # Parse this single page with vision parser
                        logger.info(f"Page {page_num}: Using vision parser (high complexity)")
                        page_result["parser_used"] = "vision"
                        
                        # We will force the vision parser by setting content to empty
                        # to ensure the quality check fails
                        single_page_result = parse_document(temp_path)
                        vision_content.append(single_page_result["content"])
                        
                        # Track token usage
                        page_result["tokens_used"] = single_page_result["api_tokens_used"]
                        result["total_tokens_used"] += single_page_result["api_tokens_used"]
                        
                        # Clean up temp file
                        os.unlink(temp_path)
                        
                    except Exception as e:
                        logger.error(f"Error processing page {page_num} with vision parser: {e}")
                        # Fall back to standard parser content
                        page_result["parser_used"] = "standard_fallback"
                        standard_content.append(page_data["content"])
                        
                else:
                    # For non-PDF files, we'll use the vision parser on the whole file
                    # In production, you'd implement proper page extraction for each file type
                    logger.info(f"Non-PDF file: Using vision parser for entire document")
                    
                    # Force vision parser for the entire document
                    entire_doc_result = parse_document(file_path)
                    result["content"] = entire_doc_result["content"]
                    result["total_tokens_used"] = entire_doc_result["api_tokens_used"]
                    result["vision_parsed_pages"] = result["total_pages"]
                    result["standard_parsed_pages"] = 0
                    result["processing_time"] = time.time() - start_time
                    
                    # Return early since we processed the whole document
                    return result
                
                result["vision_parsed_pages"] += 1
            
            # Add page result to tracking
            result["pages"].append(page_result)
        
        # Combine content from all pages
        full_content = []
        
        # Add standard content first
        if standard_content:
            full_content.extend(standard_content)
            
        # Add vision content
        if vision_content:
            full_content.extend(vision_content)
            
        # Join all content
        result["content"] = "\n\n".join(full_content)
        
    except Exception as e:
        logger.error(f"Error in early exit parser: {e}")
        # Fall back to processing the entire document with the cost-optimized parser
        logger.info("Falling back to processing entire document with cost-optimized parser")
        
        fallback_result = parse_document(file_path)
        result["content"] = fallback_result["content"]
        result["total_tokens_used"] = fallback_result["api_tokens_used"]
        result["fallback_method"] = fallback_result["method_used"]
    
    # Calculate processing time
    result["processing_time"] = time.time() - start_time
    
    return result

def main():
    """Command-line interface for the early exit parser"""
    if len(sys.argv) < 2:
        print("Usage: python early_exit_parser.py path/to/document.pdf [complexity_threshold]")
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
    
    try:
        print(f"Processing {file_path} with complexity threshold {complexity_threshold}...")
        result = process_with_early_exit(file_path, complexity_threshold)
        
        # Print summary
        print("\n=== Processing Summary ===")
        print(f"Total pages: {result['total_pages']}")
        print(f"Standard parsed pages: {result['standard_parsed_pages']}")
        print(f"Vision parsed pages: {result['vision_parsed_pages']}")
        print(f"Total tokens used: {result['total_tokens_used']}")
        print(f"Processing time: {result['processing_time']:.2f} seconds")
        
        # Preview content
        content_preview = result["content"][:500] + "..." if len(result["content"]) > 500 else result["content"]
        print("\n=== Content Preview ===")
        print(content_preview)
        
        # Ask if user wants to save the results
        save_results = input("\nDo you want to save the parsed content to a file? (y/n): ").lower().startswith('y')
        
        if save_results:
            # Get the original filename without extension
            file_base = Path(file_path).stem
            output_path = f"{file_base}_parsed_early_exit.txt"
            
            # Save content to text file
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result["content"])
            
            # Save metadata to JSON
            metadata = {k: v for k, v in result.items() if k != "content"}
            with open(f"{file_base}_metadata_early_exit.json", "w", encoding="utf-8") as f:
                json.dump(metadata, f, indent=2)
            
            print(f"Content saved to {output_path}")
            print(f"Metadata saved to {file_base}_metadata_early_exit.json")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
