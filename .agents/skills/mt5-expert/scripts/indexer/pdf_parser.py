import pypdf
import os
import re
from scripts.config import PDF_PATH

def extract_page_text(page):
    """Extract clean text snippet from a PyPDF page object."""
    try:
        text = page.extract_text()
        if text:
            # Clean non-printable characters and extra whitespace
            clean = re.sub(r'\s+', ' ', text).strip()
            return clean
    except Exception:
        pass
    return ""

def parse_pdf_document(pdf_file=PDF_PATH, max_pages=None):
    """Iterate through pages of mql5.pdf and yield (page_num, title, text)."""
    if not os.path.exists(pdf_file):
        raise FileNotFoundError(f"MQL5 PDF file not found at: {pdf_file}")
    
    reader = pypdf.PdfReader(pdf_file)
    total_pages = len(reader.pages)
    limit = max_pages if max_pages is not None else total_pages
    
    for idx in range(min(total_pages, limit)):
        page_num = idx + 1
        page = reader.pages[idx]
        text = extract_page_text(page)
        
        # Derive page title from first line if available
        title = text.split('.')[0][:100] if text else f"Page {page_num}"
        
        yield {
            "page_number": page_num,
            "title": title,
            "text": text
        }
