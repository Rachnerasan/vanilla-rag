# 🧠 RAG From Scratch (Pure Python, Fully Local)

> A fully local, offline Retrieval-Augmented Generation (RAG) system built from first principles. No LangChain, no LlamaIndex, and no external VectorDBs (like Chroma or FAISS).

This project was built to deeply understand the mechanics of RAG by implementing the core components—text extraction, sliding-window chunking, and vector math (cosine similarity)—entirely from scratch using pure Python.

All generation and embedding runs locally on your machine, ensuring 100% data privacy.

## ✨ Features

- **Zero Cloud Dependencies:** Your documents never leave your computer.
- **Custom Vector Store:** Implements exact cosine distance math $O(N)$ without relying on black-box vector databases.
- **Smart Text Chunking:** Custom sliding-window token chunking ensures context is preserved without silently exceeding the embedding model's context window.
- **Live Streaming UI:** A clean, chat-based Streamlit interface that streams the LLM's response token-by-token.
- **Modern Python Tooling:** Environment and dependencies managed by `uv`, with a full `pytest` suite for core math and logic.

## 🏗️ Architecture & Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Document Parsing:** PyMuPDF (`pymupdf4llm`)
- **Embeddings:** `sentence-transformers/all-MiniLM-L6-v2`
- **LLM (Generation):** `Qwen/Qwen2.5-3B-Instruct` (Running locally via Hugging Face `transformers`)
- **Vector Search:** Pure Python standard `math` library
- **Environment Management:** `uv`

## 🚀 Getting Started

### Prerequisites

1. Python 3.12+
2. [uv](https://github.com/astral-sh/uv) installed (`pip install uv`)
3. A Hugging Face account and Access Token (for downloading gated models)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/vanilla-rag.git
   cd vanilla-rag
   ```

2. **Set up the environment with `uv`:**

   ```bash
   uv sync
   ```

3. **Configure Environment Variables:**
   Rename `.env.example` to `.env` and add your Hugging Face token.

   ```bash
   cp .env.example .env
   ```

   _Edit `.env` to include your `HF_TOKEN=hf_...`\_

4. **Run the Application:**
   ```bash
   uv run streamlit run app/main.py
   ```
   _The app will automatically download the necessary models on the first run. This may take a few minutes depending on your internet connection and GPU._

## 🧪 Running Tests

The project includes a suite of unit tests to validate the custom chunking logic and vector math.

```bash
uv run pytest tests/
```

## 📂 Project Structure

```text
.
├── app/
│   ├── main.py                # Streamlit UI & application entry point
│   ├── config.py              # Centralized environment configuration
│   ├── ingestion/
│   │   ├── chunker.py         # Custom sliding-window text chunking
│   │   └── pdf_reader.py      # PyMuPDF text extraction
│   ├── retrieval/
│   │   ├── embeddings.py      # Local MiniLM embedding generation
│   │   └── vector_store.py    # Native Python cosine similarity search
│   └── generation/
│       └── llm.py             # Qwen2.5 initialization & text streaming
├── tests/                     # Pytest suite
├── pyproject.toml             # uv project metadata and dependencies
├── .env.example               # Example environment variables
└── README.md
```

## 🤝 Why build it from scratch?

Modern AI frameworks are fantastic for shipping products quickly, but they often abstract away the actual mechanics of how vectors, embeddings, and context windows interact. By building the vector store and chunking logic manually, this project serves as a transparent, educational look under the hood of modern AI systems.
