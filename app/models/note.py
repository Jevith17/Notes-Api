# app/models/note.py

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime

from app.db.session import Base

# This is the main Note table. It always holds the LATEST version of the note.
class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    
    # Foreign key to link to the User table. This ensures per-user isolation.
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Relationship to the User model
    owner = relationship("User", back_populates="notes")
    
    # Relationship to the NoteVersion model
    versions = relationship("NoteVersion", back_populates="note", cascade="all, delete-orphan")


# This table stores the historical versions of a note.
class NoteVersion(Base):
    __tablename__ = "note_versions"

    id = Column(Integer, primary_key=True, index=True)
    note_id = Column(Integer, ForeignKey("notes.id"), nullable=False)
    version = Column(Integer, nullable=False) # e.g., 1, 2, 3...
    title = Column(String, index=True)
    content = Column(Text)
    edited_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationship back to the main Note
    note = relationship("Note", back_populates="versions")