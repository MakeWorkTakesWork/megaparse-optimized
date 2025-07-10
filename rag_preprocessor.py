#!/usr/bin/env python
"""
RAG Preprocessor for MegaParse
Automatically enhances parsed documents for RAG applications
"""

import re
import json
import os
from pathlib import Path
from datetime import datetime

def preprocess_for_rag(input_file, output_file=None):
    """
    Preprocesses a parsed document file for better RAG performance.
    
    Args:
        input_file (str): Path to the parsed text file
        output_file (str, optional): Path to save the optimized output. If None, will generate one.
    
    Returns:
        str: Path to the processed file
    """
    if output_file is None:
        base_path = os.path.splitext(input_file)[0]
        output_file = f"{base_path}_RAG.md"
    
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Step 1: Identify and format section headers
    lines = content.split('\n')
    processed_lines = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            processed_lines.append(line)
            continue
            
        # Check if this is likely a header (standalone line, shorter than 60 chars)
        is_header = (i == 0 or not lines[i-1].strip()) and \
                    (i == len(lines)-1 or not lines[i+1].strip()) and \
                    len(line) < 60 and not line.endswith(':')
                    
        if is_header:
            # Determine heading level (main headers vs sub-headers)
            if line.isupper() or "Process" in line or any(key in line for key in ["Sales", "Demo", "Set up", "PoC", "Services", "Guide", "Product"]):
                processed_lines.append(f"\n## {line}\n")
            else:
                processed_lines.append(f"\n### {line}\n")
        else:
            processed_lines.append(line)
    
    # Step 2: Reconstruct tables where possible
    content = '\n'.join(processed_lines)
    
    # Look for table-like patterns (consecutive lines with similar column count)
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        # Check for table header candidates
        if re.match(r'^(Stage|Customer|Name|Title|Type)\s+\w+', lines[i]):
            # Count words to estimate columns
            potential_table_start = i
            words = lines[i].split()
            potential_columns = []
            
            # Try to identify column headers
            for word in words:
                if word[0].isupper() and len(word) > 2:
                    potential_columns.append(word)
            
            # If we have potential columns, look for table rows
            if len(potential_columns) >= 2:
                # Create markdown table header
                table_md = f"\n| {' | '.join(potential_columns)} |\n"
                table_md += "| " + " | ".join(["---"] * len(potential_columns)) + " |\n"
                
                # Look ahead for table rows
                row_count = 0
                max_rows = 10
                j = i + 1
                while j < len(lines) and row_count < max_rows:
                    if not lines[j].strip():
                        j += 1
                        continue
                    
                    # Simple heuristic: Lines with similar number of parts might be table rows
                    parts = lines[j].split()
                    if len(parts) >= len(potential_columns):
                        # Try to split into columns
                        row_values = []
                        current_col = ""
                        col_idx = 0
                        
                        for part in parts:
                            if col_idx < len(potential_columns)-1 and len(current_col) > 5:
                                row_values.append(current_col.strip())
                                current_col = part
                                col_idx += 1
                            else:
                                if current_col:
                                    current_col += " " + part
                                else:
                                    current_col = part
                        
                        if current_col:
                            row_values.append(current_col.strip())
                        
                        # Ensure we have enough columns
                        while len(row_values) < len(potential_columns):
                            row_values.append("")
                        
                        # Add row to table
                        table_md += f"| {' | '.join(row_values[:len(potential_columns)])} |\n"
                        row_count += 1
                    else:
                        # This line doesn't match table pattern
                        break
                    j += 1
                
                # If we found rows, replace the original text with the markdown table
                if row_count > 0:
                    # Remove original lines
                    lines[potential_table_start:j] = [table_md]
                    i = potential_table_start + 1
                    continue
        i += 1
    
    content = '\n'.join(lines)
    
    # Step 3: Format lists properly
    # Number lists
    content = re.sub(r'(\n\d+\.\s+)', r'\n1. ', content)
    
    # Bullet lists
    content = re.sub(r'(\n\s*[-•]\s+)', r'\n* ', content)
    
    # Format email sections
    email_sections = re.findall(r'(Hey\s+folks,.*?(?=\n\n\w+|$))', content, re.DOTALL)
    for email in email_sections:
        formatted_email = f"\n```\n{email}\n```\n"
        content = content.replace(email, formatted_email)
    
    # Step 4: Add metadata for RAG
    # Extract document title
    title_match = re.search(r'^(.+?)(?=\n|$)', content)
    title = title_match.group(1).strip() if title_match else "Untitled Document"
    
    # Extract key topics
    topics = []
    for topic in ["Sales", "POC", "Process", "Demo", "Evaluation", "Zendesk", "Salesforce", "Product", "Messaging"]:
        if topic in content:
            topics.append(topic.lower())
    
    metadata = {
        "title": title,
        "document_type": "process" if "Process" in title else "guide",
        "primary_topics": topics,
        "last_preprocessed": datetime.now().strftime("%Y-%m-%d")
    }
    
    metadata_section = "---\n"
    for key, value in metadata.items():
        if isinstance(value, list):
            metadata_section += f"{key}: {', '.join(value)}\n"
        else:
            metadata_section += f"{key}: {value}\n"
    metadata_section += "---\n\n"
    
    content = metadata_section + content
    
    # Write the processed content to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ RAG optimization complete: {output_file}")
    return output_file

def create_chunking_guide(input_file, output_file=None):
    """
    Creates a JSON file with chunking recommendations for RAG
    
    Args:
        input_file (str): Path to the processed markdown file
        output_file (str, optional): Path to save the chunking guide
    
    Returns:
        str: Path to the chunking guide file
    """
    if output_file is None:
        base_path = os.path.splitext(input_file)[0]
        output_file = f"{base_path}_chunking.json"
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract headers to create a structural map
    headers = re.findall(r'##\s+(.*?)$', content, re.MULTILINE)
    
    # Create chunking recommendations
    chunking_guide = {
        "document_id": Path(input_file).stem,
        "recommended_chunk_size": 512,
        "chunk_overlap": 128,
        "logical_sections": []
    }
    
    priority_sections = ["Sales & POC Process", "Demo", "Set up process", "Product Messaging"]
    preserve_sections = ["Sales & POC Process", "Important notes", "Set up process", "Key Messages"]
    
    for header in headers:
        header = header.strip()
        chunking_guide["logical_sections"].append({
            "section": header,
            "preserve_as_unit": header in preserve_sections or any(term in header for term in ["Messaging", "Key", "Competitive"]),
            "priority_weight": 1.2 if header in priority_sections or "Messaging" in header else 1.0
        })
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(chunking_guide, f, indent=2)
    
    print(f"✅ Chunking guide created: {output_file}")
    return output_file

def post_process_document(document_path, enable_chunking_guide=True):
    """
    Main function to run all RAG optimizations on a document
    
    Args:
        document_path (str): Path to the parsed document
        enable_chunking_guide (bool): Whether to create a chunking guide
    
    Returns:
        dict: Paths to the optimized files
    """
    results = {}
    
    try:
        # Run RAG preprocessing
        rag_file = preprocess_for_rag(document_path)
        results["rag_optimized_file"] = rag_file
        
        # Create chunking guide if enabled
        if enable_chunking_guide:
            chunking_file = create_chunking_guide(rag_file)
            results["chunking_guide"] = chunking_file
            
        return results
    
    except Exception as e:
        print(f"⚠️ Error during RAG optimization: {str(e)}")
        return {"error": str(e)}

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python rag_preprocessor.py path/to/document.txt")
        sys.exit(1)
    
    document_path = sys.argv[1]
    post_process_document(document_path)
