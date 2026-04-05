from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate
from app.dependencies.auth import get_db
from app.dependencies.role import require_role
from app.dependencies.auth import get_logged_in_user
from app.models.user import User
from typing import Optional
from fastapi import Query

router = APIRouter()
@router.post("/")
def create_transaction(
    data: TransactionCreate,
    db: Session=Depends(get_db),
    user: User = Depends(get_logged_in_user)
):
    transaction = Transaction(
        amount=data.amount,
        type=data.type,
        category=data.category,
        note=data.note,
        user_id=user.id
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

@router.get("/")
def get_transactions(
    db: Session = Depends(get_db), 
    user: User= Depends(get_logged_in_user),
    type: Optional[str] = Query(None),
    category: Optional[str] = Query(None)
):
    if user.role ==" admin":
        query = db.query(Transaction)
    else:
        query = db.query(Transaction).filter(
            Transaction.user_id == user.id 
    )
    if type:
        query = query.filter(Transaction.type == type)
    if category:
        query = query.filter(Transaction.category == category)

    return query.all()

@router.put("/{transaction_id}")
def update_transaction(
    transaction_id: int,
    data: TransactionCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_logged_in_user)
):
    if user.role == "admin":
        transaction = db.query(Transaction).filter(
            Transaction.id == transaction_id
        ).first()
    else:
        transaction = db.query(Transaction).filter(
            Transaction.id == transaction_id,
            Transaction.user_id == user.id
        ).first()
    
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    transaction.amount = data.amount
    transaction.type = data.type
    transaction.category = data.category
    transaction.note = data.note
    db.commit()
    db.refresh(transaction)
    return transaction

@ router.delete("/{transaction_id}")
def delete_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_logged_in_user)
):
    if user.role == "admin":
        transaction = db.query(Transaction).filter(
            Transaction.id == transaction_id
        ).first()
    else:
        transaction = db.query(Transaction).filter(
            Transaction.id == transaction_id,
            Transaction.user_id == user.id
        ).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    db.delete(transaction)
    db.commit()
    return {"status": "success", "message": "Transaction deleted"}