# DocuMindV2

A modular Python-based RAG application that allows users to load documents, generate embeddings, search for relevant information, chat with their documents, and generate document summaries using a local LLM through Ollama.

## Overview

DocuMindV2 combines document processing and Retrieval-Augmented Generation into a single pipeline.

The application supports:

* `.txt` documents
* `.csv` documents
* Sliding-window text chunking
* Semantic embeddings using Sentence Transformers
* Vector storage using NumPy
* Cosine similarity search
* Context retrieval
* Prompt construction
* Document summarization
* Question answering over documents
* Local LLM inference using Ollama

The project is designed to run locally so document content does not need to be sent to a cloud AI service during inference.

## Features

### Document Loading

DocuMindV2 uses a modular loader system to select the appropriate loader based on the document type.

Currently supported:

* TXT
* CSV

The loader system uses a Factory-style design to keep document loading separate from the rest of the application.

### Text Chunking

Large documents are divided into smaller overlapping chunks using a sliding-window approach.

This allows the retrieval system to work with smaller sections of the document instead of treating the entire document as one large piece of text.

### Embeddings

Each document chunk is converted into a numerical vector using a Sentence Transformers embedding model.

These vectors represent the semantic meaning of the document chunks and allow the system to perform similarity-based retrieval.

### Vector Store

DocuMindV2 stores:

* Document chunks
* Their corresponding embeddings

The vector store uses NumPy arrays and cosine similarity to compare a user's question against the document embeddings.

### Retrieval

When the user asks a question:

1. The question is converted into an embedding.
2. The question embedding is compared with the stored document embeddings.
3. The most similar chunks are selected.
4. The retrieved chunks are provided as context to the LLM.

### Document Summarization

Users can choose to summarize the document.

The complete set of document chunks is provided to the local LLM, which generates a concise summary containing the most important information.

### Document Chat

Users can also chat with the document.

Instead of sending the entire document to the LLM, DocuMindV2 retrieves the most relevant chunks for the user's question and uses those chunks as context.

This is the RAG workflow implemented by the project.

## Architecture

```text
                         User
                          |
                          v
                    Main Application
                          |
                          v
                     MainLoader
                          |
                          v
                    File Loader
                          |
                          v
                     Document
                          |
                          v
                       Chunking
                          |
                          v
                       Chunks
                          |
                          v
                      Embedding
                          |
                          v
                Document Embeddings
                          |
                          v
                    Vector Store
                          |
                          v
                    User Choice
                     /       \
                    /         \
                   v           v
             Summarization    Chat
                   |            |
                   |            v
                   |        Question Embedding
                   |            |
                   |            v
                   |       Similarity Search
                   |            |
                   |            v
                   |      Relevant Chunks
                   |            |
                   |            v
                   |      Context Builder
                   |            |
                   |            v
                   |      Prompt Builder
                   |            |
                   |            v
                   |         AI Engine
                   |            |
                   +-------> Ollama
                                |
                                v
                              Answer
```

## Project Structure

```text
DocumindV2/
│
├── AI/
│   ├── Engine.py
│   └── __init__.py
│
├── Chunking/
│   ├── chunking.py
│   └── __init__.py
│
├── ContextBuilder/
│   ├── context_builder.py
│   └── __init__.py
│
├── Embeddings/
│   ├── embedding.py
│   └── __init__.py
│
├── FileLoaders/
│   ├── base_loader.py
│   ├── loaders.py
│   ├── main_loader.py
│   └── __init__.py
│
├── Prompt/
│   ├── prompt.py
│   └── __init__.py
│
├── Retreiver/
│   └── retriever.py
│
├── Search/
│   └── Cosine_Similarity.py
│
├── Storage/
│   └── vector_store.py
│
├── exceptions.py
├── main.py
├── requirements.txt
├── .gitignore
└── Readme.md
```

## RAG Pipeline

The main RAG pipeline is:

```text
Document
    ↓
Load
    ↓
Chunk
    ↓
Embed
    ↓
Store
    ↓
User Question
    ↓
Embed Question
    ↓
Cosine Similarity
    ↓
Retrieve Top-K Chunks
    ↓
Build Context
    ↓
Build Prompt
    ↓
Local LLM
    ↓
Answer
```

The important idea is that the LLM does not need to receive the entire document for every question.

Instead, the retrieval system finds the parts of the document that are most relevant to the question.

## Requirements

* Python 3.10+
* Ollama
* A compatible Ollama model
* NumPy
* Sentence Transformers
* Requests

The default LLM configured in `AI/Engine.py` is:

```text
phi3:mini
```

You can change the model through the `AIEngine` configuration.

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd DocumindV2
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Make sure Ollama is installed and running.

Pull the default model:

```bash
ollama pull phi3:mini
```

## Running the Project

Run:

```bash
python main.py
```

The application will ask for the document directory and filename.

Example:

```text
Enter directory path: C:\Documents
Enter file name: history.txt
```

After processing the document, choose:

```text
1. Summarize Document
2. Chat with Document
```

### Summarization

Select:

```text
1
```

DocuMindV2 will send the document chunks to the local LLM and generate a concise summary.

### Document Chat

Select:

```text
2
```

Then enter a question related to the document.

The system will:

```text
Question
   ↓
Question Embedding
   ↓
Similarity Search
   ↓
Relevant Chunks
   ↓
Context
   ↓
Prompt
   ↓
Ollama
   ↓
Answer
```

## Technologies Used

* Python
* NumPy
* Sentence Transformers
* Ollama
* Object-Oriented Programming
* Factory Design Pattern
* Abstract Base Classes
* Vector Embeddings
* Cosine Similarity
* Retrieval-Augmented Generation

## What I Learned From This Project

This project was built to understand the logic behind a basic RAG system rather than relying entirely on high-level frameworks.

The project demonstrates:

* File handling
* Object-oriented programming
* Modular architecture
* Factory design pattern
* Abstract base classes
* Text processing
* Sliding-window chunking
* Embeddings
* Vector representations
* Cosine similarity
* Semantic retrieval
* Context construction
* Prompt engineering
* Local LLM integration
* Basic RAG architecture

## Limitations

This is an educational RAG implementation and intentionally uses a simple architecture.

Current limitations include:

* Vector data is stored only in memory.
* Documents must be processed again when the application restarts.
* Retrieval currently uses basic cosine similarity.
* Only TXT and CSV document types are supported.
* There is no persistent vector database.
* Large documents may exceed the context capacity of the local model during summarization.
* The CLI interface is intentionally simple.

## Future Improvements

Possible future improvements include:

* Persistent vector storage
* PDF support
* Better document metadata
* Configurable top-K retrieval
* Improved chunking strategies
* Conversation memory
* Streaming LLM responses
* Source citations for retrieved chunks
* Reranking
* Better error handling
* Web interface
* Multiple document support

## License

This project is intended for educational and personal development purposes.
