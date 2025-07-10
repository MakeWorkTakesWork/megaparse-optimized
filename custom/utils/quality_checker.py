"""
Document Quality Checker

This module provides functions to check the quality of parsed document content
to determine if the parsing result is sufficient or if additional parsing is needed.
"""

import re
from typing import List, Dict, Any, Optional


def is_quality_sufficient(
    content: str, 
    min_characters: int = 100, 
    min_words: int = 20,
    min_paragraphs: int = 1,
    error_indicators: Optional[List[str]] = None
) -> bool:
    """
    Check if the parsed content meets minimum quality standards.
    
    Args:
        content (str): The parsed content to evaluate
        min_characters (int): Minimum number of characters required
        min_words (int): Minimum number of words required
        min_paragraphs (int): Minimum number of paragraphs required
        error_indicators (List[str], optional): List of strings that indicate parsing errors
        
    Returns:
        bool: True if content seems to have sufficient quality
    """
    # Default error indicators if none provided
    if error_indicators is None:
        error_indicators = [
            "failed to extract", 
            "cannot parse", 
            "error processing",
            "[?]" * 5,  # Multiple unknown character markers often indicate OCR failure
            "error: unable to",
            "processing error",
            "extraction failed"
        ]
    
    # Skip empty content
    if not content:
        print("Content is empty")
        return False
        
    # Check content length
    if len(content) < min_characters:
        print(f"Content too short: {len(content)} characters (minimum: {min_characters})")
        return False
        
    # Check word count
    word_count = len(content.split())
    if word_count < min_words:
        print(f"Too few words detected: {word_count} words (minimum: {min_words})")
        return False
    
    # Check paragraph count (assuming paragraphs are separated by double newlines)
    paragraphs = re.split(r'\n\s*\n', content)
    if len(paragraphs) < min_paragraphs:
        print(f"Too few paragraphs detected: {len(paragraphs)} (minimum: {min_paragraphs})")
        return False
        
    # Check for error indicators
    for indicator in error_indicators:
        if indicator.lower() in content.lower():
            print(f"Found error indicator: '{indicator}'")
            return False
    
    # Additional check: Does it have some structure? (paragraphs, etc.)
    if "\n" not in content and len(content) > 500:
        print("Content lacks structure (no line breaks found in a long document)")
        return False
    
    # Additional check: Does it have reasonable character distribution?
    # E.g., not just repeated characters or garbage
    char_counts = {}
    for char in content:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    # If a single character makes up more than 30% of the content, it's suspicious
    max_char_ratio = max(char_counts.values()) / len(content)
    if max_char_ratio > 0.3 and len(content) > 100:
        print(f"Suspicious character distribution (single character makes up {max_char_ratio:.1%} of content)")
        return False
        
    return True


def get_quality_score(content: str) -> float:
    """
    Calculate a quality score for the parsed content from 0.0 to 1.0.
    
    This is a more nuanced version of is_quality_sufficient that returns a
    continuous score rather than a binary decision.
    
    Args:
        content (str): The parsed content to evaluate
        
    Returns:
        float: Quality score from 0.0 (very poor) to 1.0 (excellent)
    """
    if not content:
        return 0.0
    
    score = 0.0
    
    # Length factors (up to 0.3)
    char_length = min(len(content) / 1000, 1.0) * 0.15
    word_count = min(len(content.split()) / 200, 1.0) * 0.15
    score += char_length + word_count
    
    # Structure factors (up to 0.4)
    paragraphs = content.split("\n\n")
    paragraph_score = min(len(paragraphs) / 5, 1.0) * 0.2
    
    # Has reasonable paragraph length variation?
    if len(paragraphs) > 1:
        lengths = [len(p) for p in paragraphs]
        variance = sum((l - sum(lengths)/len(lengths))**2 for l in lengths) / len(lengths)
        variance_score = min(variance / 1000, 1.0) * 0.1
    else:
        variance_score = 0.0
    
    # Has headings or structure?
    structure_indicators = ["#", "##", "Chapter", "Section", "Part", "Title"]
    structure_score = 0.1 if any(i in content for i in structure_indicators) else 0.0
    
    score += paragraph_score + variance_score + structure_score
    
    # Content quality factors (up to 0.3)
    error_indicators = [
        "failed to extract", "cannot parse", "error processing",
        "[?]" * 3, "error: unable to", "processing error"
    ]
    
    # Penalize for error indicators
    error_penalty = sum(0.1 for i in error_indicators if i.lower() in content.lower())
    error_score = max(0.0, 0.3 - error_penalty)
    
    score += error_score
    
    return min(score, 1.0)  # Cap at 1.0
