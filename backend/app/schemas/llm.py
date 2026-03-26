from datetime import datetime
from typing import Literal

from pydantic import BaseModel


class ParseRecordRequest(BaseModel):
    baby_id: str
    text: str


class ParsedRecord(BaseModel):
    domain: Literal["feeding"]
    confidence: float
    occurred_at: datetime
    payload: dict[str, object]
    safety_note: str
