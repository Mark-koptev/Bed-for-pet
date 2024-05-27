from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import user as user_model
from schemas import user as user_schema
from crud import user as user_crud
from database.database import get_db
router = APIRouter()


@router.post("/", response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, user=user)


@router.get('/{email}', response_model=user_schema.User)
def get_user_by_email(email: str, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_email(db, email=email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
