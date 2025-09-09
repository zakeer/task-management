from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.repo.user import get_current_active_user
from app.repo.project import get_projects_by_user, create_user_project
from app.db.sessions import get_db

from app.schema import ProjectCreate, ProjectForUserResponse, User

# Create the router
router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=ProjectForUserResponse)
def create_project_for_user(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Create a new project.
    
    The project will be automatically associated with the logged-in user.
    """
    return create_user_project(db=db, project=project, user=current_user)


@router.get("/", response_model=List[ProjectForUserResponse])
def read_user_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    Retrieve all projects for the current logged-in user.
    """
    projects = get_projects_by_user(db, user_id=current_user.id)
    return projects