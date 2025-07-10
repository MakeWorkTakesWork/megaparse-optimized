# MegaParse Cost-Optimized Usage Guide

This guide explains how to use MegaParse with the cost optimization strategies implemented in this package.

## Understanding the Cost Optimization Strategy

We've implemented multiple layers of cost optimization in this package:

1. **Tiered Parsing Approach**: Try free parsing methods first, only fall back to AI when needed
2. **Cost-Effective Models**: Use `gpt-4o-mini` instead of full `gpt-4o` (approximately 8× cheaper)
3. **Early-Exit for Text Pages**: Process image-heavy pages differently from text-heavy pages
4. **Batch Processing**: Efficiently process multiple documents with detailed tracking

This approach can reduce costs by 80-90% compared to naively using high-end AI models for all documents.

## Basic Usage: Cost-Optimized Parser

The simplest way to parse a document with cost optimization is to use the `cost_optimized_parser.py` script:

```bash
# Activate the virtual environment
source venv/bin/activate

# Parse a document with cost optimization
python cost_optimized_parser.py path/to/your/document.pdf
```

This script will:
1. First try the standard parser (zero API cost)
2. Check if the results meet quality thresholds
3. Only use the vision-based parser with `gpt-4o-mini` if necessary

## Advanced Usage: Early-Exit Parser

For more granular control, especially with multi-page documents, use the `early_exit_parser.py`:

```bash
# Process a document with page-by-page analysis
python early_exit_parser.py path/to/your/document.pdf

# Adjust the complexity threshold (0.0-1.0, default: 0.5)
python early_exit_parser.py path/to/your/document.pdf 0.7
```

This parser:
1. Splits the document into individual pages
2. Analyzes each page for complexity
3. Uses the standard parser for simple text pages
4. Only uses the vision parser for complex pages with images, tables, etc.

## Batch Processing

To process multiple documents efficiently:

```bash
# Process all documents in a directory
python batch_processor.py path/to/document/directory

# Specify an output directory
python batch_processor.py path/to/document/directory --output results

# Process documents in subdirectories
python batch_processor.py path/to/document/directory --output results --recursive

# Control parallel processing (default: 2 workers)
python batch_processor.py path/to/document/directory --max-workers 4
```

The batch processor provides:
- Parallel document processing with controlled concurrency
- Detailed statistics about parsing methods and costs
- Structured output files for each document
- A summary report with aggregated statistics

## Checking Costs and Tracking

After processing, each script provides statistics about:
- Which parser was used for each document/page
- How many tokens were used (estimating API costs)
- Processing time and efficiency metrics

For batch processing, a summary JSON file includes detailed stats about the entire batch.

## Customizing the Approach

You can adjust several parameters to fine-tune the optimization:

1. **Quality Threshold**: Modify the `is_quality_sufficient()` function in `cost_optimized_parser.py`
2. **Complexity Analysis**: Adjust the page complexity analysis in `early_exit_parser.py`
3. **Model Selection**: Change the model from `gpt-4o-mini` to another option based on your needs
4. **Batch Size**: Control parallel processing with the `--max-workers` parameter

## Typical Costs

Based on the tiered approach:

- **Text-heavy documents**: $0 (standard parser only)
- **Mixed documents**: $0.15-$1 per document (depends on complexity)
- **Very complex documents**: $2-$5 per document (vision parser used more)

These costs are significantly lower than always using high-end models, which could cost $15-$40 per document.

## Troubleshooting

If you encounter issues:

1. **API Key Problems**: Ensure your OpenAI API key is correctly set in the `.env` file
2. **Dependency Errors**: Run `setup_megaparse.py` to check and install dependencies
3. **Parsing Failures**: Try adjusting the complexity thresholds or quality checks
4. **High Costs**: Review which pages are using the vision parser and adjust thresholds

## Example Workflow for a Large Document Set

For processing thousands of documents:

1. Start with a small test batch to calibrate settings
2. Adjust complexity thresholds based on results
3. Process documents in batches with the batch processor
4. Review cost and quality metrics
5. Fine-tune parameters for subsequent batches
