from datetime import datetime

from app.db.base import Base
from app.models.enums import TaskStatus  # FIX: import TaskStatus
from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

# app/models/__init__.py
# from .user import User
# from .task import Task


# def create_task_for_user():
#     from .user import User  # import locally

#     user = User()


# ---------- TASK ----------
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    status = Column(Enum(TaskStatus), default=TaskStatus.todo)
    story_id = Column(Integer, ForeignKey("stories.id", ondelete="CASCADE"))
    assignee_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"))
    created_at = Column(DateTime, default=datetime.utcnow)

    story = relationship("Story", back_populates="tasks")
    assignee = relationship("User", back_populates="tasks")
    comments = relationship("Comment", back_populates="task")
