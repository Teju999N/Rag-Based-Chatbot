import os
import fitz  # PyMuPDF
# text extraction from scanned PDFs
import pytesseract # OCR(optical character recognition) # it will extract the text which are inside images in the PDF.
from PIL import Image
from modules.config import TESSERACT_PATH

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def extract_text_from_pdf(pdf_path):
    """
    Extract text from a single PDF.
    If a page has no text, use OCR.
    """

    document = fitz.open(pdf_path)

    extracted_pages = []

    filename = os.path.basename(pdf_path)

    for page_number in range(len(document)):

        page = document.load_page(page_number)

        # Try normal text extraction
        text = page.get_text().strip()

        # If page has no text, use OCR
        if not text:

            pix = page.get_pixmap(dpi=300)

            image = Image.frombytes(
                "RGB",
                [pix.width, pix.height],
                pix.samples
            )

            text = pytesseract.image_to_string(image)

        extracted_pages.append({

            "filename": filename,
            "page": page_number + 1,
            "text": text.strip()

        })

    document.close()

    return extracted_pages


def extract_text_from_folder(folder_path):
    """
    Extract text from all PDFs inside a folder.
    """

    all_pages = []

    for file in os.listdir(folder_path):

        if file.lower().endswith(".pdf"):

            pdf_path = os.path.join(folder_path, file)

            print(f"Processing: {file}")

            pages = extract_text_from_pdf(pdf_path)

            all_pages.extend(pages)

    return all_pages