from PyPDF2 import PdfReader

def get_text_from_pdfs(pdf_files):
    text = ""
    for pdf_file in pdf_files:
        reader = PdfReader(pdf_file)
            
        for page in reader.pages:
            text += page.extract_text() or ""

        text += "\n\n\n\n\n" # Add some space between different Resume PDF texts so that AI can differenciate between them
    return text.strip()