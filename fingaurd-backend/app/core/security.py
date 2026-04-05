from passlib.context import CryptContext
from jose import jwt
from datetime import datetime,timedelta

SECRET_KEY = "your_secret"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str):

    password = password.strip()

    print("AFTER STRIP:", password)
    print("NEW LENGTH:", len(password))

    if len(password) > 72:
        password = password[:72]
        print("TRUNCATED LENGTH:", len(password))

    return pwd_context.hash(password)  

def verify_password(plain, hashed):
    plain = plain.strip()
    if len(plain) > 72:
        plain = plain[:72]    
    return pwd_context.verify(plain, hashed)

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours = 2)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

