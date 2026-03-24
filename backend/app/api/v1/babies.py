from datetime import date

from fastapi import APIRouter

from app.schemas.baby import BabySummary

router = APIRouter()


@router.get("/{baby_id}", response_model=BabySummary)
def get_baby(baby_id: str) -> BabySummary:
    birth_date = date(2025, 12, 1)
    age_days = (date.today() - birth_date).days
    return BabySummary(
        id=baby_id,
        name="하린",
        birth_date=birth_date,
        age_days=age_days,
    )
