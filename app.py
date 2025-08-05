# research-assistant/app.py

import streamlit as st
from components import document_loader, text_chunker, embedding_store, summarizer, qa_engine

st.set_page_config(page_title="LLM Research Assistant", layout="wide")
st.title("📚 LLM-Powered Research Assistant")

# Sidebar inputs
st.sidebar.header("Upload or Input")
uploaded_file = st.sidebar.file_uploader("Upload a PDF", type=["pdf"])
url_input = st.sidebar.text_input("Or enter a URL to summarize")

# Process input
if uploaded_file or url_input:
    with st.spinner("Loading and processing document..."):
        if uploaded_file:
            text = document_loader.load_pdf(uploaded_file)
        else:
            text = document_loader.load_url(url_input)

        chunks = text_chunker.chunk_text(text)
        embedding_store.create_vector_store(chunks)

    st.success("Document loaded and indexed!")

    if st.button("Generate Executive Summary"):
        with st.spinner("Generating summary..."):
            summary = summarizer.generate_summary(chunks)
            st.subheader("Executive Summary")
            st.write(summary)

    user_question = st.text_input("Ask a question about the document")
    if user_question:
        with st.spinner("Searching for answer..."):
            answer = qa_engine.answer_question(user_question)
            st.subheader("Answer")
            st.write(answer)

    if st.button("Suggest Follow-up Reading"):
        with st.spinner("Generating suggestions..."):
            suggestions = summarizer.suggest_reading(chunks)
            st.subheader("Follow-up Reading Suggestions")
            for item in suggestions:
                st.markdown(f"- {item}")
