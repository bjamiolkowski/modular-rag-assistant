<p align="center">
  <img src="assets/logo.png" width="800">
</p>

<p align="center">
  <b>Build and chat with your private knowledge base using Retrieval-Augmented Generation.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/RAG-Hybrid%20Retrieval-purple">
  <img src="https://img.shields.io/badge/LangChain-Framework-green">
  <img src="https://img.shields.io/badge/FAISS-Vector%20Search-orange">
  <img src="https://img.shields.io/badge/OpenAI-API-black">
  <img src="https://img.shields.io/badge/Ollama-Local%20LLM-lightgrey">
  <img src="https://img.shields.io/badge/Streamlit-App-red">
  <img src="https://img.shields.io/badge/Docker-Containerized-blue">
</p>

---

## What is Parrotly?

Parrotly is a modular AI application that allows users to create a private knowledge base from their own documents and interact with it using natural language.

The system focuses on building a reliable Retrieval-Augmented Generation pipeline with hybrid retrieval, reranking, evaluation, and support for both cloud-based and local LLM providers.

---

## Capabilities

Parrotly allows users to:

- Upload PDF and TXT documents
- Build a searchable private knowledge base
- Ask questions grounded in document context
- Generate document summaries
- Inspect retrieved sources used for answers
- Compare different retrieval configurations
- Monitor token usage, latency and estimated costs
- Switch between OpenAI and local models using Ollama

---

## Demo

### Main application view

<p align="center">
  <img src="assets/main_ui.jpg" width="850">
</p>


### Query and source inspection

<p align="center">
  <img src="assets/usage_details.jpg" width="850">
</p>

---

## Key Features

### Document Processing

- PDF and TXT document ingestion
- Text splitting with metadata preservation
- Document parsing and preprocessing pipeline


### Retrieval Pipeline

- Dense retrieval using FAISS vector search and embeddings
- Sparse retrieval using TF-IDF keyword search
- Hybrid retrieval combining semantic similarity and keyword matching
- Post-retrieval reranking based on relevance scoring


### LLM Integration

- Cloud-based generation using OpenAI models
- Local model execution through Ollama
- Context-grounded response generation
- Token usage and cost tracking


### Evaluation & Monitoring

- Automated retrieval evaluation pipeline
- Experiment comparison across retrieval configurations
- Token usage, cost and latency monitoring

---

## Evaluation

A key part of Parrotly is an experiment-driven approach to improving retrieval quality.

Instead of relying on a single retrieval method, the system includes an evaluation framework for benchmarking different configurations and selecting the most effective setup.

The evaluation compares:

- Dense semantic retrieval using vector search
- Sparse retrieval using TF-IDF keyword search
- Hybrid retrieval combining both approaches
- Different retrieval parameters and Top-K configurations


Performance is measured using:

- Top-K Accuracy
- Hit Rate
- Mean Reciprocal Rank (MRR)
- Recall@K
- Retrieval latency


### Results

Hybrid retrieval achieved the best overall ranking performance by combining semantic understanding with exact keyword matching.

| Retrieval Strategy | Top-1 Accuracy | Top-5 Hit Rate | MRR | Recall@5 |
|---|---:|---:|---:|---:|
| Dense Search | 0.90 | 1.00 | 0.92 | 1.00 |
| TF-IDF Search | 0.80 | 1.00 | 0.85 | 1.00 |
| Hybrid Search | **0.90** | **1.00** | **0.95** | **1.00** |

The results showed that hybrid retrieval improved ranking quality while maintaining full source recall.

Detailed experiment outputs are exported automatically:

```text
evaluation/results/retrieval_comparison.csv
evaluation/results/retrieval_details.json
```

---

## Tech Stack

### AI & Retrieval

- LangChain
- FAISS
- OpenAI API
- Ollama
- TF-IDF retrieval


### Application

- Python
- Streamlit
- Pydantic


### Data Processing

- NumPy
- Pandas
- Scikit-learn


### Infrastructure

- Docker
- Docker Compose

---

## Running Locally

### Clone repository

```bash
git clone https://github.com/bjamiolkowski/modular-rag-assistant.git

cd modular-rag-assistant
```


### Create virtual environment

```bash
python -m venv .venv

source .venv/bin/activate
```


Windows:

```bash
.venv\Scripts\activate
```


### Install dependencies

```bash
pip install -r requirements.txt
```


### Configure environment variables

Create `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

Optional local model configuration:

```env
OLLAMA_MODEL=llama3
```


### Run application

```bash
streamlit run app.py
```


Application will be available at:

```text
http://localhost:8501
```

---

## Docker

Build and run:

```bash
docker compose up --build
```

---

## License

MIT License