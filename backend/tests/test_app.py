from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthcheck() -> None:
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_api_index() -> None:
    response = client.get("/api/v1")

    assert response.status_code == 200
    assert "domains" in response.json()


def test_parse_record_endpoint() -> None:
    response = client.post(
        "/api/v1/llm/parse-record",
        json={"baby_id": "baby_123", "text": "11시 20분에 분유 90ml 먹었어"},
    )

    body = response.json()
    assert response.status_code == 200
    assert body["domain"] == "feeding"
    assert body["payload"]["amount_ml"] == 90
