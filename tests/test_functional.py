from fastapi.testclient import TestClient
from payment.main import app
from unittest.mock import patch, AsyncMock

client = TestClient(app)

def test_create_order_invalid_product():

    mock_response = AsyncMock()
    mock_response.status_code = 400

    with patch("httpx.AsyncClient.get", return_value=mock_response):

        response = client.post(
            "/orders",
            json={
                "id": "999",
                "quantity": 1
            }
        )

        assert response.status_code == 400