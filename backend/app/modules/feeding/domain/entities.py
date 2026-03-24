from dataclasses import dataclass
from datetime import datetime
from typing import Literal


FeedingMethod = Literal["breast_milk", "formula", "solid_food"]


@dataclass(frozen=True)
class FeedingLog:
    id: str
    baby_id: str
    method: FeedingMethod
    amount_ml: int | None
    occurred_at: datetime
    memo: str | None = None
