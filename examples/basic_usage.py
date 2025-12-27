"""
Example: Basic usage of ResumeMatch package.

This script demonstrates how to use the ResumeMatch package to analyze
a resume and match it against a job description.
"""

from resumematch import ResumeAnalyzer, ResumeParser, ResumeMatcher


def main():
    """Main function demonstrating basic package usage."""
    print("=" * 60)
    print("ResumeMatch - Basic Usage Example")
    print("=" * 60)
    print()
    
    # 1. Initialize components
    print("1. Initializing ResumeMatch components...")
    parser = ResumeParser()
    matcher = ResumeMatcher()
    analyzer = ResumeAnalyzer()
    print(f"   ✓ Using ResumeMatch version: {analyzer.get_version()}")
    print()
    
    # 2. Check supported formats
    print("2. Supported file formats:")
    for fmt in parser.SUPPORTED_FORMATS:
        print(f"   - {fmt}")
    print()
    
    # 3. Example: Parse a resume (placeholder)
    print("3. Example workflow:")
    print("   a) Parse resume file")
    print("      parser.parse('path/to/resume.pdf')")
    print()
    print("   b) Parse job description")
    print("      job_description = 'Your job description text...'")
    print()
    print("   c) Match resume with job description")
    print("      matcher.match(resume_data, job_description)")
    print()
    print("   d) Get comprehensive analysis")
    print("      analyzer.analyze('path/to/resume.pdf', job_description)")
    print()
    
    # 4. Show expected output structure
    print("4. Expected output structure:")
    sample_output = {
        "overall_score": 85.5,
        "keywords": ["Python", "Machine Learning", "Data Analysis"],
        "recommendations": [
            "Add more quantified achievements",
            "Include specific project outcomes"
        ],
        "ats_score": 92.0
    }
    print("   {")
    for key, value in sample_output.items():
        print(f"      '{key}': {value},")
    print("   }")
    print()
    
    print("=" * 60)
    print("For more examples, see the documentation:")
    print("https://github.com/anshuman-nanda/ResumeMatch/wiki")
    print("=" * 60)


if __name__ == "__main__":
    main()
