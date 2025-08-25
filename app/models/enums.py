from enum import Enum


class BugSeverity(Enum):
    low = "low"
    medium = "medium"
    high = "high"


class TaskStatus(Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"
