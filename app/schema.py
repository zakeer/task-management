from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime



"""
User Schemas
"""
class UserBase(BaseModel):
    email: EmailStr
    id: int
    username: str
    
    class Config:
        from_attributes = True


class UserCreate(UserBase):
    password: str

class User(UserBase):
    projects: List['ProjectForUserResponse'] = [] # List of projects this user is part of



""" Project Schemas """
class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None

class ProjectForUserResponse(ProjectBase):
    """A simplified Project schema that does NOT include the 'users' field."""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int
    created_at: datetime
    users: List['User'] = [] # Forward reference to User schema

    class Config:
        from_attributes = True


"""
Token Schemas
"""
# Schema for the JWT token response
class Token(BaseModel):
    access_token: str
    token_type: str

# Schema for data embedded within the JWT
class TokenData(BaseModel):
    username: str | None = None
