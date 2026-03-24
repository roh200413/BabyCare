from fastapi import APIRouter

from app.api.v1 import auth, babies, feeding, iot, llm

router = APIRouter()
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(babies.router, prefix="/babies", tags=["babies"])
router.include_router(feeding.router, prefix="/feeding-logs", tags=["feeding"])
router.include_router(llm.router, prefix="/llm", tags=["llm"])
router.include_router(iot.router, prefix="/devices", tags=["iot"])


@router.get("")
def api_index() -> dict[str, object]:
    return {
        "message": "BabyCare API v1",
        "domains": ["auth", "babies", "feeding", "llm", "iot"],
    }
