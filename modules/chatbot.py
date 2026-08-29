import ollama
from modules.config import LLM_MODEL
from modules.retriever import retrieve_documents


def ask_chatbot(question):
    """
    Retrieve relevant context and generate an answer.
    """

    results = retrieve_documents(question)

    context = ""

    for doc in results["documents"][0]:
        context += doc + "\n\n"

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the context below.
If the answer is not present, say:
"I couldn't find the answer in the provided documents."

Context:
{context}

Question:
{question}
"""

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    unique_sources = []
    seen = set()

    for source in results["metadatas"][0]:
        key = (source["filename"], source["page"])

        if key not in seen:
            seen.add(key)
            unique_sources.append(source)

    return answer, unique_sources