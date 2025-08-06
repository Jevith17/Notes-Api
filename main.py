# main.py

from fastapi import FastAPI
from app.api.v1.api import api_router
from app.db.session import engine
from app.models import user, note # Import your models

# This line creates the database tables if they don't exist
# It uses the metadata from the Base class in db.session
user.Base.metadata.create_all(bind=engine)
note.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Notes API with History + Auth")

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Notes API!"}