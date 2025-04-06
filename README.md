# PDF RAG

PDF RAG is a lightweight Retrieval-Augmented Generation (RAG) chatbot designed to answer questions based on the content of local PDF files. It accepts both **text** and **screenshot images containing text** as input, retrieves the most relevant information from the PDFs, and responds with the **answer** along with the **source document reference**.

## 🚀 Features

- 📄 Load and index multiple local PDF files
- 🔍 Semantic search using vector embeddings
- 🤖 Simple chatbot interface
- 🧠 Answer questions from:
  - Text input
  - Screenshots (image-to-text OCR)
- 📚 Provides source document reference for transparency

## 🛠️ Tech Stack

- Python 3
- [Sentence Transformers](https://www.sbert.net/) for embeddings
- [Chroma](https://www.trychroma.com/) or FAISS for vector search
- [Flask](https://flask.palletsprojects.com/) or FastAPI for serving
- [PyMuPDF](https://pymupdf.readthedocs.io/) for PDF parsing
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for image-to-text (screenshot support)
