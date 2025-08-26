# DB Migrations

```bash
# Auto generate tables to alembic script
alembic revision --autogenerate -m "initial setup"

# push to DB
alembic upgrade head
```