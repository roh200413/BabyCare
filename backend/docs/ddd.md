# BabyCare Backend DDD 초안

## 목표

BabyCare 백엔드는 기능이 늘어날수록 `라우터에 로직이 몰리는 구조`를 피하고,
도메인별로 책임을 분리하는 **DDD(도메인 주도 설계) 스타일**로 확장합니다.

## 기본 레이어

```text
app/
  api/                # FastAPI 라우터, 요청/응답 매핑
  schemas/            # 외부 입출력 스키마(Pydantic)
  modules/
    feeding/
      domain/         # 도메인 엔티티, 규칙
      application/    # 유스케이스
    iot/
      domain/
      application/
  core/               # 설정, 공통 인프라 진입점
```

## 레이어 책임

### 1. API / Presentation

- HTTP 엔드포인트 정의
- 요청 검증 결과를 유스케이스로 전달
- 도메인 결과를 응답 스키마로 변환

### 2. Application

- 유스케이스 실행
- 트랜잭션/권한/오케스트레이션 중심
- 여러 도메인 객체와 리포지토리를 조합

### 3. Domain

- 핵심 비즈니스 개념 표현
- 엔티티, 밸류 오브젝트, 도메인 규칙
- 프레임워크 의존 최소화

## 현재 적용 도메인

### Feeding

- `FeedingLog`를 도메인 엔티티로 분리
- `CreateFeedingLogUseCase`에서 생성 책임 담당

### IoT

- `Device`, `DeviceReading` 도메인 엔티티 분리
- `RegisterDeviceUseCase`, `CreateDeviceReadingUseCase`, `GetDeviceStatusUseCase`로 센서/캠 흐름 분리
- 향후 `cry events`, `camera snapshots`, `stream sessions` 같은 하위 도메인 확장 가능

## 다음 단계 제안

1. `repositories/` 인터페이스를 도메인별로 추가
2. SQLAlchemy 모델과 도메인 엔티티 매퍼 분리
3. LLM 파서도 `llm` 모듈의 application/domain으로 이동
4. 알림, 가족 권한, 앨범을 동일 패턴으로 확장
