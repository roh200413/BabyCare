from fastapi import APIRouter, Query

from app.schemas.rooms import RoomParticipant, RoomStateResponse

router = APIRouter(prefix="/api/rooms", tags=["rooms"])


@router.get("/{room_code}", response_model=RoomStateResponse)
def get_room(room_code: str, player_id: str | None = Query(default=None, alias="playerId")) -> RoomStateResponse:
    participants = []
    if player_id:
        participants.append(RoomParticipant(player_id=player_id, role="viewer"))

    return RoomStateResponse(
        room_code=room_code,
        player_id=player_id,
        found=False,
        status="pending",
        participants=participants,
        message="Room API scaffold is active. Implement persistence/join flow next.",
    )
