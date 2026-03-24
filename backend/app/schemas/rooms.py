from pydantic import BaseModel


class RoomParticipant(BaseModel):
    player_id: str
    role: str


class RoomStateResponse(BaseModel):
    room_code: str
    player_id: str | None = None
    found: bool
    status: str
    participants: list[RoomParticipant] = []
    message: str
