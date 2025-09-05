from app.db.base import Base
from sqlalchemy import Column, ForeignKey, Integer, Table

project_members = Table(
    "project_members",
    Base.metadata,
    Column(
        "project_id", Integer, ForeignKey("projects.id", ondelete="CASCADE")
    ),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE")),
)
