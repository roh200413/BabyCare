from datetime import date

from pydantic import BaseModel


class BabySummary(BaseModel):
    id: str
    name: str
    birth_date: date
    age_days: int
