"""Text processing utilities."""

import re


def clean_text(text: str) -> str:
    """
    Clean text by removing extra whitespace and special characters.
    
    Args:
        text: Input text to clean.
    
    Returns:
        Cleaned text.
    """
    # Remove extra whitespace
    text = normalize_whitespace(text)
    
    # Remove special characters but keep punctuation
    text = re.sub(r'[^\w\s\.\,\-\(\)\:\;]', '', text)
    
    return text.strip()


def normalize_whitespace(text: str) -> str:
    """
    Normalize whitespace in text (convert multiple spaces to single space).
    
    Args:
        text: Input text.
    
    Returns:
        Text with normalized whitespace.
    """
    # Replace multiple whitespace with single space
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length.
    
    Args:
        text: Input text.
        max_length: Maximum length of the output text.
        suffix: Suffix to add if text is truncated (default: "...").
    
    Returns:
        Truncated text.
    """
    if len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)] + suffix
