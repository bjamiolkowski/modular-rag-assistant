<p align="center">
  <img src="assets/logo.png" width="850">
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

## What is Parrotly?

Parrotly is a modular AI application that allows users to create a private knowledge base from their own documents and interact with it using natural language.

The system focuses on building a reliable Retrieval-Augmented Generation pipeline with hybrid retrieval, reranking, evaluation, and support for both cloud-based and local LLM providers.

---

## Overview

Parrotly allows users to:

- Upload PDF and TXT documents
- Build a searchable private knowledge base
- Ask questions grounded in document context
- Generate document summaries
- Inspect retrieved sources used for answers
- Compare different retrieval configurations
- Monitor token usage, latency and estimated costs
- Switch between OpenAI and local models using Ollama

## Demo

### Main application view

<p align="center">
  <img src="assets/main_ui.jpg" width="850">
</p>

### Query and source inspection

<p align="center">
  <img src="assets/usage_details.jpg" width="850">
</p>

## Key Features

### Document Processing

- PDF and TXT document ingestion
- Text chunking with metadata preservation
- OCR support for scanned documents

### Retrieval Pipeline

- Dense retrieval using FAISS vector search and embeddings
- Sparse keyword-based retrieval
- Hybrid retrieval combining semantic and keyword search
- Post-retrieval reranking to improve context quality

### LLM Integration

- Cloud-based models using OpenAI API
- Local model support through Ollama
- Context-grounded answer generation
- Token usage and cost tracking

### Evaluation & Monitoring

- Retrieval quality evaluation using Top-K accuracy, MRR and Recall@K
- Comparison of different retrieval configurations
- Latency and usage monitoring

## Architecture

Parrotly uses a modular RAG architecture with separated document processing, retrieval, generation and evaluation components.

<p align="center">
  <img src="assets/architecture.png" width="850">
</p>