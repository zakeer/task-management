from datetime import datetime

from app.db.base import Base
from app.models.association_table import project_members
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship


# ---------- USER ----------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    projects = relationship(
        "Project", secondary=project_members, back_populates="members"
    )
    tasks = relationship("Task", back_populates="assignee")
    bugs = relationship("Bug", back_populates="assignee")
    comments = relationship("Comment", back_populates="author")
