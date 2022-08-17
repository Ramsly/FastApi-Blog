from datetime import datetime
from pydantic import BaseModel, Field


class RequestBlogScheme(BaseModel):
    title: str = Field(default=None, title="Title of blog", max_length=100)
    owner_id: int = Field(default=1, title="ID owner", ge=0)
    content: str | None = Field(default=None, title="Content of blog", max_length=5000)
    created_at: datetime = Field(default=None, title="Time of published blog")
    visible: bool = Field(default=True, title="Blog visibility")


class ResponseBlogScheme(BaseModel):
    id: int = Field(default=1, ge=0)
    title: str = Field(default=None, title="Title of blog", max_length=100)
    content: str = Field(default=None, title="Content of blog", max_length=5000)
    created_at: datetime = Field(default=None, title="Time of published blog")
    updated_at: datetime = Field(default=None, title="Updated time of published blog")

    class Config:
        orm_mode = True