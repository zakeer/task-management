from fastapi import FastAPI

from . import models
from .database import engine

app = FastAPI(title="Project Management API")

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Project Management API is running"}
