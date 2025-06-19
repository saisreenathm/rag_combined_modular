### vector_store/backends/qdrant_store.py
from typing import Any
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance, PointStruct
from qdrant_client.http.exceptions import UnexpectedResponse
from ..interfaces import VectorDB

class QdrantVectorStore(VectorDB):
    def __init__(self, host: str = "localhost", port: int = 6333, collection_name: str = "default_collection", vector_dim: int = 384):
        self.client = QdrantClient(host=host, port=port)
        self.collection_name = collection_name
        self.vector_dim = vector_dim

    def init_collection(self) -> None:
        # Try deleting the collection manually to avoid recreate_collection crash
        try:
            self.client.delete_collection(collection_name=self.collection_name)
        except UnexpectedResponse as e:
            print(f"Warning: Failed to delete collection '{self.collection_name}' (might not exist): {e}")

        # Create it fresh
        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(size=self.vector_dim, distance=Distance.COSINE),
        )

    def index_document(self, doc_id: str, vector: list[float], payload: dict[str, Any]) -> None:
        if len(vector) != self.vector_dim:
            raise ValueError(f"Vector dimension mismatch: expected {self.vector_dim}, got {len(vector)}")

        self.client.upsert(
            collection_name=self.collection_name,
            points=[PointStruct(id=doc_id, vector=vector, payload=payload)],
        )

    def query_vector(self, vector: list[float], top_k: int = 5) -> list[dict[str, Any]]:
        if len(vector) != self.vector_dim:
            raise ValueError(f"Vector dimension mismatch: expected {self.vector_dim}, got {len(vector)}")

        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            limit=top_k
        )
        return [result.dict() for result in results]

