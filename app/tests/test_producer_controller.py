import pytest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
from app.api.v1.schemas.producer import ProducerCreate
from app.api.v1.controllers.producer_controller import (
    register_producer_controller,
    list_producers_controller,
    remove_producer_controller,
)
from app.models.producer import Producer


@pytest.fixture
def mock_db():
    db = MagicMock(spec=Session)
    return db


def test_register_producer(mock_db):
    producer_data = ProducerCreate(
        cpf_cnpj="12345678901",
        name="John Doe",
        farm_name="Green Farm",
        city="Rural City",
        state="MG",
        total_area=100.0,
        agricultural_area=60.0,
        vegetation_area=40.0,
        crops=["Soybean", "Corn"],
    )

    mock_db.add = MagicMock()
    mock_db.commit = MagicMock()
    mock_db.refresh = MagicMock()

    result = register_producer_controller(mock_db, producer_data)

    assert result.name == "John Doe"
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()


def test_list_producers(mock_db):
    mock_db.query.return_value.all.return_value = [
        Producer(
            id=1,
            cpf_cnpj="12345678901",
            name="John Doe",
            farm_name="Green Farm",
            city="Rural City",
            state="MG",
            total_area=100.0,
            agricultural_area=60.0,
            vegetation_area=40.0,
            crops="Soybean,Corn",
        )
    ]

    producers = list_producers_controller(mock_db)
    assert len(producers) == 1
    assert producers[0].name == "John Doe"


def test_remove_producer(mock_db):
    mock_db.query.return_value.filter.return_value.first.return_value = Producer(id=1)
    mock_db.delete = MagicMock()
    mock_db.commit = MagicMock()

    result = remove_producer_controller(mock_db, 1)

    assert result["message"] == "Producer successfully removed"
    mock_db.delete.assert_called_once()
    mock_db.commit.assert_called_once()
