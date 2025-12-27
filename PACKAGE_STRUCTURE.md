# Package Structure Guide

## Overview

ResumeMatch follows a standard Python package layout with a `src/` directory structure. This document explains the organization and purpose of each component.

## Directory Structure

```
ResumeMatch/
├── src/
│   └── resumematch/              # Main package directory
│       ├── __init__.py           # Package initialization
│       ├── core/                 # Core analysis functionality
│       │   ├── __init__.py
│       │   └── analyzer.py       # ResumeAnalyzer class
│       ├── parser/               # Resume parsing modules
│       │   ├── __init__.py
│       │   └── resume_parser.py  # ResumeParser class
│       ├── matcher/              # Matching logic
│       │   ├── __init__.py
│       │   └── resume_matcher.py # ResumeMatcher class
│       └── utils/                # Utility functions
│           ├── __init__.py
│           ├── file_utils.py     # File handling utilities
│           └── text_utils.py     # Text processing utilities
├── tests/                        # Test suite
│   ├── unit/                     # Unit tests
│   │   ├── test_analyzer.py
│   │   ├── test_parser.py
│   │   ├── test_matcher.py
│   │   └── test_utils.py
│   └── integration/              # Integration tests
├── examples/                     # Example scripts
│   ├── basic_usage.py
│   └── library_usage.py
├── docs/                         # Documentation (future)
├── pyproject.toml                # Modern Python project metadata
├── setup.py                      # Package setup script
├── requirements.txt              # Core dependencies
├── requirements-dev.txt          # Development dependencies
├── MANIFEST.in                   # Distribution file manifest
├── README.md                     # Main documentation
├── INSTALL.md                    # Installation guide
├── CONTRIBUTING.md               # Contribution guidelines
└── LICENSE                       # MIT License

```

## Module Descriptions

### Core Modules

#### `resumematch.core`
Contains the main analysis functionality.

- **`ResumeAnalyzer`**: High-level interface for resume analysis
  - Coordinates parsing, matching, and scoring
  - Returns comprehensive analysis results

#### `resumematch.parser`
Handles parsing of resume files in various formats.

- **`ResumeParser`**: Extracts structured data from resume files
  - Supports PDF, DOCX, TXT, RTF formats
  - Extracts contact info, experience, education, skills

#### `resumematch.matcher`
Implements the matching logic between resumes and job descriptions.

- **`ResumeMatcher`**: Compares resumes with job descriptions
  - Semantic analysis and keyword matching
  - Calculates match scores and ATS compatibility
  - Generates improvement recommendations

#### `resumematch.utils`
Utility functions used across the package.

- **`file_utils`**: File handling utilities
  - Path validation
  - File extension checking
  - File size calculation

- **`text_utils`**: Text processing utilities
  - Text cleaning and normalization
  - Whitespace handling
  - Text truncation

## Design Principles

### 1. Modular Architecture
Each component has a single, well-defined responsibility:
- **Parser**: File → Structured Data
- **Matcher**: Resume + Job Description → Match Results
- **Analyzer**: High-level coordination and analysis

### 2. PEP 8 Compliance
All code follows Python naming conventions:
- `snake_case` for functions and variables
- `PascalCase` for classes
- Descriptive names that convey purpose

### 3. Type Hints
All public APIs use type hints for better IDE support and documentation.

### 4. Comprehensive Documentation
Every public function includes:
- Docstring with description
- Args documentation
- Returns documentation
- Raises documentation (when applicable)

### 5. Testability
Code is structured to be easily testable:
- Clear separation of concerns
- Dependency injection where appropriate
- Placeholder implementations for gradual development

## Usage Patterns

### Basic Usage
```python
from resumematch import ResumeAnalyzer

analyzer = ResumeAnalyzer()
result = analyzer.analyze("resume.pdf", "job_description.txt")
print(f"Match score: {result['overall_score']}")
```

### Advanced Usage
```python
from resumematch import ResumeParser, ResumeMatcher

# Parse resume
parser = ResumeParser()
resume_data = parser.parse("resume.pdf")

# Match with job description
matcher = ResumeMatcher()
match_results = matcher.match(resume_data, job_description)

# Get ATS score
ats_score = matcher.calculate_ats_score(resume_data)
```

### Using Utilities
```python
from resumematch.utils import clean_text, validate_file_path

# Clean text
cleaned = clean_text("  Messy   text   here  ")

# Validate file path
path = validate_file_path("resume.pdf")
```

## Extension Points

The package is designed to be extended:

1. **Add New Parsers**: Implement new parsers in `resumematch.parser`
2. **Add Matching Algorithms**: Extend `ResumeMatcher` with new algorithms
3. **Add Utilities**: Add new utility modules in `resumematch.utils`
4. **Add Analyzers**: Create specialized analyzers in `resumematch.core`

## Testing

Run tests to ensure the package structure is working:

```bash
# Run all tests
pytest tests/

# Run specific test modules
pytest tests/unit/test_analyzer.py
pytest tests/unit/test_parser.py

# Run with coverage
pytest --cov=resumematch tests/
```

## Next Steps

- Review [INSTALL.md](INSTALL.md) for installation instructions
- Check [examples/](examples/) for usage examples
- Read [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines
