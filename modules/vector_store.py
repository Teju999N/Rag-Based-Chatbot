import chromadb
from modules.embeddings import create_embedding

def create_vector_database(chunks):
    """
    Create and populate a ChromaDB collection.
    """

    # Create persistent database
    client = chromadb.PersistentClient(path="vector_db")

    # Delete existing collection if it exists
    try:
        client.delete_collection("rag_collection")
    except:
        pass

    # Create new collection
    collection = client.create_collection("rag_collection")

    # Add all chunks
    for i, chunk in enumerate(chunks):

        embedding = create_embedding(chunk["text"])

        collection.add(
            ids=[str(i)],
            embeddings=[embedding],
            documents=[chunk["text"]],
            metadatas=[{
                "filename": chunk["filename"],
                "page": chunk["page"]
            }]
        )

    print(f"\nStored {len(chunks)} chunks in ChromaDB.")

    return collection