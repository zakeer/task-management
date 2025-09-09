from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from app.models.user import User
from app.schema import UserCreate, TokenData
from app.db.sessions import get_db
from app.utils.auth import get_password_hash, oauth2_scheme, SECRET_KEY, ALGORITHM

def get_user_by_username(db: Session, username: str): 
    """Fetches a user by their username."""
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    """Creates a new user in the database."""
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username, 
        email=user.email, 
        password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

async def get_current_active_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> User:
    """
    Dependency to get the current user from a JWT token.
    Validates token, decodes it, and fetches the user from the database.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    if not token_data:
        raise credentials_exception
    
    user = get_user_by_username(db, username=str(token_data.username))
    if user is None:
        raise credentials_exception
    return user