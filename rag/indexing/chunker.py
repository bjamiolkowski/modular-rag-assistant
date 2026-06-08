"""
Splits loaded documents into retrieval-ready chunks.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter


DEFAULT_CHUNK_SIZE = 1000
DEFAULT_CHUNK_OVERLAP = 200


def chunk_documents(
    documents: list[dict],
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
) -> list[dict]:
    """
    Split documents into chunked units with metadata.

    Keeps the project's internal chunk format compatible with
    retrieval, reranking, logging and UI source display.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            "",
        ],
    )

    all_chunks = []

    for document in documents:
        text = document.get("text", "").strip()
        if not text:
            continue

        source = document.get("source", "unknown")
        metadata = document.get("metadata", {})

        chunks = splitter.split_text(text)

        for chunk_id, chunk_text in enumerate(chunks):
            clean_text = chunk_text.strip()

            if not clean_text:
                continue

            all_chunks.append(
                {
                    "source": source,
                    "chunk_id": chunk_id,
                    "text": clean_text,
                    "metadata": {
                        **metadata,
                        "chunk_id": chunk_id,
                    },
                }
            )

    return all_chunks