from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db.base import Base

class Transaction(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    type = Column(String)
    category = Column(String)
    note = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)