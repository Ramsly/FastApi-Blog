from pydantic import BaseModel


class RequestLikesScheme(BaseModel):
    post_id: int
    user_id: int


class ResponseLikeScheme(BaseModel):
    id: int
    post_id: int
    user_id: int

    class Config:
        orm_mode = True