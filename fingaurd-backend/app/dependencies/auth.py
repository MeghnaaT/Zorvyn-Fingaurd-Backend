from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.core.security import SECRET_KEY, ALGORITHM

security = HTTPBearer()  

def get_logged_in_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session =Depends(get_db)
):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail = "Invalid token")
        
        user = db.query(User).filter(User.email ==email).first()
        if user is None:
            raise HTTPException(status_code=401, detail = "User not found")
        return user
    except:
        raise HTTPException(status_code=401, detail = "Invalid token")

def require_role(required_role: str):
    def role_checker(user: User = Depends(get_logged_in_user)):
        if user.role!=required_role:
            raise HTTPException(status_code=403, detail = "Forbidden")
        return user
    return role_checker
        