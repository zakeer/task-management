## Step for application run

FastAPI run server without docker
```bash
uvicorn app.main:app --reload
```

Verify the app is running or not by checking http://localhost:8000/docs

Run Server using Docker
```bash
# Build the docker
docker build -t fastapi-app .

# Run the docker container
docker run -d -p 8000:8000 --name fastapi-container fastapi-app

# Verify container is running
docker ps

```

```
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS          PORTS                                         NAMES
ced7f1d85b28   fastapi-app   "uvicorn app.main:ap…"   22 seconds ago   Up 22 seconds   0.0.0.0:8000->8000/tcp, [::]:8000->8000/tcp   fastapi-container
```
