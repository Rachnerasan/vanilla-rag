class TextChunker:
    def __init__(self, chunk_size=300, chunk_overlap=50):
        """
        A simple sliding-window text chunker based on word count.
        chunk_size: number of words per chunk
        chunk_overlap: number of overlapping words between chunks
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_text(self, text: str) -> list[str]:
        words = text.split()
        chunks = []
        start = 0
        
        if not words:
            return chunks

        while start < len(words):
            end = start + self.chunk_size
            chunk = " ".join(words[start:end])
            chunks.append(chunk)
            
            if end >= len(words):
                break
                
            start += self.chunk_size - self.chunk_overlap
            
        return chunks
