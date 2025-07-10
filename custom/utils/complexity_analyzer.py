"""
Document Complexity Analyzer

This module provides functions to analyze document complexity to determine
which parsing strategy would be most effective and cost-efficient.
"""

import re
from typing import Dict, List, Set, Tuple, Optional, Any


def analyze_page_complexity(page_content: str) -> float:
    """
    Analyze a page's content to determine its text vs. visual complexity
    
    Returns a score from 0.0 to 1.0, where:
    - 0.0 means highly textual (standard parser sufficient)
    - 1.0 means highly visual (vision parser needed)
    
    Args:
        page_content (str): The content of the page to analyze
        
    Returns:
        float: Complexity score from 0.0 (simple text) to 1.0 (complex visual)
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
    table_indicators = [
        "table", "column", "row", "|", "+--", "+--+", "----+",
        "-----", "┌", "┐", "└", "┘", "─", "│", "┼", "┬", "┴", "┤", "├"
    ]
    has_table_indicators = any(indicator in page_content for indicator in table_indicators)
    
    # 4. Check for bullet points and formatting
    bullet_indicators = ["•", "○", "●", "■", "□", "◆", "◇", "▪", "▫", "►", "▻"]
    has_bullets = any(indicator in page_content for indicator in bullet_indicators)
    
    # 5. Check for image placeholders or captions
    image_indicators = ["[image]", "[figure]", "fig.", "figure", "image:", "photo:", "diagram"]
    has_image_indicators = any(indicator in page_content.lower() for indicator in image_indicators)
    
    # 6. Check for complex formatting based on patterns of whitespace
    whitespace_pattern = re.findall(r'\s{2,}', page_content)
    has_complex_whitespace = len(whitespace_pattern) > total_chars / 50
    
    # 7. Check for math expressions
    math_indicators = ["=", "+", "-", "*", "/", "^", "√", "∫", "∑", "∏", "÷", "×", "±"]
    math_count = sum(page_content.count(i) for i in math_indicators)
    has_math = math_count > 5
    
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
    
    # Complex whitespace patterns often indicate structured content
    if has_complex_whitespace:
        complexity_score += 0.2
    
    # Mathematical content often benefits from vision models
    if has_math:
        complexity_score += 0.2
    
    # Cap at 1.0
    return min(complexity_score, 1.0)


def calculate_document_complexity(pages: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calculate overall document complexity and statistics based on page analysis.
    
    Args:
        pages (List[Dict]): List of page data, each with 'content' and optional 'complexity'
    
    Returns:
        Dict: Document complexity statistics
    """
    if not pages:
        return {
            'avg_complexity': 0.0,
            'max_complexity': 0.0,
            'complex_page_ratio': 0.0,
            'recommended_parser': 'standard'
        }
    
    # Calculate complexity for pages that don't have it yet
    for page in pages:
        if 'complexity' not in page and 'content' in page:
            page['complexity'] = analyze_page_complexity(page['content'])
    
    complexities = [page.get('complexity', 0.0) for page in pages]
    avg_complexity = sum(complexities) / len(complexities)
    max_complexity = max(complexities)
    complex_pages = sum(1 for c in complexities if c > 0.5)
    complex_page_ratio = complex_pages / len(pages)
    
    # Determine recommended parser based on complexity
    if max_complexity > 0.7 or complex_page_ratio > 0.3:
        recommended_parser = 'vision'
    elif max_complexity > 0.5 or complex_page_ratio > 0.1:
        recommended_parser = 'early_exit'
    else:
        recommended_parser = 'standard'
    
    return {
        'avg_complexity': avg_complexity,
        'max_complexity': max_complexity,
        'complex_page_ratio': complex_page_ratio,
        'complex_pages': complex_pages,
        'total_pages': len(pages),
        'recommended_parser': recommended_parser
    }


def identify_complex_sections(content: str) -> List[Dict[str, Any]]:
    """
    Identify complex sections within a document that might benefit from vision parsing.
    
    Args:
        content (str): Document content
        
    Returns:
        List[Dict]: List of complex sections with start/end positions and complexity scores
    """
    # Split content into sections (e.g., by double newlines or headings)
    sections = re.split(r'\n\s*\n|\n#+\s+', content)
    complex_sections = []
    
    start_pos = 0
    for section in sections:
        if not section.strip():
            start_pos += len(section) + 2  # +2 for the newlines
            continue
            
        complexity = analyze_page_complexity(section)
        
        if complexity > 0.5:
            complex_sections.append({
                'start': start_pos,
                'end': start_pos + len(section),
                'complexity': complexity,
                'content': section[:100] + '...' if len(section) > 100 else section
            })
            
        start_pos += len(section) + 2  # +2 for the newlines
    
    return complex_sections
