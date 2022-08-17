from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class RequestUser(BaseModel):
    f_name: str | None = Field(default=None, title="First name of user", max_length=100)
    l_name: str | None = Field(default=None, title="Second name of user", max_length=100)
    username: str = Field(default=None, title="Username of user (unique)", max_length=100)
    email: EmailStr = Field(default=None, title="Email of user (unique)")
    password: str = Field(default=None, title="Hashed password")
    disabled: bool = Field(default=False, title="User status")


class ResponseUser(RequestUser):
    id: int = Field(default=1, title="ID of user")
    last_login: datetime = Field(default=None, title="Time of last login")
    created_at: datetime = Field(default=None, title="Time of created user")

    class Config:
        orm_mode = True


