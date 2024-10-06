from sqlalchemy.orm import Session
from app.models.producer import Producer
from app.api.v1.schemas.producer import ProducerCreate


def create_producer(db: Session, producer: ProducerCreate):
    new_producer = Producer(**producer.dict(), crops=",".join(producer.crops))
    db.add(new_producer)
    db.commit()
    db.refresh(new_producer)
    return new_producer


def get_producers(db: Session):
    return db.query(Producer).all()


def delete_producer(db: Session, producer_id: int):
    producer = db.query(Producer).filter(Producer.id == producer_id).first()
    if producer:
        db.delete(producer)
        db.commit()
        return True
    return False
