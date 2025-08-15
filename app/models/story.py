from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Enum, Text, Table
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.database import Base


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
