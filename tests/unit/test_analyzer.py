"""Test cases for the ResumeAnalyzer class."""

import pytest
from resumematch import ResumeAnalyzer


def test_resume_analyzer_initialization():
    """Test that ResumeAnalyzer can be initialized."""
    analyzer = ResumeAnalyzer()
    assert analyzer is not None
    assert analyzer.config == {}


def test_resume_analyzer_with_config():
    """Test that ResumeAnalyzer can be initialized with config."""
    config = {"setting": "value"}
    analyzer = ResumeAnalyzer(config=config)
    assert analyzer.config == config


def test_analyze_returns_dict():
    """Test that analyze method returns a dictionary."""
    analyzer = ResumeAnalyzer()
    # Note: This is a placeholder test. In a real implementation,
    # we would need to create a test resume file.
    result = analyzer.analyze("test_resume.pdf")
    assert isinstance(result, dict)
    assert "overall_score" in result
    assert "keywords" in result
    assert "recommendations" in result
    assert "ats_score" in result


def test_get_version():
    """Test that get_version returns the correct version."""
    analyzer = ResumeAnalyzer()
    version = analyzer.get_version()
    assert version == "0.1.0"
