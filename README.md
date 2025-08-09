# 🗂 Task Management API – FastAPI, Docker & AWS EC2

A complete **Task Management REST API** built with **FastAPI**, **PostgreSQL**, and **Docker**, deployed on an **AWS EC2** instance.  
This project is designed as a **4-part tutorial series** to guide you from **idea → API → containerization → deployment**.

---

## 📚 Tutorial Series

1. **[Part 1: Planning & Project Setup](docs/part1_planning_setup.md)**  
   Requirements, workflow, local setup, and first endpoint.
2. **Part 2: Building the Core API**  
   Database models, JWT authentication, CRUD for tasks, filtering & search.
3. **Part 3: Containerization & Deployment**  
   Dockerizing the app, running locally, deploying to AWS EC2.
4. **Part 4: Security, Optimization & Enhancements**  
   HTTPS setup, performance tuning, logging, and future features.

---

## 🛠 Tech Stack

- **Backend:** FastAPI (Python 3.11+)
- **Database:** PostgreSQL
- **Authentication:** JWT (JSON Web Token)
- **Containerization:** Docker, Docker Compose
- **Deployment:** AWS EC2 (Ubuntu 22.04 LTS)
- **Documentation:** Swagger/OpenAPI (built-in with FastAPI)

---

## ✨ Features

- User registration & login
- JWT-based authentication
- CRUD operations for tasks
- Task filtering & search
- Modular, production-ready architecture
- Dockerized for portability
- AWS EC2 deployment guide

---

## 📂 Project Structure

```

task-management/
│
├── app/
│   ├── core/            # Config, security, dependencies
│   ├── models/          # SQLAlchemy models
│   ├── schemas/         # Pydantic schemas
│   ├── routes/          # API endpoints
│   ├── services/        # Business logic
│   ├── main.py
│   └── **init**.py
│
├── diagrams/            # UML & architecture diagrams
├── docs/                # Tutorial & reference documentation
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── alembic.ini
├── .env.example
└── README.md

````

---

## 📊 Diagrams

- **System Workflow:** High-level request flow.
- **Database Schema:** User & Task relationships.
- **Use Case Diagram:** Interaction between user & system.
- **Deployment Architecture:** EC2 + Docker + Nginx + Certbot.

Diagrams are stored in the [`diagrams/`](diagrams/) folder.

---

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/zakeer/task-management.git
cd task-management

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn app.main:app --reload
````

Visit API Docs: <br >
➡ Swagger UI: `http://127.0.0.1:8000/docs`<br >
➡ ReDoc: `http://127.0.0.1:8000/redoc`

---

## 📄 License

MIT License © 2025 \[Syed Zakeer Hussain]
