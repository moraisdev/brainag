from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.api.v1.schemas.producer import ProducerCreate
from app.services.producer_service import (
    create_producer,
    get_producers,
    delete_producer,
)


def register_producer_controller(db: Session, producer: ProducerCreate):
    try:
        return create_producer(db, producer)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def list_producers_controller(db: Session):
    return get_producers(db)


def remove_producer_controller(db: Session, producer_id: int):
    success = delete_producer(db, producer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Producer not found")
    return {"message": "Producer successfully removed"}
