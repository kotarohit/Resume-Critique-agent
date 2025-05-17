import os
import streamlit as st
from agents.resume_agent import critique_resume
from utils.file_parser import parse_resume

st.set_page_config(page_title="Resume Critique Agent", layout="wide")
st.title("📄 AI Resume Critique & Ranking")

# File uploader
uploaded_files = st.file_uploader(
    "Upload one or more resumes (PDF or DOCX):", 
    type=["pdf", "docx"], 
    accept_multiple_files=True
)

# Critique criteria
criteria = [
    "Years of experience",
    "Skill match with job",
    "Communication quality",
    "Certifications",
    "Project relevance"
]

# Results container
if uploaded_files:
    st.markdown("### Results")
    for uploaded_file in uploaded_files:
        # Save to temp
        temp_path = f"temp/{uploaded_file.name}"
        os.makedirs("temp", exist_ok=True)
        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        try:
            resume_text = parse_resume(temp_path)
            feedback = critique_resume(resume_text, criteria)
            with st.expander(f"📝 {uploaded_file.name}"):
                st.markdown(f"**Critique:**\n\n```\n{feedback}\n```")
        except Exception as e:
            st.error(f"❌ Failed to parse {uploaded_file.name}: {e}")