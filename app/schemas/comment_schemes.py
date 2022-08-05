from datetime import datetime
from pydantic import BaseModel


class RequestCommentSchema(BaseModel):
    content: str
    post_id: int


class ResponseCommentSchema(BaseModel):
    id: int
    content: int
    post_id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True