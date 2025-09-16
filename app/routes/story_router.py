from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.db.sessions import get_db
from app.models.story import Story
from app.schemas.story import StoryCreate, StoryRead  # You need these schemas

story_router = APIRouter(prefix="/story", tags=["Story"])

# Create a new story
@story_router.post("/create", response_model=StoryRead)
def create_story(story_in: StoryCreate, db: Session = Depends(get_db)):
    # Check if a story with the same title already exists
    exists = db.query(Story).filter(Story.title == story_in.title).first()
    if exists:
        raise HTTPException(status_code=400, detail="Story with this title already exists")

    story = Story(
        title=story_in.title,
        description=story_in.description,
        epic_id=story_in.epic_id,
        created_at=datetime.utcnow()
    )
    db.add(story)
    db.commit()
    db.refresh(story)
    return story
