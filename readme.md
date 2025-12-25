# WHATSAPP Personalize AI Agent


## Folder Structure
``` python
 whatsapp-ai-bot/
│
├── whatsapp_raw_chats/
│   ├── raw_chats/
│   │   ├── mom.txt
│   │   ├── friend.txt
│   │   ├── crush.txt
│   │   └── group1.txt
│   │
│   ├── clean_chats.py
│   └── cleaned_messages.json
│
├── embeddings/
│   ├── create_embeddings.py
│   └── faiss_index/
│       ├── index.faiss
│       └── index.pkl
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── utils.py
│
├── n8n/
│   └── whatsapp_workflow.json
│
├── README.md
└── .gitignore
```


---

## 🧠 Project Overview

This project builds a **personalized AI agent** that replies to WhatsApp messages in a **human-like and context-aware manner**.

Instead of training a model, it uses **Retrieval-Augmented Generation (RAG)**:

- Past WhatsApp messages are converted into embeddings  
- Relevant messages are retrieved using vector similarity  
- An LLM generates replies based on retrieved context  

This approach is:
- ✅ Efficient  
- ✅ Privacy-friendly  
- ✅ Cost-effective  

---

## ⚙️ Tech Stack

### 🔹 Data Cleaning
- **Regex (`re`)**
- Extracts sender and message
- Removes timestamps and system messages

### 🔹 Embeddings
- **Ollama Embeddings**
- Model: `nomic-embed-text`
- Runs locally (no API key required)

### 🔹 Vector Database
- **FAISS**
- Fast similarity search over chat embeddings

### 🔹 Backend
- **FastAPI**
- Handles API requests
- Performs retrieval and response generation

### 🔹 AI Framework
- **LangChain**
- Manages embeddings, documents, and vector retrieval

### 🔹 Automation
- **n8n**
- Connects WhatsApp → Backend → Reply
- Orchestrates message workflows

### 🔹 Deployment
- **Railway**
- Hosts the backend service

---

## 🔄 System Architecture
```python
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

## ✨ Key Features

- 📌 Contact-specific context isolation
- 🧠 Memory-based replies using chat history
- 🔒 Local embeddings (privacy-safe)
- ⚡ Fast vector search with FAISS
- 🧩 Modular and scalable architecture
- 🆓 Uses free and open-source tools

---

## 🎯 Use Cases

- Personalized WhatsApp auto-replies  
- AI memory and RAG systems  
- Conversational AI experiments  
- Hackathon demonstrations  
- Resume and portfolio projects  

---

## 🏆 Why This Project Matters

This project demonstrates:
- Real-world **AI system design**
- Practical **RAG implementation**
- Strong **backend + AI integration**
- Clean architecture and scalability
- Production-style engineering mindset

Ideal for:
- 🎓 Hackathons  
- 💼 Resumes  
- 🔗 LinkedIn projects  

---

## 🤝 Contributing

Contributions are welcome!

- Open an issue for bugs or suggestions  
- Submit a pull request for improvements  

For queries or discussions, feel free to contact the maintainer.

---

## 📌 Author

- Maintained by: Nitesh
- Project Type: Personal / Open Source  
- Status:  Active Development

