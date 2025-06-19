import numpy as np
from typing import Any
from ..interfaces import VectorDB

class SessionVectorStore(VectorDB):
    def __init__(self, vector_dim: int = 384):
        self.vectors = []
        self.payloads = []
        self.ids = []
        self.vector_dim = vector_dim

    def init_collection(self) -> None:
        self.vectors.clear()
        self.payloads.clear()
        self.ids.clear()

    def index_document(self, doc_id: str, vector: list[float], payload: dict[str, Any]) -> None:
        if len(vector) != self.vector_dim:
            raise ValueError(f"Vector dimension mismatch: expected {self.vector_dim}, got {len(vector)}")
        self.ids.append(doc_id)
        self.vectors.append(np.array(vector))
        self.payloads.append(payload)

    def query_vector(self, vector: list[float], top_k: int = 5) -> list[dict[str, Any]]:
        if len(vector) != self.vector_dim:
            raise ValueError(f"Vector dimension mismatch: expected {self.vector_dim}, got {len(vector)}")
        
        query_vec = np.array(vector)
        all_vecs = np.stack(self.vectors)
        similarities = np.dot(all_vecs, query_vec) / (
            np.linalg.norm(all_vecs, axis=1) * np.linalg.norm(query_vec) + 1e-10
        )

        top_indices = similarities.argsort()[-top_k:][::-1]
        return [
            {"id": self.ids[i], "payload": self.payloads[i], "score": float(similarities[i])}
            for i in top_indices
        ]
