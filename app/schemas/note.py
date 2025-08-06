# app/schemas/note.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NoteBase(BaseModel):
    title: str
    content: Optional[str] = None

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    pass

class Note(NoteBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

# We need this forward declaration for the User schema
Note.update_forward_refs()

class NoteVersion(NoteBase):
    id: int
    note_id: int
    version: int
    edited_at: datetime

    class Config:
        orm_mode = True