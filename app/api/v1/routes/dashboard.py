from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.producer import Producer
from sqlalchemy import func

router = APIRouter()

@router.get("/totals")
def get_totals(db: Session = Depends(get_db)):
    total_farms = db.query(func.count(Producer.id)).scalar()
    total_area = db.query(func.sum(Producer.total_area)).scalar()
    return {
        "total_farms": total_farms,
        "total_area": total_area
    }

@router.get("/state-distribution")
def get_farms_by_state(db: Session = Depends(get_db)):
    state_distribution = db.query(Producer.state, func.count(Producer.id)) \
        .group_by(Producer.state).all()
    return [{"state": state, "total_farms": total_farms} for state, total_farms in state_distribution]

@router.get("/crop-distribution")
def get_farms_by_crop(db: Session = Depends(get_db)):
    crop_distribution = db.query(
        func.unnest(func.string_to_array(Producer.crops, ',')).label("crop"),
        func.count(Producer.id)
    ).group_by("crop").all()
    return [{"crop": crop, "total_farms": total_farms} for crop, total_farms in crop_distribution]

@router.get("/land-use")
def get_land_use_distribution(db: Session = Depends(get_db)):
    land_use = db.query(
        func.sum(Producer.agricultural_area).label("total_agricultural"),
        func.sum(Producer.vegetation_area).label("total_vegetation")
    ).first()
    return {
        "total_agricultural_area": land_use.total_agricultural,
        "total_vegetation_area": land_use.total_vegetation
    }