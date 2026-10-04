import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Hugging Face Authentication
HF_TOKEN = os.getenv("HF_TOKEN", "")

# LLM Settings
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "Qwen/Qwen2.5-3B-Instruct")
LLM_MAX_NEW_TOKENS = int(os.getenv("LLM_MAX_NEW_TOKENS", "1000"))

# Embedding Settings
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "sentence-transformers/all-MiniLM-L6-v2")
DISTANCE_METRIC = os.getenv("DISTANCE_METRIC", "cosine")
