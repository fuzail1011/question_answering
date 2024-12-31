from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_document(
    text,
    chunk_size=600,
    chunk_overlap=50,
):
    """
    Split the document into chunks with overlap for better context retrieval.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    chunks = text_splitter.split_text(text)
    return chunks
