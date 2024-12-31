import faiss
import numpy as np


class FAISS_VectorStore:
    def __init__(
        self,
        dimension=384,
    ):
        """
        Initialize the FAISS index for storing embeddings.
        """
        self.index = faiss.IndexFlatL2(dimension)  # L2 distance for similarity search
        self.embeddings = []
        self.texts = []

    def add_texts(
        self,
        texts,
        embeddings,
    ):
        """
        Add text and its corresponding embeddings to the FAISS index.
        """
        self.texts.extend(texts)
        self.embeddings.extend(embeddings)
        embeddings_np = np.array(embeddings).astype("float32")
        self.index.add(embeddings_np)

    def search(
        self,
        query_embedding,
        k=5,
    ):
        """
        Search for the top k most similar texts to the query embedding.
        """
        query_embedding = np.array(query_embedding).reshape(1, -1).astype("float32")
        distances, indices = self.index.search(
            query_embedding,
            k,
        )
        return [self.texts[i] for i in indices[0]]
