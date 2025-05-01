from query import ask_question

print("📚 PDF RAG Chatbot (type 'exit' to quit)\n")

while True:
    print("🧠 Paste your question below. Press Enter twice to submit:")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    question = "\n".join(lines)

    if question.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    print("\n🌐 Sending request to model...\n")
    res = ask_question(question)

    if res["answer"].startswith("[Ollama timed out") or res["answer"].startswith("[Failed"):
        print(f"\n❌ ERROR: {res['answer']}")
    else:
        print(f"\n🤖 Answer:\n{res['answer']}")

    print("\n📚 Sources:")
    for src in res['sources']:
        print(f"📄 {src['source']} (page {src['page']})")
