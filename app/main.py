from app.routes.auth import router as user_router
from fastapi import FastAPI

app = FastAPI(title="Project Management API")

# Include your router
app.include_router(user_router)


@app.get("/")
def root():
    return {"message": "Project Management API is running successfully"}
