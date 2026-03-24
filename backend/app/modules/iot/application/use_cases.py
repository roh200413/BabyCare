from datetime import datetime, timezone
from uuid import uuid4

from app.modules.iot.domain.entities import Device, DeviceReading, DeviceType
from app.schemas.iot import DeviceReadingCreate, DeviceRegisterRequest


class RegisterDeviceUseCase:
    def execute(self, command: DeviceRegisterRequest) -> Device:
        return Device(
            id=f"device_{uuid4().hex[:8]}",
            baby_id=command.baby_id,
            device_type=command.device_type,
            name=command.name,
            location=command.location,
            status="online",
            capabilities=_capabilities_for(command.device_type),
        )


class CreateDeviceReadingUseCase:
    def execute(self, device_id: str, command: DeviceReadingCreate) -> DeviceReading:
        return DeviceReading(
            id=f"reading_{uuid4().hex[:8]}",
            device_id=device_id,
            recorded_at=command.recorded_at,
            temperature_c=command.temperature_c,
            humidity_pct=command.humidity_pct,
            air_quality_index=command.air_quality_index,
            sound_level_db=command.sound_level_db,
            cry_detected=command.cry_detected,
            motion_detected=command.motion_detected,
        )


class GetDeviceStatusUseCase:
    def execute(self, device_id: str) -> tuple[Device, DeviceReading, list[str]]:
        device = Device(
            id=device_id,
            baby_id="baby_demo_001",
            device_type="camera",
            name="아기방 캠",
            location="nursery",
            status="online",
            capabilities=_capabilities_for("camera"),
        )
        reading = DeviceReading(
            id="reading_demo_001",
            device_id=device_id,
            recorded_at=datetime.now(timezone.utc),
            temperature_c=24.1,
            humidity_pct=46.5,
            air_quality_index=18,
            sound_level_db=42.0,
            cry_detected=False,
            motion_detected=True,
        )
        alerts: list[str] = []
        if reading.sound_level_db and reading.sound_level_db > 65:
            alerts.append("소음 수치가 높습니다.")
        if reading.cry_detected:
            alerts.append("울음 감지가 발생했습니다.")
        return device, reading, alerts


def _capabilities_for(device_type: DeviceType) -> list[str]:
    if device_type == "environment_sensor":
        return ["temperature", "humidity", "air_quality"]
    if device_type == "cry_detector":
        return ["sound_level", "cry_detection"]
    return ["video_stream", "motion_detection", "snapshot"]
