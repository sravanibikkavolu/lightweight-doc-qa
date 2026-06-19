import os
import streamlit as st

from extractor import extract_pdf
from retrieval import split_sections
from retrieval import find_section
from qa import answer_question

st.title("📄 Local Document Q&A")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    os.makedirs("documents", exist_ok=True)
    os.makedirs("sections", exist_ok=True)

    pdf_path = "documents/file.pdf"

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    markdown = extract_pdf(pdf_path)

    sections = split_sections(markdown)

    question = st.text_input(
        "Ask a Question"
    )

    if question:

        context = find_section(
            question,
            sections
        )

        answer = answer_question(
            question,
            context
        )

        st.subheader("Answer")

        st.write(answer)