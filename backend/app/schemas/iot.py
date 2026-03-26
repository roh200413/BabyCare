from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


class DeviceRegisterRequest(BaseModel):
    baby_id: str
    device_type: Literal["environment_sensor", "cry_detector", "camera"]
    name: str = Field(min_length=2, max_length=50)
    location: str | None = Field(default=None, max_length=100)


class DeviceSummary(BaseModel):
    id: str
    baby_id: str
    device_type: Literal["environment_sensor", "cry_detector", "camera"]
    name: str
    location: str | None = None
    status: Literal["online", "offline", "idle"]
    capabilities: list[str]


class DeviceReadingCreate(BaseModel):
    recorded_at: datetime
    temperature_c: float | None = None
    humidity_pct: float | None = None
    air_quality_index: int | None = None
    sound_level_db: float | None = None
    cry_detected: bool = False
    motion_detected: bool = False


class DeviceReadingResponse(DeviceReadingCreate):
    id: str
    device_id: str


class DeviceStatusResponse(BaseModel):
    device: DeviceSummary
    latest_reading: DeviceReadingResponse | None = None
    alerts: list[str] = []
