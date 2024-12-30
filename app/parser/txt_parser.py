def extract_text_from_txt(file) -> str:
    """
    Reads text content from a TXT file
    """
    return file.read().decode("utf-8")
