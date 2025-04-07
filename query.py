import spacy
from chromadb import PersistentClient

# Load the same SpaCy model used in embedder.py
nlp = spacy.load("en_core_web_md")

# Connect to ChromaDB
chroma_client = PersistentClient(path="storage")
collection = chroma_client.get_collection(name="pdf_chunks")

def ask_question(question: str, top_k: int = 3):
    # Embed the question
    doc = nlp(question)
    question_vector = doc.vector.tolist()

    # Query the vector store
    results = collection.query(
        query_embeddings=[question_vector],
        n_results=top_k
    )

    answers = []
    for i in range(len(results['documents'][0])):
        answers.append({
            "text": results['documents'][0][i],
            "metadata": results['metadatas'][0][i],
            "score": results['distances'][0][i]
        })

    return answers
