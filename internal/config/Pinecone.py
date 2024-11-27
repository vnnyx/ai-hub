from pinecone import Pinecone as PineconeClient
from internal.config.Config import Config

class Pinecone:
    def __init__(self, config: Config):
        self.config = config

    def new_pinecone(self) -> PineconeClient:
        return PineconeClient(
            api_key=self.config.pinecone_api_key,
        )
