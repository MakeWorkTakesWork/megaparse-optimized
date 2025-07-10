"""
Cost Tracking Utilities

This module provides utilities for tracking and estimating the cost of API usage
when parsing documents with MegaParse.
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Any, Optional


# Define cost constants (prices subject to change)
MODEL_COSTS = {
    # Cost per 1000 tokens (input, output)
    "gpt-4o": (0.01, 0.03),
    "gpt-4o-mini": (0.0015, 0.006),
    "gpt-4-turbo": (0.01, 0.03),
    "gpt-4": (0.03, 0.06),
    "gpt-3.5-turbo": (0.001, 0.002),
    "claude-3-opus": (0.015, 0.075),
    "claude-3-sonnet": (0.003, 0.015),
    "claude-3-haiku": (0.00025, 0.00125),
}


def estimate_token_usage(content: str, model: str = "gpt-4o-mini") -> Dict[str, Any]:
    """
    Estimate token usage for a given content and model.
    
    Args:
        content (str): The content to estimate tokens for
        model (str): The model name to use for cost estimation
        
    Returns:
        Dict: Token usage estimation including input tokens, output tokens, and cost
    """
    # Rough estimate of tokens: 1 token ≈ 4 characters for English text
    char_count = len(content)
    words = content.split()
    word_count = len(words)
    
    # Different models have different tokenization, this is a rough estimate
    estimated_tokens = max(int(char_count / 4), word_count)
    
    # For image/vision models, add additional tokens for image processing
    is_vision_model = True if 'vision' in model.lower() or model in ["gpt-4o", "gpt-4-vision"] else False
    
    input_tokens = estimated_tokens
    output_tokens = estimated_tokens
    
    if is_vision_model:
        # Vision models have higher token usage for image processing
        input_tokens += 1000  # Rough estimate for image tokens
    
    # Calculate cost based on model pricing
    input_cost_per_1k, output_cost_per_1k = MODEL_COSTS.get(
        model, (0.01, 0.03)  # Default to gpt-4o pricing if model not found
    )
    
    input_cost = (input_tokens / 1000) * input_cost_per_1k
    output_cost = (output_tokens / 1000) * output_cost_per_1k
    total_cost = input_cost + output_cost
    
    return {
        "model": model,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
        "input_cost": input_cost,
        "output_cost": output_cost,
        "total_cost": total_cost
    }


def estimate_token_cost(
    content: str, 
    model: str = "gpt-4o-mini",
    content_is_output: bool = True
) -> float:
    """
    Estimate the cost of API usage for a given content and model.
    
    Args:
        content (str): The content to estimate cost for
        model (str): The model name to use for cost estimation
        content_is_output (bool): Whether the content is model output (True) or input (False)
        
    Returns:
        float: Estimated cost in USD
    """
    char_count = len(content)
    words = content.split()
    word_count = len(words)
    
    # Different models have different tokenization, this is a rough estimate
    estimated_tokens = max(int(char_count / 4), word_count)
    
    # Get cost rates
    input_cost_per_1k, output_cost_per_1k = MODEL_COSTS.get(
        model, (0.01, 0.03)  # Default to gpt-4o pricing if model not found
    )
    
    # Calculate cost
    if content_is_output:
        cost = (estimated_tokens / 1000) * output_cost_per_1k
    else:
        cost = (estimated_tokens / 1000) * input_cost_per_1k
    
    return cost


class CostTracker:
    """
    Track API usage costs across multiple document parsing operations.
    """
    
    def __init__(self, log_file: Optional[str] = None):
        """
        Initialize the cost tracker.
        
        Args:
            log_file (str, optional): Path to log file for saving cost data
        """
        self.logs = []
        self.log_file = log_file or os.path.join(
            os.path.expanduser("~"), 
            ".megaparse_cost_tracker.json"
        )
        self.load_logs()
    
    def load_logs(self) -> None:
        """Load existing logs from file if it exists."""
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, 'r') as f:
                    self.logs = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                self.logs = []
    
    def save_logs(self) -> None:
        """Save logs to file."""
        try:
            with open(self.log_file, 'w') as f:
                json.dump(self.logs, f, indent=2)
        except Exception as e:
            print(f"Warning: Failed to save cost logs: {e}")
    
    def log_usage(
        self, 
        file_path: str, 
        model: str, 
        input_tokens: int, 
        output_tokens: int, 
        parser_type: str
    ) -> Dict[str, Any]:
        """
        Log API usage for a document parsing operation.
        
        Args:
            file_path (str): Path to the document
            model (str): Model used for parsing
            input_tokens (int): Number of input tokens
            output_tokens (int): Number of output tokens
            parser_type (str): Type of parser used ('standard', 'vision', etc.)
            
        Returns:
            Dict: Log entry with cost information
        """
        # Get cost rates
        input_cost_per_1k, output_cost_per_1k = MODEL_COSTS.get(
            model, (0.01, 0.03)  # Default to gpt-4o pricing if model not found
        )
        
        # Calculate costs
        input_cost = (input_tokens / 1000) * input_cost_per_1k
        output_cost = (output_tokens / 1000) * output_cost_per_1k
        total_cost = input_cost + output_cost
        
        # Create log entry
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "file_path": file_path,
            "model": model,
            "parser_type": parser_type,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": input_tokens + output_tokens,
            "input_cost": input_cost,
            "output_cost": output_cost,
            "total_cost": total_cost
        }
        
        # Add to logs and save
        self.logs.append(log_entry)
        self.save_logs()
        
        return log_entry
    
    def get_summary(self, days: Optional[int] = None) -> Dict[str, Any]:
        """
        Get a summary of API usage and costs.
        
        Args:
            days (int, optional): If provided, only include logs from the last N days
            
        Returns:
            Dict: Summary of API usage and costs
        """
        if days:
            # Filter logs by date
            cutoff = datetime.now().timestamp() - (days * 86400)
            filtered_logs = [
                log for log in self.logs 
                if datetime.fromisoformat(log["timestamp"]).timestamp() > cutoff
            ]
        else:
            filtered_logs = self.logs
        
        # Calculate summary statistics
        total_cost = sum(log["total_cost"] for log in filtered_logs)
        total_tokens = sum(log["total_tokens"] for log in filtered_logs)
        file_count = len(set(log["file_path"] for log in filtered_logs))
        
        # Group by model and parser type
        model_costs = {}
        parser_costs = {}
        
        for log in filtered_logs:
            model = log["model"]
            parser = log["parser_type"]
            
            if model not in model_costs:
                model_costs[model] = 0
            model_costs[model] += log["total_cost"]
            
            if parser not in parser_costs:
                parser_costs[parser] = 0
            parser_costs[parser] += log["total_cost"]
        
        return {
            "total_cost": total_cost,
            "total_tokens": total_tokens,
            "file_count": file_count,
            "average_cost_per_file": total_cost / max(file_count, 1),
            "model_costs": model_costs,
            "parser_costs": parser_costs,
            "date_range": {
                "start": filtered_logs[0]["timestamp"] if filtered_logs else None,
                "end": filtered_logs[-1]["timestamp"] if filtered_logs else None
            },
            "days": days
        }
