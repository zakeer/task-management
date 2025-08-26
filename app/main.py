from fastapi import FastAPI

app = FastAPI(title="Project Management API")


@app.get("/")
def root():
    return {"message": "Project Management API is running successfully"}
