from transformers import pipeline
from app.configs.constants import MODEL_NAME

# Initialize the question answering pipeline with the specified model
qa_pipeline = pipeline(
    "question-answering",
    model=MODEL_NAME,
)


def answer_question(paragraph, question):
    """
    Get answer from the context using the QA model
    """
    answer = qa_pipeline(
        context=paragraph,
        question=question,
    )
    return answer["answer"] if "answer" in answer else "No answer found"
