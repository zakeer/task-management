from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    fullname: str | None = None


class UserCreate(UserBase):
    password: str
    username: str


class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True
