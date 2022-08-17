from datetime import datetime
from pydantic import BaseModel, Field


class RequestCommentSchema(BaseModel):
    content: str = Field(default=None, title="Comment", max_length=1000)
    post_id: int = Field(default=1, title="Post ID where based comment", ge=0)
    user_id: int = Field(default=1, title="User ID who's left comment", ge=0)


class ResponseCommentSchema(RequestCommentSchema):
    id: int = Field(default=1, ge=0)
    created_at: datetime = Field(default=None, title="Comment time")

    class Config:
        orm_mode = True