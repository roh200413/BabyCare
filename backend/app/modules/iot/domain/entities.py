from dataclasses import dataclass, field
from datetime import datetime
from typing import Literal


DeviceType = Literal["environment_sensor", "cry_detector", "camera"]
DeviceStatus = Literal["online", "offline", "idle"]


@dataclass(frozen=True)
class Device:
    id: str
    baby_id: str
    device_type: DeviceType
    name: str
    location: str | None
    status: DeviceStatus
    capabilities: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class DeviceReading:
    id: str
    device_id: str
    recorded_at: datetime
    temperature_c: float | None = None
    humidity_pct: float | None = None
    air_quality_index: int | None = None
    sound_level_db: float | None = None
    cry_detected: bool = False
    motion_detected: bool = False
