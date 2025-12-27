"""File handling utilities."""

from pathlib import Path
from typing import Optional


def validate_file_path(file_path: str) -> Path:
    """
    Validate that a file path exists and is a file.
    
    Args:
        file_path: Path to validate.
    
    Returns:
        Path object if valid.
    
    Raises:
        FileNotFoundError: If the file doesn't exist.
        ValueError: If the path is not a file.
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    
    return path


def get_file_extension(file_path: str) -> str:
    """
    Get the file extension from a file path.
    
    Args:
        file_path: Path to the file.
    
    Returns:
        File extension (lowercase, including the dot).
    """
    return Path(file_path).suffix.lower()


def get_file_size(file_path: str) -> int:
    """
    Get the size of a file in bytes.
    
    Args:
        file_path: Path to the file.
    
    Returns:
        File size in bytes.
    
    Raises:
        FileNotFoundError: If the file doesn't exist.
    """
    path = validate_file_path(file_path)
    return path.stat().st_size
