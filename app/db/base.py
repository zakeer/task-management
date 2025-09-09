from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

from app.models import user  # pyright: ignore[reportUnusedImport]
from app.models import project  # pyright: ignore[reportUnusedImport]
from app.models import user_project_association  # pyright: ignore[reportUnusedImport]