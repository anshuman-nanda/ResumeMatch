# Contributing to ResumeMatch

First off, thank you for considering contributing to ResumeMatch! It's people like you that make ResumeMatch such a great tool.

## Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct:
- Be respectful and inclusive
- Welcome newcomers and help them get started
- Focus on what is best for the community
- Show empathy towards other community members

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if applicable**
- **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List any similar features in other tools**

### Pull Requests

1. Fork the repository and create your branch from `main`
2. If you've added code that should be tested, add tests
3. Ensure the test suite passes
4. Make sure your code follows the existing style
5. Write a clear commit message
6. Update documentation as needed

## Development Setup

```bash
# Clone your fork
# Note: Replace YOUR_USERNAME with your GitHub username
# Use the current repository name until the rename is complete:
git clone https://github.com/YOUR_USERNAME/resume-intelligence.git
cd resume-intelligence

# After the rename, use:
# git clone https://github.com/YOUR_USERNAME/ResumeMatch.git
# cd ResumeMatch

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt  # If available
```

## Coding Standards

- Follow PEP 8 style guide for Python code
- Write meaningful commit messages
- Comment your code where necessary
- Keep functions focused and modular
- Write tests for new features

## Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=resumematch
```

## Documentation

- Update the README.md if you change functionality
- Add docstrings to new functions and classes
- Update examples if you add new features

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.

Thank you for contributing to ResumeMatch! 🎉
