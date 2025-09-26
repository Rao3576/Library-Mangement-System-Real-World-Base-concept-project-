from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import transaction
from repositories.transaction_query import TransactionQuery

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/", response_model=transaction.Transaction)
def create_transaction(tx: transaction.TransactionCreate, db: Session = Depends(get_db)):
    return TransactionQuery.create_transaction_query(tx, db)

@router.get("/", response_model=list[transaction.Transaction])
def list_transactions(db: Session = Depends(get_db)):
    return TransactionQuery.list_transactions_query(db)

@router.get("/{tx_id}", response_model=transaction.Transaction)
def get_transaction(tx_id: str, db: Session = Depends(get_db)):
    tx = TransactionQuery.get_transaction_query(tx_id, db)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx

@router.put("/{tx_id}", response_model=transaction.Transaction)
def update_transaction(tx_id: str, tx: transaction.TransactionUpdate, db: Session = Depends(get_db)):
    updated = TransactionQuery.update_transaction_query(tx_id, tx, db)
    if not updated:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return updated

@router.delete("/{tx_id}")
def delete_transaction(tx_id: str, db: Session = Depends(get_db)):
    return TransactionQuery.delete_transaction_query(tx_id, db)
