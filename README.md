# 🤖 WhatsApp Personalized AI Agent

A **personalized AI assistant for WhatsApp** that generates **human-like replies** by learning from your **own chat history** — without training or fine-tuning any model.

The system uses **Retrieval-Augmented Generation (RAG)** with **local embeddings**, **vector search**, and a **FastAPI backend**, orchestrated via **n8n workflows**.

---

## ✨ Key Highlights

- 🧠 Learns reply style from **your own WhatsApp chats**
- 🔒 Privacy-first (local embeddings, no data sent to cloud)
- ⚡ Fast semantic search using FAISS
- 🆓 Uses free & open-source tools
- 🧩 Clean, modular, production-style architecture
- 🎯 Ideal for hackathons, resumes, and AI portfolios

---

## 📁 Folder Structure

``` python
whatsapp-ai-bot/
│
├── whatsapp_raw_chats/
│ ├── raw_chats/
│ │ ├── mom.txt
│ │ ├── friend.txt
│ │ ├── crush.txt
│ │ └── group1.txt
│ │
│ ├── clean_chats.py
│ └── cleaned_messages.json
│
├── embeddings/
│ ├── create_embeddings.py
│ └── faiss_index/
│ ├── index.faiss
│ └── index.pkl
│
├── backend/
│ ├── app.py
│ ├── utils.py
│ └── requirements.txt
│
├── n8n/
│ └── whatsapp_workflow.json
│
├── README.md
└── .gitignore
```

---

## 🧠 Project Overview

This project builds a **context-aware WhatsApp AI agent** that replies based on **relevant past conversations**.

Instead of training a model, it uses **Retrieval-Augmented Generation (RAG)**:

1. WhatsApp chats are cleaned and structured
2. Messages are converted into vector embeddings
3. Similar past messages are retrieved using FAISS
4. An LLM generates replies using retrieved context

### Why RAG?
- No model training required
- Faster and cheaper
- Better privacy
- Easier to debug and scale

---

## ⚙️ Tech Stack

### 🧹 Data Cleaning
- **Python Regex (`re`)**
- Extracts sender and message text
- Removes timestamps, system messages, and noise

### 🧠 Embeddings
- **Ollama Embeddings**
- Model: `nomic-embed-text`
- Runs locally (no API key required)

### 📦 Vector Database
- **FAISS**
- Efficient similarity search over embeddings

### 🌐 Backend
- **FastAPI**
- Exposes `/query` endpoint
- Handles retrieval, prompt creation, and response logic

### 🔗 AI Framework
- **LangChain**
- Manages documents, embeddings, and vector retrieval

### 🔁 Automation
- **n8n**
- Connects WhatsApp → Backend → Reply
- Orchestrates message workflows

### ☁️ Deployment
- **Railway**
- Hosts the FastAPI backend

---

## 🔄 System Architecture

``` python
WhatsApp Message
↓
n8n Workflow
↓
FastAPI Backend
├─ FAISS Vector Search
├─ Ollama Embeddings
└─ LLM Response Generation
↓
n8n
↓
WhatsApp Reply
```

---

## 🚀 How It Works

1. Export WhatsApp chats as `.txt` files
2. Clean and parse chats using regex
3. Generate embeddings with Ollama
4. Store vectors in FAISS
5. Receive new messages via n8n
6. Retrieve relevant past chats
7. Generate a personalized reply
8. Send reply back to WhatsApp

---

## 🎯 Use Cases

- Personalized WhatsApp auto-replies  
- AI memory and RAG-based assistants  
- Conversational AI experiments  
- Hackathon demos  
- Resume and portfolio projects  

---

## 🏆 Why This Project Matters

This project demonstrates:

- Real-world **AI system design**
- Practical use of **RAG architecture**
- Strong **backend + AI integration**
- Clean separation of concerns
- Debugging of messy real-world data
- Production-style engineering mindset

Perfect for:
- 🎓 Hackathons  
- 💼 Technical interviews  
- 🔗 LinkedIn & GitHub portfolios  


## 🤝 Contributing

Contributions are welcome!

- Open an issue for bugs or feature requests
- Submit a pull request for improvements

For questions or collaboration, feel free to reach out.

---

## 👤 Author

- Maintained by: Nitesh  -
- Project Type: Personal / Open Source  
- Status: Active Development

---

## 📌 Disclaimer

This project is for **educational and experimental purposes**.  
Ensure compliance with WhatsApp’s terms of service when deploying automation.

---
