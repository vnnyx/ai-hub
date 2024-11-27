from pb.vector.vector_pb2_grpc import VectorServicer
from internal.usecase.NewsPineconeUseCase import _NewsPinecone
from google.protobuf.wrappers_pb2 import BoolValue


class NewsPineconeService(VectorServicer):
    def __init__(self, news_usecase: _NewsPinecone):
        self.news_usecase = news_usecase

    def StoreToVectorDB(self, request, context):
        self.news_usecase.store_to_pinecone(request)
        return BoolValue(value=True)
    