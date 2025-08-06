# app/schemas/user.py

from pydantic import BaseModel
from typing import List, Optional

# We need to forward-declare Note to avoid circular imports
from .note import Note

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    notes: List[Note] = []

    class Config:
        orm_mode = True # This allows the model to be created from ORM objects