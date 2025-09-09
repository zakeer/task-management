# main.py

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from app.db.sessions import get_db

from app.schema.user import UserBase, UserCreate, Token
from app.utils.auth import verify_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from app.repo import user as user_repo 

router = APIRouter(prefix="/auth", tags=["auth"])

# --- API Endpoints ---

@router.post("/register/", response_model=UserBase)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint to register a new user.
    """
    db_user = user_repo.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return user_repo.create_user(db=db, user=user)


@router.post("/login", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)
):
    """
    Endpoint to login a user and get a JWT token.
    FastAPI's OAuth2PasswordRequestForm requires form data with 'username' and 'password'.
    """
    user = user_repo.get_user_by_username(db, username=form_data.username)
    if not user or not verify_password(form_data.password, str(user.password)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserBase)
async def read_users_me(current_user: UserBase = Depends(user_repo.get_current_active_user)):
    """
    Fetch the current logged in user.
    
    This endpoint is protected. You must include an 'Authorization: Bearer <token>'
    header in your request.
    """
    return current_user