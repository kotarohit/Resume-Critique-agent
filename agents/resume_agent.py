from utils.file_parser import parse_resume
from utils.llm_wrapper import call_openrouter
import os

criteria = [
    "Years of experience",
    "Skill match with job",
    "Communication quality",
    "Certifications",
    "Project relevance"
]

def critique_resume(resume_text, criteria):
    prompt = f"""You're an expert recruiter. Critique this resume based on the following criteria: {criteria}.
    
Resume:
{resume_text}

Give detailed feedback and a score (0-10) for each criterion."""
    
    messages = [
        {"role": "user", "content": prompt}
    ]
    
    return call_openrouter(messages)

def rank_resumes(resume_dir):
    critiques = []
    for filename in os.listdir(resume_dir):
        path = os.path.join(resume_dir, filename)
        resume_text = parse_resume(path)
        critique = critique_resume(resume_text, criteria)
        critiques.append((filename, critique))
    return critiques