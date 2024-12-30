import streamlit as st
from app.components.file_uploader import file_uploader
from app.components.qa_section import qa_section
from app.parser.main_extractor import TextExtractor


def main():
    st.set_page_config(page_title="Question Answering App")
    st.title("Question Answering from Documents")

    # Upload file
    uploaded_file = file_uploader()

    if uploaded_file:
        # Extract text from the uploaded file
        text_extractor = TextExtractor()
        file_content = text_extractor.read_file(
            uploaded_file,
            uploaded_file.name,
        )

        # Question answering section
        qa_section(file_content)


if __name__ == "__main__":
    main()
