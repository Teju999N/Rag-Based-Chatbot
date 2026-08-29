import ollama
from modules.config import EMBEDDING_MODEL


def create_embedding(text):
    """
    Generate embedding for a single text chunk.
    """

    response = ollama.embed(
        model=EMBEDDING_MODEL,
        input=text
    )

    return response["embeddings"][0]