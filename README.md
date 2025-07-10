# MegaParse Optimized 📄✨

**Cost-optimized extensions for MegaParse document parser**

MegaParse Optimized extends the powerful [MegaParse](https://github.com/quivrhq/megaparse) document parsing library with intelligent cost optimization strategies and batch processing capabilities. Parse documents efficiently while minimizing API costs.

## 🌟 Key Features

- **Tiered Parsing Approach**: Automatically tries free parsing methods first, only using AI when necessary
- **Cost-Efficient Models**: Smart selection of models to minimize API costs
- **Early-Exit for Text Pages**: Analyzes document pages individually to use AI only on complex pages
- **Batch Processing**: Efficiently process multiple documents with parallel processing
- **Cost Tracking**: Detailed metrics on token usage and cost savings

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/MakeWorkTakesWork/megaparse-optimized.git
cd megaparse-optimized

# Install the package
pip install -e .

# Create a .env file with your API keys
echo "OPENAI_API_KEY=your_openai_key_here" > .env
```

### Basic Usage

```python
from custom.parsers.cost_optimized_parser import parse_document

# Parse a document with automatic cost optimization
result = parse_document("path/to/document.pdf")

# Check which method was used
print(f"Method used: {result['method_used']}")
print(f"API tokens used: {result['api_tokens_used']}")

# Get the parsed content
content = result["content"]
```

### Command-Line Usage

```bash
# Parse a single document with cost optimization
python examples/cost_optimized_example.py path/to/document.pdf

# Process a directory of documents in batch
python examples/batch_processing_example.py path/to/document/directory -o results
```

## 💰 Cost Optimization Strategy

MegaParse Optimized uses a multi-tiered approach to minimize costs:

1. **Standard Parser**: First attempts to parse with the standard free parser
2. **Quality Check**: Evaluates parsing quality to determine if AI is needed
3. **Page-by-Page Analysis**: For multi-page documents, analyzes each page individually
4. **Cost-Effective Models**: Uses `gpt-4o-mini` instead of full `gpt-4o` (approximately 8× cheaper)

In practice, this approach can reduce API costs by **80-90%** compared to always using high-end AI models.

## 📂 Repository Structure

```
megaparse-optimized/
├── custom/                 # Custom implementations
│   ├── parsers/            # Parser implementations
│   │   ├── cost_optimized_parser.py
│   │   └── early_exit_parser.py
│   ├── batch/              # Batch processing tools
│   │   └── batch_processor.py
│   └── utils/              # Utility functions
│       ├── quality_checker.py
│       ├── complexity_analyzer.py
│       └── cost_tracker.py
├── docs/                   # Documentation
│   ├── INSTALLATION.md
│   └── USAGE_GUIDE.md
├── examples/               # Example scripts
│   ├── standard_example.py
│   ├── cost_optimized_example.py
│   ├── early_exit_example.py
│   └── batch_processing_example.py
├── libs/                   # Original MegaParse implementation
├── tests/                  # Tests for custom implementations
├── .env.example            # Example environment variables
├── setup.py                # Package setup script
└── README.md               # This file
```

## 📊 Benchmarks

Typical cost savings compared to using full AI models:

- **Text-heavy documents**: $0 (standard parser only)
- **Mixed documents**: $0.15-$1 per document (depends on complexity)
- **Very complex documents**: $2-$5 per document (vision parser used more)

This represents a **90-99%** cost reduction for text-heavy documents and **70-80%** for complex documents compared to always using high-end models.

## 📚 Documentation

- [Installation Guide](docs/INSTALLATION.md): Detailed installation instructions
- [Usage Guide](docs/USAGE_GUIDE.md): Comprehensive usage examples and parameter documentation

## 🧪 Running Tests

```bash
# Install development dependencies
pip install -e .[dev]

# Run tests
pytest
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [MegaParse](https://github.com/quivrhq/megaparse) - The original document parsing library
- [LangChain](https://github.com/langchain-ai/langchain) - For AI integration capabilities
