from abc import ABC, abstractmethod
from typing import Any

class VectorDB(ABC):
    @abstractmethod
    def init_collection(self) -> None:
        pass

    @abstractmethod
    def index_document(self, doc_id: str, vector: list[float], payload: dict[str, Any]) -> None:
        pass

    @abstractmethod
    def query_vector(self, vector: list[float], top_k: int = 5) -> list[dict[str, Any]]:
        pass
