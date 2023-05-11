import re

from pydantic.main import BaseModel
from typing import Optional


class LoginRequest(BaseModel):

    email: str
    pwd: str


class CreateMemberRequest(BaseModel):

    name: str
    gender: Optional[str] = None
    email: str
    pwd: str


class EditMemberInfoRequest(BaseModel):

    account_id: str
    name: str
    gender: Optional[str] = None
    pwd: str
