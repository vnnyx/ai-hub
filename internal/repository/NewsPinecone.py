from abc import ABC, abstractmethod
from typing import List, Dict

class NewsPineconeRepository(ABC):
    @abstractmethod
    def store_to_pinecone(self, vectors: List[Dict[str, str]]):
        pass