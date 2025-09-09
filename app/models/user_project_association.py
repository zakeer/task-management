from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.base import Base

# --- Define the Association Table ---
# This table links users to projects in a many-to-many relationship.
# It's defined using SQLAlchemy's Table construct, not a declarative model class.
user_project_association = Table(
    'user_project_association', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('project_id', Integer, ForeignKey('projects.id'), primary_key=True)
)