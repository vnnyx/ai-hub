from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DataVectorRequest(_message.Message):
    __slots__ = ("data", "type")
    DATA_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    data: str
    type: str
    def __init__(self, data: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
