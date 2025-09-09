from datetime import datetime

from app.db.base import Base
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from app.models.user_project_association import user_project_association

# ---------- USER ----------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    # Add this relationship to link users to their projects
    projects = relationship(
        "Project",
        secondary=user_project_association,
        back_populates="users"
    )

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
    