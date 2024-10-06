from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.api.v1.controllers.producer_controller import (
    register_producer_controller,
    list_producers_controller,
    remove_producer_controller,
)
from app.api.v1.schemas.producer import ProducerCreate, ProducerResponse

router = APIRouter()


@router.post("/", response_model=ProducerResponse)
def register_producer(producer: ProducerCreate, db: Session = Depends(get_db)):
    return register_producer_controller(db, producer)


@router.get("/", response_model=list[ProducerResponse])
def list_producers(db: Session = Depends(get_db)):
    return list_producers_controller(db)


@router.delete("/{producer_id}")
def remove_producer(producer_id: int, db: Session = Depends(get_db)):
    return remove_producer_controller(db, producer_id)
