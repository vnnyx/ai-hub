from concurrent import futures
from pb.vector.vector_pb2_grpc import add_VectorServicer_to_server
from internal.delivery.grpc.NewsPinecone import NewsPineconeService
from internal.config.Config import Config
from internal.config.Pinecone import Pinecone
from internal.usecase.NewsPineconeUseCase import _NewsPinecone
from internal.repository.NewsPineconeRepository import _NewsPineconeRepository
from sentence_transformers import SentenceTransformer
import grpc

def grpc_serve():
    config = Config()
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    pc = Pinecone(config)
    pc = pc.new_pinecone()
    pinecone_repository = _NewsPineconeRepository(pc)
    news_usecase = _NewsPinecone(pc, pinecone_repository)
    news_pinecone_service = NewsPineconeService(news_usecase)
    
    add_VectorServicer_to_server(news_pinecone_service, server)

    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()