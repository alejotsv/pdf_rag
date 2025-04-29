import os
import fitz
import re

DATA_DIR = "data"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

def load_cleaning_rules(path="cleaning_rules.txt"):
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return [re.compile(line.strip()) for line in f if line.strip()]

def clean_text(text, regex_list):
    lines = text.split("\n")
    cleaned_lines = []
    for line in lines:
        if any(regex.search(line) for regex in regex_list):
            continue
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)

def extract_text_from_pdf(pdf_path, cleaning_rules=None):
    doc = fitz.open(pdf_path)
    full_text = []
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        if cleaning_rules:
            text = clean_text(text, cleaning_rules)

        if text.strip():
            full_text.append((page_num, text))
    return full_text

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

def parse_all_pdfs():
    all_chunks = []
    cleaning_rules = load_cleaning_rules()

    for filename in os.listdir(DATA_DIR):
        if filename.lower().endswith(".pdf"):
            path = os.path.join(DATA_DIR, filename)
            print(f"Parsing {filename}...")

            pages = extract_text_from_pdf(path, cleaning_rules)

            for page_num, page_text in pages:
                chunks = chunk_text(page_text)
                for chunk in chunks:
                    metadata = {
                        "source": filename,
                        "page": page_num
                    }
                    all_chunks.append((chunk, metadata))

    return all_chunks
