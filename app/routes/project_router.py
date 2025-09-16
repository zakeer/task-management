from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from app.db.sessions import get_db
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectRead

project_router = APIRouter(prefix="/projects", tags=["Projects"])


# -------- CREATE PROJECT --------
@project_router.post("/", response_model=ProjectRead)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    new_project = Project(
        name=project.name,
        description=project.description,
        created_at=datetime.utcnow()
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project
