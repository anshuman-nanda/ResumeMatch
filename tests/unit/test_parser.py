"""Test cases for the ResumeParser class."""

import pytest
from pathlib import Path
from resumematch import ResumeParser


def test_resume_parser_initialization():
    """Test that ResumeParser can be initialized."""
    parser = ResumeParser()
    assert parser is not None


def test_supported_formats():
    """Test that supported formats are correctly defined."""
    parser = ResumeParser()
    expected_formats = ['.pdf', '.docx', '.txt', '.rtf']
    assert parser.SUPPORTED_FORMATS == expected_formats


def test_is_supported_format():
    """Test is_supported_format method."""
    parser = ResumeParser()
    
    # Test supported formats
    assert parser.is_supported_format("resume.pdf") is True
    assert parser.is_supported_format("resume.docx") is True
    assert parser.is_supported_format("resume.txt") is True
    assert parser.is_supported_format("resume.rtf") is True
    
    # Test unsupported formats
    assert parser.is_supported_format("resume.doc") is False
    assert parser.is_supported_format("resume.html") is False


def test_parse_nonexistent_file():
    """Test that parse raises FileNotFoundError for nonexistent files."""
    parser = ResumeParser()
    
    with pytest.raises(FileNotFoundError):
        parser.parse("nonexistent_file.pdf")


def test_parse_unsupported_format(tmp_path):
    """Test that parse raises ValueError for unsupported formats."""
    parser = ResumeParser()
    
    # Create a temporary file with unsupported format
    test_file = tmp_path / "test.html"
    test_file.write_text("Test content")
    
    with pytest.raises(ValueError):
        parser.parse(str(test_file))
