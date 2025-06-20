from .router import get_store

_store = get_store()

def init_collection():
    return _store.init_collection()

def index_document(doc_id, vector, payload):
    return _store.index_document(doc_id, vector, payload)

def query_vector(vector, top_k=5):
    return _store.query_vector(vector, top_k)
