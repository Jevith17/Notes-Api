# app/models/user.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    # This creates the relationship with the Note model.
    # 'back_populates' links it to the 'owner' attribute in the Note model.
    notes = relationship("Note", back_populates="owner")