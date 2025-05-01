import os
import time
import spacy
import requests
from chromadb import PersistentClient
from dotenv import load_dotenv

load_dotenv()
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "phi")

nlp = spacy.load("en_core_web_md")
chroma_client = PersistentClient(path="storage")
collection = chroma_client.get_collection(name="pdf_chunks")


def ask_question(question: str, top_k: int = 2):
    doc = nlp(question)
    question_vector = doc.vector.tolist()

    results = collection.query(
        query_embeddings=[question_vector],
        n_results=top_k
    )

    chunks = results['documents'][0]
    metadata = results['metadatas'][0]
    context = "\n\n".join(chunks)

    if len(context) > 3000:
        context = context[:3000]

    prompt = f"""You are an AI assistant trained to answer questions based on the context below.
Answer concisely and only based on the given information. If the answer cannot be found, say "I don't know."

Context:
{context}

Question: {question}
"""

    try:
        start_time = time.time()

        response = requests.post(
            f"{OLLAMA_API_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=480
        )

        duration = round(time.time() - start_time, 2)
        print(f"✅ Ollama responded in {duration} seconds.")

        try:
            data = response.json()
            return {
                "answer": data.get("response", "[No response]").strip(),
                "sources": metadata
            }

        except Exception as e:
            print("❌ ERROR parsing Ollama JSON response:", e)
            print("🔁 Raw response text:\n", response.text[:500])
            return {
                "answer": "[Failed to parse model response]",
                "sources": metadata
            }

    except requests.exceptions.Timeout:
        print("❌ Ollama took too long to respond.")
        return {
            "answer": "[Ollama timed out — model may not be loaded or is slow to respond.]",
            "sources": metadata
        }

    except requests.exceptions.RequestException as e:
        print("❌ ERROR while calling Ollama:", e)
        return {
            "answer": "[Failed to generate answer — API error]",
            "sources": metadata
        }
