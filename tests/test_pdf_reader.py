import os
from app.ingestion.pdf_reader import PdfReader

def test_pdf_reader_extraction():
    # Path to the sample PDF in your project
    pdf_path = os.path.join("data", "raw", "pdfs", "2025-q1-earnings-transcript.pdf")
    
    # We only run the assertions if the file exists
    if not os.path.exists(pdf_path):
        return
        
    reader = PdfReader(pdf_path)
    
    # 1. Test raw extraction
    text = reader.extract_text()
    assert text is not None
    assert len(text) > 100  # Should have a reasonable amount of text
    
    # 2. Test chunking integration
    chunks = reader.get_chunks()
    assert len(chunks) > 0
    
    # Ensure no chunk is completely empty
    for chunk in chunks:
        assert len(chunk.strip()) > 0
