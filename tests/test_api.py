from fastapi.testclient import TestClient

from orders_api.main import app

client = TestClient(app)


def test_create_and_get():
    body = {"id": "x1", "customer_id": "c1", "lines": [{"sku": "A", "quantity": 1, "unit_price": 100}]}
    assert client.post("/orders", json=body).status_code == 201
    assert client.get("/orders/x1").json()["id"] == "x1"
