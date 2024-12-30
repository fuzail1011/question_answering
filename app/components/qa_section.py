import streamlit as st
from app.pipeline.question_answering_pipeline import answer_question


def qa_section(file_content):
    """
    Handles the question input and shows the answer
    """
    question = st.text_input("Enter your question:")

    if st.button("Extract Answer"):
        if question:
            with st.spinner("Processing..."):
                # Get the answer based on the extracted content
                answer = answer_question(
                    file_content,
                    question,
                )
                st.subheader("Answer")
                st.write(answer)
        else:
            st.warning("Please enter a question.")
