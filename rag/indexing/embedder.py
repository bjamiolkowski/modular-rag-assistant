"""
Generates normalized embeddings. The default provider uses local Ollama embeddings.
"""

from __future__ import annotations

import faiss
import numpy as np

from langchain_ollama import OllamaEmbeddings

from rag.config import EMBED_MODEL, OLLAMA_BASE_URL


def _get_embedding_model() -> OllamaEmbeddings:
    """Create the LangChain Ollama embedding model."""
    return OllamaEmbeddings(
        model=EMBED_MODEL,
        base_url=OLLAMA_BASE_URL,
    )


def embed_text(text: str) -> np.ndarray:
    """
    Generate a normalized embedding for a single text.
    """
    if not text.strip():
        return np.zeros((1, 1), dtype="float32")

    embedding_model = _get_embedding_model()
    vector = embedding_model.embed_query(text)

    vec = np.array([vector], dtype="float32")
    faiss.normalize_L2(vec)

    return vec


def build_embeddings(chunks: list[dict]) -> np.ndarray:
    """
    Generate normalized embeddings for document chunks.
    """
    texts = [
        chunk.get("text", "").strip()
        for chunk in chunks
        if chunk.get("text", "").strip()
    ]

    if not texts:
        return np.empty((0, 0), dtype="float32")

    embedding_model = _get_embedding_model()

    vectors = []
    for text in texts:
        vector = embedding_model.embed_query(text)
        vectors.append(vector)

    embeddings = np.array(vectors, dtype="float32")
    faiss.normalize_L2(embeddings)

    return embeddings