# from fastapi import APIRouter, Depends, Query
# from sqlalchemy.orm import Session
# from database import get_db
# from repositories.master_lookup import MasterLookupQuery

# router = APIRouter(prefix="/built-in-method", tags=["MasterLookup"])

# @router.get("/")
# def get_all_master_lookup(
#     filter: str = Query(None, description="Optional filter to search by name across all models"),
#     db: Session = Depends(get_db)
# ):
#     return MasterLookupQuery.get_all_master_data(db, filter)
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import get_db
from repositories.master_lookup import MasterLookupQuery

router = APIRouter(prefix="/master-lookup", tags=["MasterLookup"])

@router.get("/")
def master_lookup(
    model: str = Query(..., description="Entity to search (students, books, authors, publishers, employees)"),
    field: str = Query(..., description="Field name in the selected model"),
    filter: str = Query(None, description="Optional search term for filtering"),
    db: Session = Depends(get_db)
):
   return MasterLookupQuery.get_all_master_data(db=db, filter_name=filter)

