from pydantic import BaseModel, Field


class RequestLikesScheme(BaseModel):
    post_id: int = Field(default=1, ge=0, description="Like on post")
    user_id: int = Field(default=1, ge=0, description="User like")


class ResponseLikeScheme(RequestLikesScheme):
    id: int = Field(default=1, ge=0)

    class Config:
        orm_mode = True