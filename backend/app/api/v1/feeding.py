from fastapi import APIRouter, status

from app.modules.feeding.application.use_cases import CreateFeedingLogUseCase
from app.schemas.feeding import FeedingLogCreate, FeedingLogResponse

router = APIRouter()
create_feeding_log_use_case = CreateFeedingLogUseCase()


@router.post("", response_model=FeedingLogResponse, status_code=status.HTTP_201_CREATED)
def create_feeding_log(payload: FeedingLogCreate) -> FeedingLogResponse:
    feeding_log = create_feeding_log_use_case.execute(payload)
    return FeedingLogResponse(**feeding_log.__dict__)
