import streamlit as st


def file_uploader():
    """
    Displays file uploader widget and returns the uploaded file
    """
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=[
            "pdf",
            "docx",
            "xlsx",
            "txt",
        ],
    )
    return uploaded_file
