from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Enum, Text, Table
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.database import Base

# ---------- ASSOCIATION TABLE ----------
project_members = Table(
    "project_members",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE")),
    Column("project_id", Integer, ForeignKey("projects.id", ondelete="CASCADE"))
)
