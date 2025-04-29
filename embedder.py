import spacy
from chromadb import PersistentClient
from docs_parser import parse_all_pdfs

nlp = spacy.load("en_core_web_md")

chroma_client = PersistentClient(path="storage")

collection = chroma_client.get_or_create_collection(name="pdf_chunks")

def embed_and_store_chunks():
    chunks = parse_all_pdfs()
    print(f"\n✅ Total chunks parsed: {len(chunks)}")

    for i, (text, metadata) in enumerate(chunks):
        if not text.strip():
            print(f"⚠️ Empty chunk at index {i} (page {metadata['page']} in {metadata['source']})")
            continue

        doc_id = f"{metadata['source']}_p{metadata['page']}_c{i}"
        doc = nlp(text)
        embedding = doc.vector.tolist()

        collection.add(
            documents=[text],
            metadatas=[metadata],
            ids=[doc_id],
            embeddings=[embedding]
        )

    print("\n🎉 Embeddings stored successfully.")

def load_collection():
    return chroma_client.get_collection(name="pdf_chunks")

if __name__ == "__main__":
    embed_and_store_chunks()
