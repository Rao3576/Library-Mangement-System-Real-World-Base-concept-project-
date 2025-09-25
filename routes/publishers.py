from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import publishers
from repositories.publishers_query import PublisherQuery

router = APIRouter(prefix="/publishers", tags=["Publishers"])


@router.post("/", response_model=publishers.Publisher)
def create_publisher(publisher: publishers.PublisherCreate, db: Session = Depends(get_db)):
    return PublisherQuery.create_publisher_query(publisher, db)


@router.get("/", response_model=list[publishers.Publisher])
def list_publishers(db: Session = Depends(get_db)):
    return PublisherQuery.list_publishers_query(db)


@router.get("/{publisher_id}", response_model=publishers.Publisher)
def get_publisher(publisher_id: str, db: Session = Depends(get_db)):
    publisher = PublisherQuery.get_publisher_query(publisher_id, db)
    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return publisher


@router.put("/{publisher_id}", response_model=publishers.Publisher)
def update_publisher(publisher_id: str, publisher: publishers.PublisherUpdate, db: Session = Depends(get_db)):
    updated = PublisherQuery.update_publisher_query(publisher_id, publisher, db)
    if not updated:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return updated


@router.delete("/{publisher_id}")
def delete_publisher(publisher_id: str, db: Session = Depends(get_db)):
    deleted = PublisherQuery.delete_publisher_query(publisher_id, db)
    if not deleted:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return deleted
