import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()

        self.pinecone_api_key = os.getenv("PINECONE_API_KEY")
        self.pinecone_host = os.getenv("PINECONE_HOST")
        self.pinecone_region = os.getenv("PINECONE_REGION")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

    @classmethod
    def from_env_file(cls):
        return cls()