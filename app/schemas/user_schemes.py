from datetime import datetime
from pydantic import BaseModel, EmailStr


class RequestUser(BaseModel):
    f_name: str | None = None
    l_name: str | None = None
    username: str
    email: EmailStr
    password: str
    disabled: bool = False


class ResponseUser(RequestUser):
    id: int
    last_login: datetime = None
    created_at: datetime

    class Config:
        orm_mode = True


