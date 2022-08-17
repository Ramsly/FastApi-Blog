from datetime import datetime
from pydantic import BaseModel, Field


class RequestBlogScheme(BaseModel):
    title: str = Field(default=None, description="Title of blog", max_length=100)
    owner_id: int = Field(default=1, description="ID owner", ge=0)
    content: str | None = Field(default=None, description="Content of blog", max_length=5000)
    created_at: datetime = Field(default=None, description="Time of published blog")
    visible: bool = Field(default=True, description="Blog visibility")


class ResponseBlogScheme(BaseModel):
    id: int = Field(default=1, ge=0)
    title: str = Field(default=None, description="Title of blog", max_length=100)
    content: str = Field(default=None, description="Content of blog", max_length=5000)
    created_at: datetime = Field(default=None, description="Time of published blog")
    updated_at: datetime = Field(default=None, description="Updated time of published blog")

    class Config:
        orm_mode = True