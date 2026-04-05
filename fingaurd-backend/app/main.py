from fastapi import FastAPI
from app.db.session import engine
from app.db.base import Base
from app.api.routes import auth, transactions, analytics
from fastapi.security import HTTPBearer
security = HTTPBearer()

Base.metadata.create_all(bind=engine)
app = FastAPI(tittle="FinGaurd API")
app.include_router(auth.router, prefix="/auth", tags = ["Auth"])
app.include_router(transactions.router, prefix="/transactions", tags = ["Transactions"])
app.include_router(analytics.router, prefix="/analytics", tags =["Analytics"])

@app.get("/")
def root():
    return {"message": "API running"}