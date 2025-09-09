## Enable Strict Type Checking
setting name: `python.analysis.typeCheckingMode` and enable `strict` option

## Install requirements.txt
```bash
pip install -r requirements.txt 
```

## Start the application
```bash
uvicorn app.main:app --reload
```

For alembic installation please refer: https://alembic.sqlalchemy.org/en/latest/front.html#installation

## Initialize Alembic
```bash
alembic init alembic
```

## Configuration Alembic `env.py` with correct database url config
```python
# import setting
from app.core.config import settings

# Get the database URL from the environment variable
db_url = settings.DATABASE_URL
if not db_url:
    raise ValueError("DATABASE_URL environment variable is not set")

# Set the sqlalchemy.url in the Alembic config
config.set_main_option("sqlalchemy.url", db_url)
```

## import your model's metadata into the `alembic/env.py` script and assign it to the target_metadata variable.
```python
from app.db.base import Base


target_metadata = Base.metadata
```

## !IMPORTANT once defining model, import models into `app/db/base.py`
```python
from app.models import user  # pyright: ignore[reportUnusedImport]
```


## DB Model and Alembic Migration Script
Define Model (DB Tables) and Run Migration command

Syntax
```bash
alembic revision --autogenerate -m "<YOUR MESSAGE>"
```

Example
```bash
alembic revision --autogenerate -m "Create users table"
```

## Apply Migration to Database
```bash
alembic upgrade head
```


Introducing a third table, often called an association table, that links users and projects together.

Alembic Migration Script 📜
After updating your `user.py`, `project.py`, `user_project_association` in models, run the autogenerate command:

```bash
alembic revision --autogenerate -m "Add Project model and user-project relationship"
```

Alembic will detect the new `Project` model and the `user_project_association` table and generate a migration file like this. 

Run upgrade
```bash
alembic upgrade head
```