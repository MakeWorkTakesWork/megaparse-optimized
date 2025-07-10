"""
Custom Parser Implementations

This module contains custom parser implementations that extend the base MegaParse
functionality with cost optimization strategies.
"""

from .cost_optimized_parser import parse_document
from .early_exit_parser import process_with_early_exit

__all__ = ['parse_document', 'process_with_early_exit']
