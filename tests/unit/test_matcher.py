"""Test cases for the ResumeMatcher class."""

import pytest
from resumematch import ResumeMatcher


def test_resume_matcher_initialization():
    """Test that ResumeMatcher can be initialized."""
    matcher = ResumeMatcher()
    assert matcher is not None


def test_match_returns_dict():
    """Test that match method returns a dictionary with expected keys."""
    matcher = ResumeMatcher()
    resume_data = {
        "contact_info": {},
        "work_experience": [],
        "education": [],
        "skills": [],
        "certifications": [],
        "raw_text": "Sample resume text",
    }
    job_description = "Sample job description"
    
    result = matcher.match(resume_data, job_description)
    
    assert isinstance(result, dict)
    assert "overall_score" in result
    assert "keyword_matches" in result
    assert "missing_keywords" in result
    assert "skill_score" in result
    assert "experience_score" in result
    assert "recommendations" in result


def test_calculate_ats_score():
    """Test that calculate_ats_score returns a float."""
    matcher = ResumeMatcher()
    resume_data = {"raw_text": "Sample resume"}
    
    score = matcher.calculate_ats_score(resume_data)
    
    assert isinstance(score, float)
    assert 0 <= score <= 100


def test_extract_keywords():
    """Test that extract_keywords returns a list."""
    matcher = ResumeMatcher()
    text = "Python developer with expertise in machine learning"
    
    keywords = matcher.extract_keywords(text)
    
    assert isinstance(keywords, list)
