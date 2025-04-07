import spacy
import chromadb
from chromadb import PersistentClient
from chromadb.config import Settings
from docs_parser import parse_all_pdfs

nlp = spacy.load("en_core_web_md")

chroma_client = PersistentClient(path="storage")

collection = chroma_client.get_or_create_collection(name="pdf_chunks")

def embed_and_store_chunks():
    chunks = parse_all_pdfs()
    print(f"Embedding {len(chunks)} chunks...")

    for i, (text, metadata) in enumerate(chunks):
        doc_id = f"{metadata['source']}_p{metadata['page']}_c{i}"
        doc = nlp(text)
        embedding = doc.vector.tolist()  # SpaCy uses numpy arrays

        collection.add(
            documents=[text],
            metadatas=[metadata],
            ids=[doc_id],
            embeddings=[embedding]
        )

    print("Embeddings stored successfully.")

def load_collection():
    return chroma_client.get_collection(name="pdf_chunks")
