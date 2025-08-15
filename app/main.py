from fastapi import FastAPI
from .database import engine
from . import models

app = FastAPI(title="Project Management API")

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Project Management API is running"}