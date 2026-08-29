# RAG-Based Document Q&A Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that allows users to ask questions about a collection of PDF documents and receive context-aware answers with document source information.

## Project Overview

This project implements a Dense Retrieval-based RAG pipeline.

A collection of 11 PDF documents containing AI, Machine Learning, Python, NLP, LangChain, and related technical content is processed, chunked, converted into embeddings, and stored in a vector database.

When a user asks a question, the system retrieves the most relevant document chunks and provides them as context to Llama 3.2, which generates the final answer.

## Architecture

                    OFFLINE / INDEXING

              PDF Documents (11 PDFs)
                       |
                       v
                 Text Extraction
                PyMuPDF / Tesseract
                       |
                       v
                    Chunking
          RecursiveCharacterTextSplitter
                       |
                       v
                  BGE-M3
              Embedding Model
                       |
                       v
                   ChromaDB
                 Vector Database


                    ONLINE / QUERY

                  User Question
                       |
                       v
                  BGE-M3
              Query Embedding
                       |
                       v
              ChromaDB Retrieval
                  Top 5 Chunks
                       |
                       v
              Context + Question
                       |
                       v
                  Llama 3.2
                    Ollama
                       |
                       v
                  Final Answer
                       |
                       v
                 Streamlit UI
## Key Features
Processed 11 PDF documents.
Extracted content from 1,146 pages.
Created 2,720 searchable text chunks.
Generated 1024-dimensional embeddings using BGE-M3.
Stored document embeddings and metadata in ChromaDB.
Performs dense vector similarity retrieval.
Retrieves the Top-5 relevant chunks for a user query.
Uses Llama 3.2 locally through Ollama for answer generation.
Displays document filename and page information as sources.
Provides a simple interactive interface using Streamlit.
Supports local execution without depending on external cloud LLM APIs.

## Tech Stack
* Python
* Streamlit
* PyMuPDF
* Tesseract OCR
* LangChain Text Splitters
* BGE-M3
* ChromaDB
* Ollama
* Llama 3.2

## RAG Pipeline
1. Document Processing

PDF files are loaded and their text is extracted.
For scanned or image-based content, OCR can be used through Tesseract.

2. Text Chunking

Large documents are divided into smaller chunks using:
RecursiveCharacterTextSplitter
Chunk overlap is used to preserve context between adjacent chunks.

3. Embedding Generation

Each text chunk is converted into a numerical vector using the BGE-M3 embedding model.
The generated embeddings have 1024 dimensions.

4. Vector Storage

The embeddings are stored in ChromaDB along with:
Original text
Filename
Page number
Document metadata

5. Retrieval

When a user enters a question:
The question is converted into an embedding.
ChromaDB performs vector similarity search.
The Top-5 most relevant chunks are retrieved.

6. Answer Generation

The retrieved chunks are provided as context to Llama 3.2.
The model generates an answer based on the retrieved information.

7. User Interface

Streamlit provides a browser-based interface where users can enter questions and view:
Generated answer
Retrieved document sources
Page numbers
