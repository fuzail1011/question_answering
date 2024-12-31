from sentence_transformers import SentenceTransformer
from app.vector_store.faiss_vector_store import FAISS_VectorStore

# Initialize the embedder
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize the FAISS vector store
faiss_store = FAISS_VectorStore(dimension=384)


def embed_chunks(chunks):
    """
    Convert chunks into embeddings using SentenceTransformer
    """
    embeddings = embedder.encode(
        chunks,
        convert_to_numpy=True,
    )

    # Add the generated embeddings to the FAISS vector store
    faiss_store.add_texts(
        chunks,
        embeddings,
    )

    return embeddings


def embed_query(query):
    """
    Convert a query into an embedding using SentenceTransformer
    """
    return embedder.encode(
        [query],
        convert_to_numpy=True,
    )
