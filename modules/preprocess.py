from langchain_text_splitters import RecursiveCharacterTextSplitter
from modules.config import CHUNK_SIZE, CHUNK_OVERLAP


def create_chunks(extracted_pages):
    """
    Split extracted text into overlapping chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = []

    for page in extracted_pages:

        text_chunks = splitter.split_text(page["text"])

        for chunk in text_chunks:

            chunks.append({
                "filename": page["filename"],
                "page": page["page"],
                "text": chunk
            })

    return chunks