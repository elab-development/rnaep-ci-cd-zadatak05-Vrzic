from fastapi.testclient import TestClient
from payment.main import app

client = TestClient(app)

def test_get_nonexistent_order():

    response = client.get("/orders/999999")

    assert response.status_code == 404