"""
Tests for the quality checker module
"""

import pytest
from custom.utils.quality_checker import is_quality_sufficient, get_quality_score


def test_empty_content():
    """Test that empty content is considered insufficient."""
    assert is_quality_sufficient("") is False
    assert get_quality_score("") == 0.0


def test_short_content():
    """Test that very short content is considered insufficient."""
    short_text = "This is too short."
    assert is_quality_sufficient(short_text) is False
    assert get_quality_score(short_text) < 0.5


def test_sufficient_content():
    """Test that reasonable content is considered sufficient."""
    good_text = """
    This is a reasonably long paragraph that should pass the quality check.
    It has multiple sentences and a good number of words. The content is
    structured well and doesn't contain any error indicators.
    
    This is a second paragraph to add more structure to the document.
    This additional text helps ensure it passes length requirements.
    """
    assert is_quality_sufficient(good_text) is True
    assert get_quality_score(good_text) > 0.7


def test_error_indicators():
    """Test that content with error indicators is considered insufficient."""
    error_text = """
    This document seems okay at first glance with enough text.
    
    However, it contains the phrase "failed to extract content properly"
    which indicates a parsing problem.
    """
    assert is_quality_sufficient(error_text) is False
    assert get_quality_score(error_text) < 0.7


def test_repeated_characters():
    """Test that content with suspicious character distribution is flagged."""
    repeated_chars = "This document " + "x" * 200 + " has too many repeated characters."
    assert is_quality_sufficient(repeated_chars) is False
    assert get_quality_score(repeated_chars) < 0.5


def test_custom_thresholds():
    """Test using custom thresholds for quality checks."""
    medium_text = "This is a somewhat short text but might be acceptable with lower thresholds."
    
    # Should fail with default thresholds
    assert is_quality_sufficient(medium_text) is False
    
    # Should pass with custom lower thresholds
    assert is_quality_sufficient(medium_text, min_characters=20, min_words=5) is True


def test_structured_content():
    """Test that well-structured content gets a high quality score."""
    structured_text = """
    # Document Title
    
    ## Section 1
    This is the first section with good content.
    
    ## Section 2
    This is the second section with more good content.
    
    ## Section 3
    This final section concludes the document.
    """
    assert is_quality_sufficient(structured_text) is True
    assert get_quality_score(structured_text) > 0.8
