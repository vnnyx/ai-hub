from dataclasses import dataclass
from typing import List, Optional, Dict
from datetime import datetime


@dataclass
class DataEmbedding:
    object: str
    embedding: List[float]
    index: int

@dataclass
class Usage:
    prompt_tokens: int
    total_tokens: int

@dataclass
class OpenAIEmbeddingResponse:
    object: str
    data: List[DataEmbedding]
    model: str
    usage: Usage
