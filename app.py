import streamlit as st

st.title("📄 ResumeGPT: AI-Powered Resume & Cover Letter Generator")

st.write("Upload your resume and paste the job description below to generate a tailored cover letter.")

resume_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])

job_description = st.text_area("Paste the Job Description Here")

name = st.text_input("Your Full Name")
target_role = st.text_input("Job Title You're Applying For")

if st.button("Generate Cover Letter"):
    if resume_file and job_description:
        st.success("✔️ Generating your cover letter... (AI functionality coming soon!)")
    else:
        st.warning("⚠️ Please upload your resume and paste a job description.")
