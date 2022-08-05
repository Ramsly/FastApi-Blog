from datetime import datetime
from pydantic import BaseModel


class RequestBlogScheme(BaseModel):
    title: str
    content: str
    created_at: datetime
    visible: bool = True


class ResponseBlogScheme(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True