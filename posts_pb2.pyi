from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetPostsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetPostsResponse(_message.Message):
    __slots__ = ("content", "created_at", "total_likes")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LIKES_FIELD_NUMBER: _ClassVar[int]
    content: str
    created_at: str
    total_likes: int
    def __init__(self, content: _Optional[str] = ..., created_at: _Optional[str] = ..., total_likes: _Optional[int] = ...) -> None: ...

class CustomMessageRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CustomMessageResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...
