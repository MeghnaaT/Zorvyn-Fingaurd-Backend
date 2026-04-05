from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.models.user import User, User
from app.dependencies.auth import get_db, require_role, get_logged_in_user
from app.services.analytics_service import compute_summary

router = APIRouter()

@router.get("/summary")
def get_summary(
    db: Session = Depends(get_db),
    user: User = Depends(get_logged_in_user)  
):
    if user.role == "admin":
        transactions = db.query(Transaction).all()
    else:
        transactions = db.query(Transaction).filter(
            Transaction.user_id == user.id
        ).all()
    return compute_summary(transactions)