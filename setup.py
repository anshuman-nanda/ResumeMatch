"""Setup script for ResumeMatch package."""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="resumematch",
    version="0.1.0",
    author="Anshuman Nanda",
    description="AI-Powered Resume Analysis & Job Matching Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anshuman-nanda/ResumeMatch",
    project_urls={
        "Bug Tracker": "https://github.com/anshuman-nanda/ResumeMatch/issues",
        "Documentation": "https://github.com/anshuman-nanda/ResumeMatch/wiki",
        "Source Code": "https://github.com/anshuman-nanda/ResumeMatch",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Office/Business",
    ],
    python_requires=">=3.8",
    install_requires=[
        # Core dependencies will be added as features are implemented
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
            "isort>=5.12.0",
            "pre-commit>=3.0.0",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
