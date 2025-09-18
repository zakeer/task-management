from datetime import datetime

from app.db.base import Base
from sqlalchemy import Column, DateTime, Integer, String

from app.schema.user import UserBase


# ---------- USER ----------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now, nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.created_at is None:
            self.created_at = datetime.now()


    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
    
    def to_dict(self):
        return UserBase(
            # id=getattr(self, "id", 0),
            id=self.id if self.id is not None else 0,
            email=str(getattr(self, "email", "")),
            username=str(getattr(self, "username", ""))
        )

