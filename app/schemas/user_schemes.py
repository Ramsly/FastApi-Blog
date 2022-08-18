from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class RequestUser(BaseModel):
    f_name: str | None = Field(default=None, description="First name of user", max_length=100)
    l_name: str | None = Field(default=None, description="Second name of user", max_length=100)
    username: str = Field(default=None, description="Username of user (unique)", max_length=100)
    email: EmailStr = Field(default=None, description="Email of user (unique)")
    password: str = Field(default=None, description="Hashed password")
    disabled: bool = Field(default=False, description="User status")


class ResponseUser(BaseModel):
    id: int = Field(default=1, ge=0, description="ID of user")
    f_name: str | None = Field(default=None, description="First name of user", max_length=100)
    l_name: str | None = Field(default=None, description="Second name of user", max_length=100)
    username: str = Field(default=None, description="Username of user (unique)", max_length=100)
    email: EmailStr = Field(default=None, description="Email of user (unique)")
    disabled: bool = Field(default=False, description="User status")
    last_login: datetime = Field(default=None, description="Time of last login")
    created_at: datetime = Field(default=None, description="Time of created user")

    class Config:
        orm_mode = True


