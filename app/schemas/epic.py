from pydantic import BaseModel
from datetime import datetime

class EpicCreate(BaseModel):
    title: str
    description: str | None = None
    project_id: int

class EpicRead(BaseModel):
    id: int
    title: str
    description: str | None = None
    project_id: int
    created_at: datetime

    class Config:
        from_attributes = True  