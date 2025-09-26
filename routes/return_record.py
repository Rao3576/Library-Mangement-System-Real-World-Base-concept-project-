from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import return_record
from repositories.return_record_query import ReturnQuery

router = APIRouter(prefix="/returns", tags=["Returns"])

@router.post("/", response_model=return_record.BookReturn)
def create_return(ret: return_record.BookReturnCreate, db: Session = Depends(get_db)):
    return ReturnQuery.create_return_query(ret, db)

@router.get("/", response_model=list[return_record.BookReturn])
def list_returns(db: Session = Depends(get_db)):
    return ReturnQuery.list_returns_query(db)

@router.get("/{return_id}", response_model=return_record.BookReturn)
def get_return(return_id: str, db: Session = Depends(get_db)):
    r = ReturnQuery.get_return_query(return_id, db)
    if not r:
        raise HTTPException(status_code=404, detail="Return record not found")
    return r

@router.put("/{return_id}", response_model=return_record.BookReturn)
def update_return(return_id: str, ret: return_record.BookReturnUpdate, db: Session = Depends(get_db)):
    updated = ReturnQuery.update_return_query(return_id, ret, db)
    if not updated:
        raise HTTPException(status_code=404, detail="Return record not found")
    return updated

@router.delete("/{return_id}")
def delete_return(return_id: str, db: Session = Depends(get_db)):
    return ReturnQuery.delete_return_query(return_id, db)
