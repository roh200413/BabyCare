from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_register_device_endpoint() -> None:
    response = client.post(
        "/api/v1/devices/register",
        json={
            "baby_id": "baby_123",
            "device_type": "cry_detector",
            "name": "아기방 소리 센서",
            "location": "nursery",
        },
    )

    body = response.json()
    assert response.status_code == 201
    assert body["device_type"] == "cry_detector"
    assert "cry_detection" in body["capabilities"]


def test_device_status_endpoint() -> None:
    response = client.get("/api/v1/devices/device_demo/status")

    body = response.json()
    assert response.status_code == 200
    assert body["device"]["device_type"] == "camera"
    assert "motion_detection" in body["device"]["capabilities"]
