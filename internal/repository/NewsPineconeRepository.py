from internal.repository.NewsPinecone import NewsPineconeRepository
from pinecone import Pinecone, Vector
from typing import List, Dict

class _NewsPineconeRepository(NewsPineconeRepository):
    def __init__(self, pc: Pinecone):
        self.pc = pc

    def store_to_pinecone(self, vectors: List[Vector]):
        index = self.pc.Index("news")
        index.upsert(vectors)