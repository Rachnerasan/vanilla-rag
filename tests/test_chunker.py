from app.ingestion.chunker import TextChunker

def test_text_chunker_exact_size():
    # 10 words total
    text = "one two three four five six seven eight nine ten"
    
    # Chunk size 5, overlap 2
    # Chunk 1: one two three four five (start=0, end=5) -> next start = 5 - 2 = 3
    # Chunk 2: four five six seven eight (start=3, end=8) -> next start = 8 - 2 = 6
    # Chunk 3: seven eight nine ten (start=6, end=11, stops at 10)
    
    chunker = TextChunker(chunk_size=5, chunk_overlap=2)
    chunks = chunker.chunk_text(text)
    
    assert len(chunks) == 3
    assert chunks[0] == "one two three four five"
    assert chunks[1] == "four five six seven eight"
    assert chunks[2] == "seven eight nine ten"

def test_text_chunker_empty():
    chunker = TextChunker(chunk_size=5, chunk_overlap=2)
    assert chunker.chunk_text("") == []

def test_text_chunker_no_overlap():
    text = "one two three four"
    chunker = TextChunker(chunk_size=2, chunk_overlap=0)
    chunks = chunker.chunk_text(text)
    
    assert len(chunks) == 2
    assert chunks[0] == "one two"
    assert chunks[1] == "three four"
