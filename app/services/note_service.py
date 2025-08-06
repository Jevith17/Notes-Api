# app/services/note_service.py

from sqlalchemy.orm import Session
from app.models import note as note_model
from app.models import user as user_model
from app.schemas import note as note_schema
from typing import List, Optional

def create_note(db: Session, note: note_schema.NoteCreate, user_id: int) -> note_model.Note:
    db_note = note_model.Note(**note.dict(), owner_id=user_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def get_user_notes(db: Session, user_id: int) -> List[note_model.Note]:
    return db.query(note_model.Note).filter(note_model.Note.owner_id == user_id).all()

def get_note(db: Session, note_id: int, user_id: int) -> Optional[note_model.Note]:
    return db.query(note_model.Note).filter(note_model.Note.id == note_id, note_model.Note.owner_id == user_id).first()

def update_note(db: Session, note_id: int, note_update: note_schema.NoteUpdate, user_id: int) -> Optional[note_model.Note]:
    db_note = get_note(db, note_id, user_id)
    if not db_note:
        return None

    # --- VERSIONING LOGIC ---
    # 1. Get the current version number
    current_version_num = len(db_note.versions) + 1

    # 2. Create a historical version record of the *current* state
    historical_version = note_model.NoteVersion(
        note_id=db_note.id,
        version=current_version_num,
        title=db_note.title,
        content=db_note.content
    )
    db.add(historical_version)
    
    # 3. Now, update the main note with the new data
    update_data = note_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_note, key, value)

    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

def delete_note(db: Session, note_id: int, user_id: int) -> Optional[note_model.Note]:
    db_note = get_note(db, note_id, user_id)
    if db_note:
        db.delete(db_note)
        db.commit()
    return db_note

def get_note_versions(db: Session, note_id: int, user_id: int) -> List[note_model.NoteVersion]:
    # First, ensure the user owns the main note
    db_note = get_note(db, note_id, user_id)
    if not db_note:
        return [] # Or raise an exception
    return db.query(note_model.NoteVersion).filter(note_model.NoteVersion.note_id == note_id).order_by(note_model.NoteVersion.version.desc()).all()