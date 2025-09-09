from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.user_project_association import user_project_association

# --- Define the new Project Model ---
class Project(Base):
    """
    Project Model
    
    Represents a project in the 'projects' table.
    """
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(
        DateTime, 
        nullable=False, 
        server_default=func.now()
    )

    # Relationship to the User model through the association table
    users = relationship(
        "User",
        secondary=user_project_association,
        back_populates="projects"
    )
