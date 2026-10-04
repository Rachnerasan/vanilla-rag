import pypdf
import re


class PdfReader:

    def __init__(self, path):
        """
        Initialize the PDF reader with the path to the PDF.
        """
        self.reader = pypdf.PdfReader(path)
        self.pages_text = None

    def extract_text(self):
        """
        Extract text from all PDF pages and normalize whitespace.
        """
        all_pages_text = []

        for page in self.reader.pages:
            page_text = page.extract_text()

            if page_text:
                all_pages_text.append(page_text)

        pdf_text = "\n".join(all_pages_text)

        # 1. Mark paragraph breaks before whitespace normalization
        pdf_text = re.sub(
            r'\n([ \t]*\n)?[ \t]{2,}',
            '¶',
            pdf_text
        )

        # 2. Collapse multiple spaces
        pdf_text = re.sub(r' +', ' ', pdf_text)

        # 3. Convert word-wrap newlines into spaces
        pdf_text = re.sub(
            r'[ \t]*\n[ \t]*',
            ' ',
            pdf_text
        )

        # 4. Restore paragraph breaks
        pdf_text = pdf_text.replace('¶', '\n')

        # 5. Final whitespace cleanup
        pdf_text = re.sub(r' +', ' ', pdf_text).strip()

        print(
            f"Successfully extracted text. "
            f"Total characters: {len(pdf_text)}"
        )

        self.pages_text = pdf_text

        return pdf_text

    def get_text_slice(self, start=0, end=None):
        """
        Return a portion of the extracted text.

        start and end refer to character positions.
        """
        if self.pages_text is None:
            self.extract_text()

        return self.pages_text[start:end]

    def get_paragraphs(self):
        """
        Return the extracted text as a list of paragraphs.
        """
        if self.pages_text is None:
            self.extract_text()

        return [
            paragraph.strip()
            for paragraph in self.pages_text.split('\n')
            if paragraph.strip()
        ]

    def get_chunks(self):
        """
        Return the extracted text as a list of chunks using a sliding window.
        """
        from app.ingestion.chunker import TextChunker
        if self.pages_text is None:
            self.extract_text()
            
        chunker = TextChunker()
        return chunker.chunk_text(self.pages_text)


# Example usage
# pdf_reader = PdfReader(
#     path="./data/raw/pdfs/2025-q1-earnings-transcript.pdf"
# )
#
# pdf_reader.extract_text()
#
# print(
#     pdf_reader.get_text_slice(end=10000)
# )
#
# print(
#     pdf_reader.get_paragraphs()[:3]
# )
