# app.py

import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AQ.Ab8RN6IA0CLIBVBFgXxBCE5OCp8UIU2YwxwO_vXUz6uxd6CHRg")

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit UI
st.title("🎓 College RAG Assistant")

question = st.text_input("Ask a Question About the College")

if st.button("Ask"):

    # Read college data
    with open("college.txt", "r", encoding="utf-8") as file:
        context = file.read()

    prompt = f"""
You are a College RAG Assistant.

Answer ONLY from the college information provided below.

If the answer is not found in the college information,
reply exactly:

Answer could not be found

College Information:
{context}

Question:
{question}
"""

    response = model.generate_content(prompt)

    st.subheader("Answer")
    st.write(response.text)
