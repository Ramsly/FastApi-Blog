from datetime import datetime
from pydantic import BaseModel


class RequestBlogScheme(BaseModel):
    title: str
    owner_id: int
    content: str | None = None
    created_at: datetime = None
    visible: bool = True


class ResponseBlogScheme(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_mode = True