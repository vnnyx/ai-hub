import openai
from typing import List
from internal.model.OpenAI import OpenAIEmbeddingResponse, DataEmbedding, Usage

def get_embedding(text: List[str])->OpenAIEmbeddingResponse:
    response = openai.embeddings.create(
        model="text-embedding-3-large",
        input=text
    )
    data = [DataEmbedding(object=embedding.object, embedding=embedding.embedding, index=embedding.index) for embedding in response.data]
    usage = Usage(prompt_tokens=response.usage.prompt_tokens, total_tokens=response.usage.total_tokens)
    response = OpenAIEmbeddingResponse(
        object=response.object,
        data=data,
        model=response.model,
        usage=usage
    )
    return response