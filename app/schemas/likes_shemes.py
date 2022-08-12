from pydantic import BaseModel


class RequestLikesScheme(BaseModel):
    post_id: int
    user_id: int


class ResponseLikeScheme(RequestLikesScheme):
    id: int

    class Config:
        orm_mode = True