from app.routes.auth import router as user_router
from app.routes.story_router import story_router
from app.routes.epic_router import epic_router
from fastapi import FastAPI
from app.routes.project_router import project_router

app = FastAPI()

from fastapi import FastAPI

app = FastAPI(title="Project Management API")

# Include your router
app.include_router(user_router)
app.include_router(story_router)
app.include_router(epic_router)
app.include_router(project_router)


@app.get("/")
def root():
    return {"message": "Project Management API is running successfully"}
