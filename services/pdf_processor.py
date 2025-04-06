import hashlib
import io
import re
from typing import List
import requests
import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter

class PDFProcessor:
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
    
    def extract_text(self, pdf_url: str) -> str:
        """Extract text from PDF URL"""
        try:
            response = requests.get(pdf_url)
            response.raise_for_status()
            
            with io.BytesIO(response.content) as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                return "\n".join([page.extract_text() for page in reader.pages])
        except Exception as e:
            print(f"Error processing PDF: {e}")
            return ""
    
    def clean_and_chunk(self, text: str) -> List[str]:
        """Clean and chunk PDF text"""
        cleaned = re.sub(r'\s+', ' ', text).strip()
        return self.splitter.split_text(cleaned)
    
    # Add this method to the PDFProcessor class
    def generate_pdf_id(self, pdf_url: str, chunk_index: int) -> str:
        """Generate unique ID for PDF chunks"""
        return hashlib.md5(f"{pdf_url}_{chunk_index}".encode()).hexdigest()