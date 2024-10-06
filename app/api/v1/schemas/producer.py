from pydantic import BaseModel, validator
from typing import List


class ProducerCreate(BaseModel):
    cpf_cnpj: str
    name: str
    farm_name: str
    city: str
    state: str
    total_area: float
    agricultural_area: float
    vegetation_area: float
    crops: List[str]

    @validator("cpf_cnpj")
    def validate_cpf_cnpj(cls, value):
        if not (len(value) == 11 or len(value) == 14):
            raise ValueError("Invalid CPF or CNPJ.")
        return value

    @validator("total_area")
    def validate_areas(cls, value, values):
        if values.get("agricultural_area") + values.get("vegetation_area") > value:
            raise ValueError("Sum of areas cannot exceed the total area.")
        return value


class ProducerResponse(ProducerCreate):
    id: int
