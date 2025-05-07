from datetime import datetime
from typing import List

from pydantic import ConfigDict

from src.config import BaseSchema


class UserCreate(BaseSchema):
    name: str
    surname: str
    password: str


class UserUpdate(BaseSchema):
    name: str | None = None
    surname: str | None = None
    password: str | None = None


class UserRead(BaseSchema):
    id: int
    name: str
    surname: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserSchema(BaseSchema):
    name: str
    surname: str
    password: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ListUserReadSchema(BaseSchema):
    users: List[UserRead]

    model_config = ConfigDict(from_attributes=True)

