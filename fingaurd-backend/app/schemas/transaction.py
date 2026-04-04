from pydantic import BaseModel
from typing import Optional
class TransactionCreate(BaseModel):
    amount:float
    type:str
    category:str
    note: Optional[str] = None
    