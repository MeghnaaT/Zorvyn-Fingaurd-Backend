from fastapi import Depends, HTTPException
from app.dependencies.auth import get_logged_in_user
def require_role(allowed_roles):
    def checker(user=Depends(get_logged_in_user)):
        if user.role not in allowed_roles:
            raise HTTPException(status_code=403, detail = "Access denied")
        return user
    return checker