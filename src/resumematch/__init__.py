"""
ResumeMatch - AI-Powered Resume Analysis & Job Matching Platform.

A Python package for analyzing resumes and matching them with job descriptions
using natural language processing and semantic analysis.
"""

__version__ = "0.1.0"
__author__ = "Anshuman Nanda"
__email__ = "anshuman.nanda@example.com"

from resumematch.core import ResumeAnalyzer
from resumematch.matcher import ResumeMatcher
from resumematch.parser import ResumeParser

__all__ = [
    "ResumeAnalyzer",
    "ResumeMatcher",
    "ResumeParser",
]
