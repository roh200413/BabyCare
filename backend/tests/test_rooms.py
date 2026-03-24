from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_room_scaffold_endpoint() -> None:
    response = client.get('/api/rooms/AXLXRC', params={'playerId': '14cb9ca1'})

    assert response.status_code == 200
    body = response.json()
    assert body['room_code'] == 'AXLXRC'
    assert body['player_id'] == '14cb9ca1'
    assert body['status'] == 'pending'
