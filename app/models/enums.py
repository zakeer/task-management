from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Enum, Text, Table
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.database import Base

# ---------- ENUMS ----------
class BugSeverity(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"

class TaskStatus(str, enum.Enum):
    todo = "To Do"
    in_progress = "In Progress"
    done = "Done"