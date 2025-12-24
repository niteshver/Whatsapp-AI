from langchain_ollama import OllamaEmbeddings

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
import json
import os

with open("whatsapp_output/output_data.json", "r", encoding="utf-8") as f:
    messages = json.load(f)

print(f"Loaded {len(messages)} messages")

docs = []

for msg in messages:
    text = msg.get("text", "").strip()

    
    if not text:
        continue

    docs.append(
        Document(
            page_content=text,
            metadata={
                "contact": msg.get("contact", "unknown"),
                "sender": msg.get("sender", "unknown")
            }
        )
    )

print(f"Created {len(docs)} documents")


if not docs:
    raise ValueError("❌ No valid documents found. Check your JSON file.")


embedding = OllamaEmbeddings(model="nomic-embed-text")


db = FAISS.from_documents(docs, embedding)


os.makedirs("embedding", exist_ok=True)
db.save_local("embedding/faiss_index")

print("✅ Vector store created successfully")
