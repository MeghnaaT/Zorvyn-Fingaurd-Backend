from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.dependencies.auth import get_db
from app.services.analytics_service import compute_summary

router = APIRouter()
@router.get("/overview")
def overview(db: Session= Depends(get_db)):
    transactions=db.query(Transaction).all()
    return compute_summary(transactions)
