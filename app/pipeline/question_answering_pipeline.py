from app.vector_store.faiss_vector_store import FAISS_VectorStore
from app.embed.generate_embeddings import (
    embed_chunks,
    embed_query,
)
from app.chunking.chunk import chunk_document
from transformers import pipeline
from app.configs.constants import MODEL_NAME

# Initialize the question answering pipeline with the specified model
qa_pipeline = pipeline(
    "question-answering",
    model=MODEL_NAME,
    max_answer_length=100,
)

# Initialize your FAISS vector store
faiss_store = FAISS_VectorStore(dimension=384)


def answer_question(
    context,
    question,
):
    """
    Get the answer by performing retrieval and answering with the context.
    """
    # Step 1: Embed the query
    query_embedding = embed_query(question)

    # Step 2: Retrieve relevant chunks using the FAISS index
    chunks = chunk_document(context)
    chunks_embedding = embed_chunks(chunks)

    # Store the chunks and embeddings in FAISS
    faiss_store.add_texts(
        chunks,
        chunks_embedding,
    )

    # Perform similarity search with the query embedding
    relevant_chunks = faiss_store.search(
        query_embedding,
        k=10,
    )

    # Step 3: Concatenate relevant chunks to form the context
    context = " ".join([chunk.strip() for chunk in relevant_chunks if chunk.strip()])

    # Step 4: Pass the context and question to the QA model
    answer = qa_pipeline(
        context=context,
        question=question,
        max_answer_length=100,
    )
    return answer["answer"] if "answer" in answer else "No answer found"
