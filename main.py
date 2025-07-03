# cv_reviewer.py
import os
import streamlit as st
import PyPDF2
import docx2txt
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# 2. Helper to extract text
def extract_text(uploaded_file):
    fname = uploaded_file.name.lower()
    if fname.endswith(".pdf"):
        pdf = PyPDF2.PdfReader(uploaded_file)
        return "\n".join(page.extract_text() or "" for page in pdf.pages)
    elif fname.endswith(".docx"):
        return docx2txt.process(uploaded_file)
    else:
        return str(uploaded_file.read(), errors="ignore")

# 3. Build the prompt
def build_prompt(cv_text, tone, focus):
    return (
        f"You are an expert career coach. Review this CV and give feedback "
        f"with a {tone} tone, focusing on {focus}. "
        f"Provide numbered points and suggestions for improvement.\n\n"
        f"===== CV START =====\n{cv_text}\n===== CV END ====="
    )

# 4. Call Gemini
def review_cv(prompt):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text

# 5. Streamlit app
def main():
    st.title("🤖 CV Reviewer")
    st.write("Upload your CV and get AI-powered feedback instantly.")

    uploaded = st.file_uploader("Upload CV (PDF or DOCX)", type=["pdf", "docx", "txt"])
    tone = st.selectbox("Tone", ["Professional", "Friendly", "Direct"])
    focus = st.multiselect("Focus areas", ["Grammar", "Formatting", "Keyword Optimization", "Overall Impact"], default=["Grammar"])

    if uploaded:
        with st.spinner("Extracting text…"):
            cv_text = extract_text(uploaded)
        if st.button("Review my CV"):
            prompt = build_prompt(cv_text, tone.lower(), ", ".join(focus).lower())
            with st.spinner("Generating feedback…"):
                feedback = review_cv(prompt)
            st.subheader("AI Feedback")
            st.markdown(feedback)

if __name__ == "__main__":
    main()
