from datetime import datetime

from app.db.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    task_id = Column(
        Integer, ForeignKey("tasks.id", ondelete="CASCADE"), nullable=True
    )
    bug_id = Column(
        Integer, ForeignKey("bugs.id", ondelete="CASCADE"), nullable=True
    )

    author = relationship("User", back_populates="comments")
    task = relationship("Task", back_populates="comments")
    bug = relationship("Bug", back_populates="comments")
