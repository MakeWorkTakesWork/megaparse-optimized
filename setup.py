#!/usr/bin/env python
"""
Setup script for MegaParse Optimized

This package extends the MegaParse library with cost optimization strategies
and batch processing capabilities.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="megaparse-optimized",
    version="0.1.0",
    author="John Sweazey",
    author_email="johnsweazey@example.com",
    description="Cost-optimized extensions for the MegaParse document parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/megaparse-optimized",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "megaparse",
        "langchain-openai",
        "pypdf",
        "python-dotenv",
        "pillow",
        "rich",
    ],
    extras_require={
        "dev": [
            "pytest",
            "black",
            "flake8",
            "mypy",
        ],
    },
    entry_points={
        "console_scripts": [
            "megaparse-optimized=custom.cli:main",
            "megaparse-batch=custom.batch.batch_processor:main",
        ],
    },
)
