from fastapi import APIRouter, status

from app.modules.iot.application.use_cases import (
    CreateDeviceReadingUseCase,
    GetDeviceStatusUseCase,
    RegisterDeviceUseCase,
)
from app.schemas.iot import (
    DeviceReadingCreate,
    DeviceReadingResponse,
    DeviceRegisterRequest,
    DeviceStatusResponse,
    DeviceSummary,
)

router = APIRouter()
register_device_use_case = RegisterDeviceUseCase()
create_device_reading_use_case = CreateDeviceReadingUseCase()
get_device_status_use_case = GetDeviceStatusUseCase()


@router.post("/register", response_model=DeviceSummary, status_code=status.HTTP_201_CREATED)
def register_device(payload: DeviceRegisterRequest) -> DeviceSummary:
    device = register_device_use_case.execute(payload)
    return DeviceSummary(**device.__dict__)


@router.post("/{device_id}/readings", response_model=DeviceReadingResponse, status_code=status.HTTP_201_CREATED)
def create_device_reading(device_id: str, payload: DeviceReadingCreate) -> DeviceReadingResponse:
    reading = create_device_reading_use_case.execute(device_id, payload)
    return DeviceReadingResponse(**reading.__dict__)


@router.get("/{device_id}/status", response_model=DeviceStatusResponse)
def get_device_status(device_id: str) -> DeviceStatusResponse:
    device, latest_reading, alerts = get_device_status_use_case.execute(device_id)
    return DeviceStatusResponse(
        device=DeviceSummary(**device.__dict__),
        latest_reading=DeviceReadingResponse(**latest_reading.__dict__),
        alerts=alerts,
    )
