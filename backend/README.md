# BabyCare Backend

초기 FastAPI 백엔드 스캐폴드입니다.

## 실행

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
uvicorn app.main:app --reload
```

## 제공 엔드포인트

- `GET /healthz`
- `GET /api/v1`
- `POST /api/v1/auth/login`
- `GET /api/v1/babies/{baby_id}`
- `POST /api/v1/feeding-logs`
- `POST /api/v1/llm/parse-record`
- `POST /api/v1/devices/register`
- `POST /api/v1/devices/{device_id}/readings`
- `GET /api/v1/devices/{device_id}/status`


## IoT 확장 방향

- 환경 센서: 온도, 습도, 공기질
- 소리 감지: 데시벨, 울음 감지 이벤트
- 캠 연동: 움직임 감지, 스냅샷, 향후 스트리밍 연계


## DDD 구조

- API(Presentation): `app/api/`
- Input/Output Schema: `app/schemas/`
- Domain/Application Module: `app/modules/`
- 설계 문서: [`docs/ddd.md`](docs/ddd.md)
