# DocuMind CLI

A lightweight, modular, privacy-focused Python CLI application designed to parse documents (`.txt`, `.csv`), apply custom sliding-window text chunking, and perform document summarization or interactive Q&A using a local LLM via Ollama.

---

## What DocuMind Does
It Takes your raw text or tabular data files, converts tabular structures into clear human-readable prompts, splits large texts into overlapping context chunks, and sends grounded system prompts to a local Ollama LLM (`qwen2.5:3b`) without relying on cloud APIs or exposing data externally.

---

## Features

Dynamic File Parsing: Decouples file loading logic using the Factory Design Pattern and Abstract Base Classes (ABC).

Tabular-to-Text Mapping: Converts `.csv` rows into explicit `Key: Value` text structures so LLMs retain field context.

Sliding-Window Chunking:** Tokenizes text on a word-level with configurable chunk sizes and overlaps to preserve sentence context across chunk boundaries.

Dual AI Operations:
Document Summarization: Generates concise 6-line key topic summaries.
Interactive Document Chat: Enables ground-constrained Q&A with strict context boundaries to minimize model hallucination.

100% Privacy & Local Execution:** Runs completely offline via Ollama.

---

##  Architecture

```text
[ USER CLI ]
     │
     ▼
[ DocumentFactory ] ──> Selects dynamic loader based on file extension (.txt, .csv)
     │
     ▼
[ FileLoader ] ──> Validates & reads document into formatted text string
     │
     ▼
[ Chunker ] ──> Slices string into overlapping word arrays (`list[str]`)
     │
     ▼
[ AIEngine ] ──> Injects context chunks + query into prompt ──> Local Ollama (`qwen2.5:3b`)