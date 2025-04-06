from docs_parser import parse_all_pdfs

chunks = parse_all_pdfs()
print(f"Loaded {len(chunks)} chunks.")
print(chunks[0])  # Show first chunk + metadata
