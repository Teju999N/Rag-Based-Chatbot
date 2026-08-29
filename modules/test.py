from modules.ingest import extract_text_from_pdf

pages = extract_text_from_pdf("data/pdfs/rag.pdf")

print("Total Pages:", len(pages))
print("\nFirst 500 characters:\n")
print(pages[0]["text"][:500])