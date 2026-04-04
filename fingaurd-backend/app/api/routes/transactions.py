from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate
from app.dependencies.auth import get_db
from app.dependencies.role import require_role

router = APIRouter()
@router.post("/")
def create_transaction(
    data: TransactionCreate,
    db: Session=Depends(get_db),
    user = Depends(require_role(["admin"]))
):
    tx = Transaction(**data.dict())
    db.add(tx)
    db.commit()
    return {"message": "Created"}

@router.get("/")
def get_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()