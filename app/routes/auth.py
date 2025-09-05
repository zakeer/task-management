from typing import Optional


# import bcrypt
from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)

# from app.core import security
from app.db.sessions import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserRead
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


router = APIRouter(prefix="/user", tags=["User"])


@router.post("/register/owner", response_model=UserRead)
def create_users(user_in: UserCreate, db: Session = Depends(get_db)):
    exists = db.query(User).filter(User.email == user_in.email).first()
    if exists:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed = hash_password(user_in.password)
    user = User(
        email=user_in.email,
        fullname=user_in.fullname,
        username=user_in.username,
        hashed_password=hashed,  # ✅ use hashed_password instead of password
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    
    token_data = {"sub": str(user.id)}
    access_token = create_access_token(token_data)

    return {"access_token": access_token, "token_type": "bearer"}