"""
Loads supported files from disk using and converts them into a unified format for indexing.
"""

from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader, TextLoader


def load_txt(file_path: Path) -> list[dict]:
    """Load text content from a TXT file."""
    loader = TextLoader(str(file_path), encoding="utf-8")
    documents = loader.load()

    return [
        {
            "source": file_path.name,
            "text": document.page_content.strip(),
            "metadata": document.metadata,
        }
        for document in documents
        if document.page_content.strip()
    ]


def load_pdf(file_path: Path) -> list[dict]:
    """Load text content from a PDF file."""
    loader = PyPDFLoader(str(file_path))
    documents = loader.load()

    return [
        {
            "source": file_path.name,
            "text": document.page_content.strip(),
            "metadata": document.metadata,
        }
        for document in documents
        if document.page_content.strip()
    ]


def load_documents(data_dir: Path) -> list[dict]:
    """Load all supported documents from a directory."""
    loaded_documents = []

    for file_path in sorted(data_dir.iterdir()):
        if not file_path.is_file():
            continue

        suffix = file_path.suffix.lower()

        if suffix == ".txt":
            documents = load_txt(file_path)
        elif suffix == ".pdf":
            documents = load_pdf(file_path)
        else:
            continue

        loaded_documents.extend(documents)

    return loaded_documents