#!/usr/bin/env python
"""
MegaParse with RAG Optimization
Parses a document and automatically optimizes it for RAG applications
"""

import os
import sys
import json
import time
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import our RAG preprocessor
import rag_preprocessor

def parse_with_optimization(file_path):
    """
    Parse a document and optimize for RAG
    
    Args:
        file_path (str): Path to the document to parse
        
    Returns:
        dict: Results and paths to generated files
    """
    start_time = time.time()
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Document not found: {file_path}")
    
    print(f"\n=== Processing document: {os.path.basename(file_path)} ===")
    
    # Step 1: Parse with MegaParse
    try:
        print("Trying standard parser (no API cost)...")
        
        # Import MegaParse
        from megaparse import MegaParse
        
        standard_parser = MegaParse()
        parsed_content = standard_parser.load(file_path)
        
        # Basic quality check
        quality_sufficient = len(parsed_content) > 100 and len(parsed_content.split()) > 20
        
        if quality_sufficient:
            print("✅ Standard parser succeeded with sufficient quality!")
            method_used = "standard_parser"
            api_tokens_used = 0
        else:
            print("⚠️ Standard parser output deemed insufficient quality, trying vision parser...")
            
            # Try vision parser
            from megaparse.parser.megaparse_vision import MegaParseVision
            from langchain_openai import ChatOpenAI
            
            # Check if OpenAI API key is set
            if not os.getenv("OPENAI_API_KEY"):
                raise ValueError("OPENAI_API_KEY not found in environment variables")
            
            model = ChatOpenAI(
                model="gpt-4o-mini",
                api_key=os.getenv("OPENAI_API_KEY"),
                max_tokens=4000
            )
            
            vision_parser = MegaParseVision(model=model)
            vision_content = vision_parser.convert(file_path)
            
            parsed_content = str(vision_content)
            method_used = "vision_parser_with_gpt4o_mini"
            api_tokens_used = int(len(parsed_content.split()) * 1.3)  # Rough estimate
            print("✅ Vision parser succeeded!")
            
    except Exception as e:
        print(f"⚠️ Parsing error: {str(e)}")
        raise
    
    # Calculate processing time
    parsing_time = round(time.time() - start_time, 2)
    
    # Step 2: Save parsed content
    file_base = os.path.splitext(os.path.basename(file_path))[0]
    output_path = f"{file_base}_parsed.txt"
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(parsed_content)
    
    # Save metadata
    metadata = {
        "file_path": file_path,
        "method_used": method_used,
        "processing_time": parsing_time,
        "quality_sufficient": quality_sufficient,
        "api_tokens_used": api_tokens_used
    }
    
    metadata_path = f"{file_base}_metadata.json"
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)
    
    print(f"Content saved to {output_path}")
    print(f"Metadata saved to {metadata_path}")
    
    # Step 3: RAG Optimization
    print("\n=== Running RAG Optimization ===")
    rag_start_time = time.time()
    
    rag_results = rag_preprocessor.post_process_document(output_path)
    rag_time = round(time.time() - rag_start_time, 2)
    
    if "error" not in rag_results:
        print(f"RAG optimization completed in {rag_time} seconds")
    else:
        print(f"⚠️ RAG optimization failed: {rag_results.get('error')}")
    
    # Combine all results
    results = {
        "original_file": file_path,
        "parsed_file": output_path,
        "metadata_file": metadata_path,
        "parsing_method": method_used,
        "parsing_time": parsing_time,
        "api_tokens_used": api_tokens_used,
        "rag_optimization_time": rag_time,
        "rag_files": rag_results
    }
    
    return results

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Usage: python megaparse_rag.py path/to/document.pdf")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    try:
        print("=" * 60)
        print(" MegaParse + RAG Optimization Pipeline")
        print("=" * 60)
        
        results = parse_with_optimization(file_path)
        
        # Print summary
        print("\n" + "=" * 60)
        print(" Pipeline Summary")
        print("=" * 60)
        print(f"Document: {os.path.basename(results['original_file'])}")
        print(f"Parser: {results['parsing_method']}")
        print(f"Parsing time: {results['parsing_time']} seconds")
        print(f"API tokens used: {results['api_tokens_used']}")
        print(f"Files generated:")
        print(f"  - Parsed text: {os.path.basename(results['parsed_file'])}")
        print(f"  - Metadata: {os.path.basename(results['metadata_file'])}")
        
        if "error" not in results.get("rag_files", {}):
            rag_file = results.get("rag_files", {}).get("rag_optimized_file")
            chunking_file = results.get("rag_files", {}).get("chunking_guide")
            
            if rag_file:
                print(f"  - RAG-optimized file: {os.path.basename(rag_file)}")
            if chunking_file:
                print(f"  - Chunking guide: {os.path.basename(chunking_file)}")
        else:
            print(f"  ⚠️ RAG optimization failed")
        
        print("=" * 60)
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
