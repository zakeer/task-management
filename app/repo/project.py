from sqlalchemy.orm import Session
from app.models.project import Project
from app.schema import ProjectCreate, User as UserBase

def get_projects_by_user(db: Session, user_id: int):
    """Fetches all projects associated with a specific user."""
    return db.query(Project).filter(Project.users.any(id=user_id)).all()

def create_user_project(db: Session, project: ProjectCreate, user: UserBase):
    """Creates a new project and associates it with the creating user."""
    if not user:
        return None # Or raise an exception

    # Create the project instance
    db_project = Project(**project.model_dump())
    
    # Add the user to the project's list of users
    db_project.users.append(user)
    
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project