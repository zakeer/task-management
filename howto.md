# DB Migrations

```bash
# Auto generate tables to alembic script
alembic revision --autogenerate -m "initial setup"

# push to DB
alembic upgrade head
```


# Run Tests
```
pytest
```

## Run Tests with Coverage report
```
pytest --cov=. --cov-report=html
```