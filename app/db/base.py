from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from app.models import user, task, story, project, epic, comment, bug, association_table
