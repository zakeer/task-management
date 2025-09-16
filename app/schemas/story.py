from pydantic import BaseModel
from typing import Optional

class StoryCreate(BaseModel):
    title: str
    description: Optional[str] = None
    epic_id: int


from datetime import datetime

class StoryRead(BaseModel):
    id: int
    title: str
    description: Optional[str]
    epic_id: int
    created_at: datetime

    class Config:
        orm_mode = True
