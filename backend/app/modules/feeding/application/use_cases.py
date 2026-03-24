from uuid import uuid4

from app.modules.feeding.domain.entities import FeedingLog
from app.schemas.feeding import FeedingLogCreate


class CreateFeedingLogUseCase:
    def execute(self, command: FeedingLogCreate) -> FeedingLog:
        return FeedingLog(
            id=f"feed_{uuid4().hex[:8]}",
            baby_id=command.baby_id,
            method=command.method,
            amount_ml=command.amount_ml,
            occurred_at=command.occurred_at,
            memo=command.memo,
        )
