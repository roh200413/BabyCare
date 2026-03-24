from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class FeedingLogCreate(BaseModel):
    baby_id: str
    method: Literal["breast_milk", "formula", "solid_food"]
    amount_ml: int | None = Field(default=None, ge=0)
    occurred_at: datetime
    memo: str | None = Field(default=None, max_length=300)


class FeedingLogResponse(FeedingLogCreate):
    id: str
