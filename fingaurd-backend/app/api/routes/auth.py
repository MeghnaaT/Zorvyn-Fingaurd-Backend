from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.core.security import hash_password, verify_password, create_token
from app.dependencies.auth import get_db

router = APIRouter()
@router.post("/register")
def register(data: UserCreate, db: Session = Depends(get_db)):
    user= User(
        email = data.email,
        password= hash_password(data.password),
            role = data.role
    )
    db.add(user)
    db.commit()
    return {"message": "User created"}

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password):
        return {"message": "Invalid credentials"}
    token = create_token({"sub": user.id})
    return {"access_token": token}
