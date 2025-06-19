# 🧠 RAG_HEITAA: AI-Powered Healthcare Query Assistant

**RAG_HEITAA** is a modular Retrieval-Augmented Generation (RAG) system designed as a plug-in intelligence layer for the larger HEITa healthcare expense assistant platform.

---

## 🚨 Problem We're Addressing

Healthcare billing in the U.S. is fragmented, opaque, and error-prone:
- 30–80% of bills contain costly mistakes.
- Over 100M Americans can’t afford unexpected medical bills.
- Patients lack tools to understand, verify, or dispute charges.

### 🧩 HEITa Vision
HEITa (Healthcare Expense Information Tracking Assistant) is an AI-driven platform that will:
- Parse bills & claims
- Detect discrepancies
- Empower patients to understand and act
- Offer seamless voice/chat-based navigation

---

## 🔍 Purpose of This Module

This project represents the **RAG-based query module** (RAG_HEITAA) that powers intelligent Q&A over structured health documents (e.g., EOBs, claims, notes).

It is designed to:
- Accept natural language queries
- Use custom embeddings for document indexing
- Retrieve relevant context using a vector store
- Enable future integration with voice-based flows

---

## 🏗️ Project Structure

```
rag_new/
├── chat_engine/
│   └── chat_engine.py         # Core RAG assistant logic
│   └── modules/
│       └── retriever.py       # Query interface with vector store
├── vector_store/
│   ├── base.py                # Public API: init, index, query
│   ├── interfaces.py          # Abstract base class: VectorDB
│   └── backends/
│       └── qdrant_store.py    # Qdrant-backed vector DB implementation
├── main.py                    # CLI runner to test the assistant
└── README.md                  # ← You're here
```

---

## 🧠 RAG Strategy

- **Embedding Model:** Your LLM or embedding model generates document vectors.
- **Vector Store Abstraction:** Supports plug-and-play backends like Qdrant or FAISS via `VectorDB` interface.
- **Decoupled Logic:** Core application doesn't need to know which DB is used — just calls `index_document()` and `query_vector()`.

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Qdrant (via Docker)
```bash
docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant
```

### 3. Run the assistant
```bash
python main.py
```

You can then ask questions like:
> “What happened to my insurance claim?”

---

## 📦 Vector Storage Abstraction

RAG_HEITAA introduces an extensible vector DB architecture:

```python
# Example interface method call
index_document(doc_id="123", vector=[...], payload={"text": "Claim denied"})
results = query_vector(vector=[...], top_k=3)
```

Internally, these delegate to a backend implementation like `QdrantVectorStore`.

---

## 🛣️ Future Roadmap

✅ Modular vector backend (Qdrant)  
✅ Working retrieval pipeline  
🟡 Integration with EOB/claim data  
🟡 Voice command support  
🟡 In-memory fallback for fast prototyping  
🟢 Plug-in into HEITa Phase 1 MVP flows

---

## 🤝 Contributing

This module is part of the HEITa initiative. If you'd like to improve it or plug in alternative vector DBs (e.g., FAISS, Pinecone), feel free to extend the `VectorDB` interface.
