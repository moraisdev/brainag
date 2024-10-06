from sqlalchemy import Column, String, Integer, Float
from app.db.database import Base


class Producer(Base):
    __tablename__ = "producers"

    id = Column(Integer, primary_key=True, index=True)
    cpf_cnpj = Column(String, unique=True, index=True)
    name = Column(String)
    farm_name = Column(String)
    city = Column(String)
    state = Column(String)
    total_area = Column(Float)
    agricultural_area = Column(Float)
    vegetation_area = Column(Float)
    crops = Column(String)
