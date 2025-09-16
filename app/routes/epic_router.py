from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.db.sessions import get_db
from app.models.epic import Epic
from app.schemas.epic import EpicCreate, EpicRead 

epic_router = APIRouter(prefix="/epic", tags=["Epic"])

# Create a new Epic
@epic_router.post("/create", response_model=EpicRead)
def create_epic(epic_in: EpicCreate, db: Session = Depends(get_db)):
    exists = db.query(Epic).filter(
        Epic.title == epic_in.title,
        Epic.project_id == epic_in.project_id
    ).first()

    if exists:
        raise HTTPException(status_code=400, detail="Epic with this title already exists in this project")

    epic = Epic(
        title=epic_in.title,
        description=epic_in.description,
        project_id=epic_in.project_id,
        created_at=datetime.utcnow()
    )

    db.add(epic)
    db.commit()
    db.refresh(epic)
    return epic
