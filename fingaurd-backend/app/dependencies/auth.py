from fastapi import Depends, HTTPException
from jose import jwt
from app.db.session import SessionLocal
from app.models.user import User

SECRET_KEY = "your_secret"
ALGORITHM = "HS256"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()   

def get_current_user(token: str, db=Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, alogorithms=[ALGORITHM])
        user = db.query(User).filter(User.email ==payload["sub"]).first()
        return user
    except:
        raise HTTPException(status_code=401, detail = "Invalid token")
        