from datetime import datetime

from app.database import Base
from app.models.association_table import project_members
from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship


# ---------- PROJECT ----------
class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    members = relationship(
        "User", secondary=project_members, back_populates="projects"
    )
    epics = relationship("Epic", back_populates="project")
