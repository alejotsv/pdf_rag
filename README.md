# 📚 PDF RAG

PDF RAG is a lightweight Retrieval-Augmented Generation (RAG) chatbot designed to answer questions based on the content of **local PDF files**. It accepts **text questions** (image support coming soon), retrieves relevant content from the PDFs, and responds with a concise **answer** and **source reference**.

---

## 🚀 Features

- 📄 Load and index multiple local PDF files
- 🔍 Semantic search using vector embeddings (via SpaCy + Chroma)
- 🤖 Lightweight chatbot interface in the terminal
- 🧠 Question answering based on extracted PDF context
- 📚 Source file and page number returned with each answer
- 🧠 Powered by a **local Ollama model** (e.g., `phi`, `mistral`)

---

## 🛠️ Tech Stack

- **Python 3.12+**
- [`Ollama`](https://ollama.com) — local LLM backend (phi, mistral, gemma, etc.)
- [`ChromaDB`](https://www.trychroma.com) — vector store
- [`PyMuPDF`](https://pymupdf.readthedocs.io/) — PDF parsing
- [`SpaCy`](https://spacy.io/) — embeddings
- [`Tesseract`](https://github.com/tesseract-ocr/tesseract) — *(optional)* for screenshot text extraction (coming soon)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git https://github.com/alejotsv/pdf_rag.git
cd pdf-rag
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Using a Local Model with Ollama

1. **Install Ollama**  
   [Ollama installation guide →](https://ollama.com/download)

2. **Pull a model**  
   (Choose one based on your system resources)

   ```bash
   ollama pull phi       # Good for low RAM (~2GB)
   ollama pull mistral   # Better reasoning, ~7–8GB RAM needed
   ```

3. **Run the model locally**

   In a separate terminal:

   ```bash
   ollama run phi
   ```

   You should see:
   ```
   >>>
   ```

4. **Set the model name in your `.env` file**

   Create a `.env` file at the root of your project:

   ```env
   OLLAMA_MODEL=phi
   OLLAMA_API_URL=http://localhost:11434
   ```

---

## ▶️ Running the Chatbot

In your main terminal (where your venv is activated):

```bash
python main.py
```

Then follow the prompt to paste your question. Press Enter twice to submit.

---

## 🧪 Example Question

```
What is a B-tree index and when is it used?
```

---

## 📁 Folder Structure

```
data/                # Your local PDFs go here
storage/             # Vector DB storage (auto-generated)
main.py              # Chat interface
embedder.py          # Embeds and stores chunks
docs_parser.py       # PDF text parsing and chunking
query.py             # Handles question answering
cleaning_rules.txt   # (optional) regex rules for cleaning footers, etc.
```

---

## 📌 Notes

- If you run into memory errors, try using `phi` instead of `mistral`.
- The app currently supports **text input only** — screenshot OCR coming soon.
- To reprocess your PDFs, delete `storage/` and re-run the embed step.

---

## 🧑‍💻 Author

Made by [Alejandro Salas](https://github.com/alejotsv) — feel free to contribute or raise issues!

