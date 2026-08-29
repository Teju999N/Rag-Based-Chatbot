import chromadb
from modules.embeddings import create_embedding
from modules.config import TOP_K

# Connect to existing ChromaDB
client = chromadb.PersistentClient(path="vector_db")

collection = client.get_collection("rag_collection")


def retrieve_documents(query):
    """
    Retrieve the most relevant chunks for a user query.
    """

    query_embedding = create_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=TOP_K
    )

    return results