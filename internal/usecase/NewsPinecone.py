from abc import ABC, abstractmethod
from pb.vector.vector_pb2 import DataVectorRequest

class NewsPineconeUseCase(ABC):
    @abstractmethod
    def store_to_pinecone(self, request: DataVectorRequest):
        pass