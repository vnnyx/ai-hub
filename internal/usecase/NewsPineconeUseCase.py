from typing import List, Dict
from internal.usecase.NewsPinecone import NewsPineconeUseCase
from internal.repository.NewsPineconeRepository import NewsPineconeRepository
from pinecone import Pinecone, Vector
from pb.vector.vector_pb2 import DataVectorRequest
from internal.model.News import News
from langchain.text_splitter import RecursiveCharacterTextSplitter
from internal.utils.CleanData import clean_text
from internal.utils.Embedding import get_embedding
from datetime import datetime
from sentence_transformers import SentenceTransformer
import json

class _NewsPinecone(NewsPineconeUseCase):
    def __init__(self, pc: Pinecone, news_repository: NewsPineconeRepository):
        self.pc = pc
        self.news_repository = news_repository

    def store_to_pinecone(self, request: DataVectorRequest):
        print("Storing to Pinecone")
        vectors: List[Vector] = []
        
        data = request.data
        data_from = request.type

        data_dict = json.loads(data)
        news = News.from_json(data_dict)
        news.content = clean_text(news.content)
        meta_data = news.to_news_metadata(news)
        print(news.content)

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 512,
            chunk_overlap = 0
        )
        docs = text_splitter.create_documents([news.content])
        print(len(docs))

        content_chunks = [doc.page_content for doc in docs]
        embeddings = get_embedding(content_chunks)
        vector_values = [embedding.embedding for embedding in embeddings.data]
        print(len(vector_values))

        for i, vector_data in enumerate(vector_values):
            vector = Vector(
                id=f"{data_from}_{meta_data.publishedAt}_{i}",
                values=vector_data,
                metadata=meta_data.__dict__,
                time_stamp=datetime.now().timestamp()
            )
            vectors.append(vector)

        self.news_repository.store_to_pinecone(vectors)



