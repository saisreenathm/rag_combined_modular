from .backends.qdrant_store import QdrantVectorStore
from .backends.session_store import SessionVectorStore

# Config: how many documents are "small" enough for memory?
DOC_COUNT_THRESHOLD = 3
vector_dim = 384  # Should match your embedding model

# Dummy heuristic: in real case, count actual files or pass config
import os
doc_dir = "docs/"  # or wherever your input files are
doc_count = len(os.listdir(doc_dir)) if os.path.exists(doc_dir) else 0

# Backend selection
if doc_count < DOC_COUNT_THRESHOLD:
    print("📦 Using in-memory vector store (SessionVectorStore)")
    _store = SessionVectorStore(vector_dim=vector_dim)
else:
    print("🗄️ Using persistent vector store (QdrantVectorStore)")
    _store = QdrantVectorStore(vector_dim=vector_dim)

# Exposed API
def init_collection():
    return _store.init_collection()

def index_document(doc_id, vector, payload):
    return _store.index_document(doc_id, vector, payload)

def query_vector(vector, top_k=5):
    return _store.query_vector(vector, top_k)
