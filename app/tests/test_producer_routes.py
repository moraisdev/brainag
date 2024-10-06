from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app
from app.models.producer import Producer

client = TestClient(app)


@patch("app.services.producer_service.create_producer")
def test_register_producer(mock_create_producer):
    mock_create_producer.return_value = Producer(
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

    response = client.post(
        "/producers/",
        json={
            "cpf_cnpj": "12345678901",
            "name": "John Doe",
            "farm_name": "Green Farm",
            "city": "Rural City",
            "state": "MG",
            "total_area": 100.0,
            "agricultural_area": 60.0,
            "vegetation_area": 40.0,
            "crops": ["Soybean", "Corn"],
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    mock_create_producer.assert_called_once()


@patch("app.services.producer_service.get_producers")
def test_list_producers(mock_get_producers):
    mock_get_producers.return_value = [
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

    response = client.get("/producers/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "John Doe"
    mock_get_producers.assert_called_once()


@patch("app.services.producer_service.delete_producer")
def test_remove_producer(mock_delete_producer):
    mock_delete_producer.return_value = True

    response = client.delete("/producers/1")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Producer successfully removed"
    mock_delete_producer.assert_called_once_with(mock.ANY, 1)
