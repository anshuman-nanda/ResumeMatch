"""Test cases for utility functions."""

import pytest
from pathlib import Path
from resumematch.utils import (
    validate_file_path,
    get_file_extension,
    clean_text,
    normalize_whitespace,
)


class TestFileUtils:
    """Test cases for file utility functions."""
    
    def test_validate_file_path_nonexistent(self):
        """Test that validate_file_path raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            validate_file_path("nonexistent_file.txt")
    
    def test_validate_file_path_directory(self, tmp_path):
        """Test that validate_file_path raises ValueError for directories."""
        with pytest.raises(ValueError):
            validate_file_path(str(tmp_path))
    
    def test_validate_file_path_valid(self, tmp_path):
        """Test that validate_file_path returns Path for valid files."""
        test_file = tmp_path / "test.txt"
        test_file.write_text("Test content")
        
        result = validate_file_path(str(test_file))
        assert isinstance(result, Path)
        assert result == test_file
    
    def test_get_file_extension(self):
        """Test get_file_extension function."""
        assert get_file_extension("file.pdf") == ".pdf"
        assert get_file_extension("file.DOCX") == ".docx"
        assert get_file_extension("file.TXT") == ".txt"
        assert get_file_extension("path/to/file.pdf") == ".pdf"


class TestTextUtils:
    """Test cases for text utility functions."""
    
    def test_normalize_whitespace(self):
        """Test normalize_whitespace function."""
        assert normalize_whitespace("  hello   world  ") == "hello world"
        assert normalize_whitespace("hello\n\n\nworld") == "hello world"
        assert normalize_whitespace("hello\t\tworld") == "hello world"
    
    def test_clean_text(self):
        """Test clean_text function."""
        text = "  Hello,   world!  This is a test.  "
        result = clean_text(text)
        assert "  " not in result
        assert result.startswith("Hello")
        assert result.endswith(".")
    
    def test_clean_text_with_special_chars(self):
        """Test clean_text with special characters."""
        text = "Hello @#$% World"
        result = clean_text(text)
        # Special characters should be removed but basic punctuation kept
        assert "@" not in result
        assert "#" not in result
