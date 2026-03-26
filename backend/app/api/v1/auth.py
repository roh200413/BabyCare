from fastapi import APIRouter

from app.schemas.auth import LoginRequest, LoginResponse

router = APIRouter()


@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest) -> LoginResponse:
    return LoginResponse(
        access_token=f"dev-token-for-{payload.email}",
        user_id="user_dev_001",
    )
