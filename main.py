from query import ask_question

print("📚 PDF RAG Chatbot (type 'exit' to quit)\n")

while True:
    question = input("🧠 Ask a question: ").strip()
    if question.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    results = ask_question(question)
    if not results:
        print("⚠️ No results found.")
    else:
        for res in results:
            print(f"\n📄 {res['metadata']['source']} (page {res['metadata']['page']})")
            print(f"🔍 Similarity score: {res['score']:.4f}")
            print(f"{res['text']}")
