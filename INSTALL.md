# Installation Guide

## Overview

ResumeMatch is now structured as a standard Python package. This guide covers installation methods for different use cases.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for development installation)

## Installation Methods

### 1. Installation from Source (Current Method)

Since ResumeMatch is in early development and not yet published to PyPI, install from source:

```bash
# Clone the repository
git clone https://github.com/anshuman-nanda/ResumeMatch.git
cd ResumeMatch

# Install in editable mode (recommended for development)
pip install -e .

# Or install normally
pip install .
```

### 2. Development Installation

For contributors and developers who want to work on the codebase:

```bash
# Clone the repository
git clone https://github.com/anshuman-nanda/ResumeMatch.git
cd ResumeMatch

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in editable mode with development dependencies
pip install -e ".[dev]"

# Verify installation
python -c "import resumematch; print(resumematch.__version__)"
```

### 3. Future: Installation from PyPI

Once published to PyPI, you'll be able to install with:

```bash
# Standard installation (when available)
pip install resumematch

# With development dependencies (when available)
pip install resumematch[dev]
```

## Package Structure

After installation, the package provides the following modules:

```python
from resumematch import ResumeAnalyzer, ResumeParser, ResumeMatcher
from resumematch.utils import clean_text, normalize_whitespace
```

## Verifying Installation

To verify that ResumeMatch is installed correctly:

```bash
# Check package version
python -c "import resumematch; print(resumematch.__version__)"

# Run example scripts
python examples/basic_usage.py
python examples/library_usage.py

# Run tests (if development dependencies are installed)
pytest tests/
```

## Troubleshooting

### Common Issues

**Issue: `ModuleNotFoundError: No module named 'resumematch'`**

Solution: Ensure you've installed the package:
```bash
pip install -e .
```

**Issue: Permission denied during installation**

Solution: Use a virtual environment or install with `--user` flag:
```bash
pip install --user -e .
```

**Issue: Import errors**

Solution: Verify your Python version:
```bash
python --version  # Should be 3.8 or higher
```

## Uninstallation

To uninstall ResumeMatch:

```bash
pip uninstall resumematch
```

## Next Steps

- Check out the [README.md](README.md) for usage examples
- Read the [CONTRIBUTING.md](CONTRIBUTING.md) guide to contribute
- Explore the [examples/](examples/) directory for code samples
- Run tests to ensure everything works: `pytest tests/`
