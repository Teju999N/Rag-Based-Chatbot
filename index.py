from modules.ingest import extract_text_from_folder
from modules.preprocess import create_chunks
from modules.vector_store import create_vector_database

print("Starting document indexing...")

pages = extract_text_from_folder("data/pdfs")
print(f"Extracted {len(pages)} pages.")

chunks = create_chunks(pages)
print(f"Created {len(chunks)} chunks.")

create_vector_database(chunks)

print("Knowledge Base Created Successfully!")
