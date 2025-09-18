from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    id: int
    username: str
    
    class Config:
        from_attributes = True


class UserCreate(UserBase):
    password: str


# Schema for the JWT token response
class Token(BaseModel):
    access_token: str
    token_type: str

# Schema for data embedded within the JWT
class TokenData(BaseModel):
    username: str | None = None
