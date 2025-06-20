import os
from .backends.qdrant_store import QdrantVectorStore
from .backends.session_store import SessionVectorStore

# Heuristic: decide backend
DOC_COUNT_THRESHOLD = 3
vector_dim = 384
doc_dir = "docs/"
doc_count = len(os.listdir(doc_dir)) if os.path.exists(doc_dir) else 0

if doc_count < DOC_COUNT_THRESHOLD:
    print("📦 Using in-memory vector store (SessionVectorStore)")
    _store = SessionVectorStore(vector_dim=vector_dim)
else:
    print("🗄️ Using persistent vector store (QdrantVectorStore)")
    _store = QdrantVectorStore(vector_dim=vector_dim)

# Expose the API for base.py
def get_store():
    return _store
