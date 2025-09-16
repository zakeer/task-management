from datetime import datetime
from app.db.base import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


# ---------- STORY ----------
class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    epic_id = Column(Integer, ForeignKey("epics.id", ondelete="CASCADE"))
    created_at = Column(DateTime, default=datetime.utcnow)

    epic = relationship("Epic", back_populates="stories")
    tasks = relationship("Task", back_populates="story")
    bugs = relationship("Bug", back_populates="story")
