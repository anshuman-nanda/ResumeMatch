"""
Example: Using ResumeMatch as a library in your own project.

This example shows how to integrate ResumeMatch into your own
Python application or workflow.
"""

from typing import Dict, Any, List
from resumematch import ResumeAnalyzer, ResumeParser, ResumeMatcher


class JobApplicationProcessor:
    """
    Example class showing how to use ResumeMatch in a larger application.
    
    This could be part of a job application tracking system, a career
    services platform, or any other system that needs resume analysis.
    """
    
    def __init__(self):
        """Initialize the processor with ResumeMatch components."""
        self.parser = ResumeParser()
        self.matcher = ResumeMatcher()
        self.analyzer = ResumeAnalyzer()
    
    def process_application(
        self,
        resume_path: str,
        job_description: str
    ) -> Dict[str, Any]:
        """
        Process a job application by analyzing the resume.
        
        Args:
            resume_path: Path to the applicant's resume.
            job_description: Job description to match against.
        
        Returns:
            Dictionary with analysis results and recommendations.
        """
        # Parse the resume
        resume_data = self.parser.parse(resume_path)
        
        # Match against job description
        match_results = self.matcher.match(resume_data, job_description)
        
        # Get comprehensive analysis
        analysis = self.analyzer.analyze(resume_path, job_description)
        
        # Combine results
        return {
            "resume_data": resume_data,
            "match_results": match_results,
            "analysis": analysis,
            "overall_score": match_results["overall_score"],
            "recommendations": match_results["recommendations"],
        }
    
    def batch_process_applications(
        self,
        resume_paths: List[str],
        job_description: str
    ) -> List[Dict[str, Any]]:
        """
        Process multiple applications for the same job posting.
        
        Args:
            resume_paths: List of paths to resume files.
            job_description: Job description to match against.
        
        Returns:
            List of analysis results, one per resume.
        """
        results = []
        
        for resume_path in resume_paths:
            try:
                result = self.process_application(resume_path, job_description)
                results.append(result)
            except Exception as e:
                print(f"Error processing {resume_path}: {e}")
                results.append({
                    "error": str(e),
                    "resume_path": resume_path,
                })
        
        # Sort by overall score (highest first)
        results.sort(
            key=lambda x: x.get("overall_score", 0),
            reverse=True
        )
        
        return results


def main():
    """Demonstrate using ResumeMatch as a library."""
    print("ResumeMatch - Library Integration Example")
    print("=" * 60)
    print()
    
    # Create an instance of our custom processor
    processor = JobApplicationProcessor()
    
    print("Example 1: Process a single application")
    print("-" * 60)
    print("result = processor.process_application(")
    print("    resume_path='resumes/john_doe.pdf',")
    print("    job_description='We are looking for a Python developer...'")
    print(")")
    print()
    
    print("Example 2: Batch process multiple applications")
    print("-" * 60)
    print("results = processor.batch_process_applications(")
    print("    resume_paths=[")
    print("        'resumes/applicant1.pdf',")
    print("        'resumes/applicant2.pdf',")
    print("        'resumes/applicant3.pdf',")
    print("    ],")
    print("    job_description='Job description text...'")
    print(")")
    print()
    print("# Results are automatically sorted by score")
    print("for result in results:")
    print("    print(f\"Score: {result['overall_score']}\")")
    print()


if __name__ == "__main__":
    main()
