from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Enum, Text, Table
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.database import Base


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