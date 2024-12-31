import pdfplumber


def extract_text_from_pdf(file) -> str:
    """
    Reads text content from a PDF file
    """
    text_content = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text_content += page.extract_text()
    return text_content
