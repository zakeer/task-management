from datetime import datetime

from app.db.base import Base
from app.models.association_table import project_members
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    # User credentials
    fullname = Column(String, nullable=True)  # <-- Add this line

    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    # Timestamp
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    projects = relationship(
        "Project", secondary=project_members, back_populates="members"
    )

    tasks = relationship(
        "Task", back_populates="assignee", cascade="all, delete-orphan"
    )

    bugs = relationship(
        "Bug", back_populates="assignee", cascade="all, delete-orphan"
    )

    comments = relationship(
        "Comment", back_populates="author", cascade="all, delete-orphan"
    )
