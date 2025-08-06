# app/api/v1/endpoints/notes.py

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas, services
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Note, status_code=status.HTTP_201_CREATED)
def create_note(
    note: schemas.NoteCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(services.auth_service.get_current_user)
):
    return services.note_service.create_note(db=db, note=note, user_id=current_user.id)

@router.get("/", response_model=List[schemas.Note])
def read_notes(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(services.auth_service.get_current_user)
):
    return services.note_service.get_user_notes(db=db, user_id=current_user.id)

@router.get("/{note_id}", response_model=schemas.Note)
def read_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(services.auth_service.get_current_user)
):
    db_note = services.note_service.get_note(db, note_id=note_id, user_id=current_user.id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.put("/{note_id}", response_model=schemas.Note)
def update_note(
    note_id: int,
    note: schemas.NoteUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(services.auth_service.get_current_user)
):
    db_note = services.note_service.update_note(db, note_id=note_id, note_update=note, user_id=current_user.id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.delete("/{note_id}", response_model=schemas.Note)
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(services.auth_service.get_current_user)
):
    db_note = services.note_service.delete_note(db, note_id=note_id, user_id=current_user.id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.get("/{note_id}/history", response_model=List[schemas.NoteVersion])
def read_note_history(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(services.auth_service.get_current_user)
):
    versions = services.note_service.get_note_versions(db, note_id=note_id, user_id=current_user.id)
    if not versions and not services.note_service.get_note(db, note_id, current_user.id):
        raise HTTPException(status_code=404, detail="Note not found")
    return versions