from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Source:
    id: Optional[str]
    name: str

@dataclass
class NewsMetaData:
    sourceName: str
    author: Optional[str]
    title: str
    description: Optional[str]
    url: str
    urlToImage: Optional[str]
    publishedAt: datetime

@dataclass
class News:
    source: Source
    author: Optional[str]
    title: str
    description: Optional[str]
    url: str
    urlToImage: Optional[str]
    publishedAt: datetime
    content: Optional[str]

    @classmethod
    def from_json(cls, data_dict: dict):
        return cls(
            source=Source(
                id=data_dict.get("source", {}).get("id"),
                name=data_dict.get("source", {}).get("name")
            ),
            author=data_dict.get("author"),
            title=data_dict.get("title"),
            description=data_dict.get("description"),
            url=data_dict.get("url"),
            urlToImage=data_dict.get("urlToImage"),
            publishedAt=datetime.strptime(data_dict.get("publishedAt"), "%Y-%m-%dT%H:%M:%SZ"),
            content=data_dict.get("content")
        )
    
    @classmethod
    def to_news_metadata(cls, news):
        return NewsMetaData(
            sourceName=news.source.name,
            author=news.author,
            title=news.title,
            description=news.description,
            url=news.url,
            urlToImage=news.urlToImage,
            publishedAt=news.publishedAt
        )
    
