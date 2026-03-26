from datetime import datetime, timezone
import re

from fastapi import APIRouter

from app.schemas.llm import ParseRecordRequest, ParsedRecord

router = APIRouter()

_AMOUNT_PATTERN = re.compile(r"(\d+)\s*ml", re.IGNORECASE)


@router.post("/parse-record", response_model=ParsedRecord)
def parse_record(payload: ParseRecordRequest) -> ParsedRecord:
    amount_match = _AMOUNT_PATTERN.search(payload.text)
    amount_ml = int(amount_match.group(1)) if amount_match else None

    return ParsedRecord(
        domain="feeding",
        confidence=0.71 if amount_ml is not None else 0.42,
        occurred_at=datetime.now(timezone.utc),
        payload={
            "baby_id": payload.baby_id,
            "method": "formula" if "분유" in payload.text else "breast_milk",
            "amount_ml": amount_ml,
            "original_text": payload.text,
        },
        safety_note="의료적 진단이 아닌 기록 보조 결과이며, 정확한 판단은 전문가 상담이 필요합니다.",
    )
