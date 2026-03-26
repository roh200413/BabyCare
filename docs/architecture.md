# BabyCare 제품/아키텍처 설계 초안

## 1. 서비스 구조

### 1-1. 제품 구조

- **BabyCare**: 전체 서비스 플랫폼
- **빠기스**: 앱 안에 들어가는 육아 특화 LLM 에이전트

### 빠기스 역할

- 육아 기록 자연어 입력
- 수면/수유/배변/체온 데이터 요약
- 주간 리포트 생성
- 부모 질문 응답
- 이상 패턴 감지 보조
- 사진/기록 기반 추억 코멘트 생성

## 2. 사용자 시나리오

### 앱 사용자

- 엄마/아빠가 앱에서 수유, 수면, 배변, 체온 기록
- 자연어 입력 예시: `11시 20분에 분유 90ml 먹었어`
- 사진 촬영 후 성장 이벤트로 저장
- 홈에서 오늘 현황 확인
- 알림 수신
- IoT 센서 연동 시 아기방 상태 확인

### 웹 사용자

- 큰 화면에서 사진첩 열람
- 월별/이벤트별 앨범 보기
- 성장 타임라인 보기
- 가족 구성원이 공유 링크 또는 계정으로 접속
- 인쇄용/보관용 리포트 열람

## 3. 기능 정의

### 3-1. 앱(Flutter) 핵심 기능

#### A. 육아 기록

- 수유 기록: 모유/분유/이유식, 시간, 양, 메모
- 수면 기록: 시작/종료, 자동/수동 입력
- 배변/기저귀 기록: 소변/대변/혼합, 상태 메모
- 건강 기록: 체온, 몸무게, 키, 약 복용
- 일정 기록: 병원 예약, 예방접종, 검사 일정

#### B. 빠기스 LLM

- 자연어 기록 저장
- 대화형 질의응답
- 주간 요약
- 월령 기반 가이드
- 이상 징후 참고 알림 문구 생성
- 감성 메시지 생성

#### C. 사진/추억

- 사진 업로드
- 날짜/태그/이벤트 자동 분류
- 대표 사진 지정
- `첫 뒤집기`, `첫 이유식` 같은 이벤트 생성

#### D. 알림

- 수유 주기 알림
- 예방접종 일정 알림
- 약 복용 알림
- 성장 기록 리마인드

#### E. 가족 공유

- 공동 계정 대신 각자 계정 + 가족 그룹 연결
- 역할 기반 권한
  - 관리자
  - 보호자
  - 조회 전용

#### F. IoT 연동

- 온습도
- 공기질
- 울음 감지
- 수면 환경 지표
- 향후 스마트 체온계/체중계 연동 확장

### 3-2. 웹(React) 핵심 기능

웹은 입력보다 보기 편한 구조가 중요합니다.

#### A. 사진첩

- 월별 앨범
- 이벤트별 앨범
- 태그 필터
- 슬라이드 보기
- 다운로드/공유

#### B. 성장 타임라인

- 사진 + 기록 + 이벤트를 한 줄로 표시
- 첫 순간 모아보기
- 월령별 요약

#### C. 리포트 열람

- 주간 수면/수유 패턴
- 성장 추이
- 빠기스 요약 코멘트

#### D. 가족 공유 페이지

- 초대 링크
- 권한 있는 가족만 열람
- 비공개 앨범/공개 앨범 분리 가능

## 4. 시스템 아키텍처

### 4-1. 전체 구조

- Flutter App
- React Web
- FastAPI Backend
- PostgreSQL
- Object Storage(S3 호환)
- Redis
- LLM Service Layer
- Worker / Scheduler
- Push Notification Service

### 4-2. 추천 구성

#### 프론트엔드

- Flutter
- React + TypeScript + Vite
- 상태관리
  - Flutter: Riverpod 또는 Bloc
  - React: TanStack Query + Zustand

#### 백엔드

- FastAPI
- SQLAlchemy
- Pydantic
- Alembic
- Celery 또는 Dramatiq + Redis
- 필요 시 WebSocket 또는 SSE 일부 적용

#### DB / 저장소

- PostgreSQL: 정형 데이터
- S3 호환 스토리지: 사진, 썸네일, 리포트 파일
- Redis: 캐시, 세션, 큐

#### AI / LLM

- FastAPI 내부 LLM 오케스트레이터
- 추후 별도 AI 서비스로 분리 가능
- RAG 필요 시 pgvector 또는 Qdrant 추가

## 5. 백엔드 모듈 설계

### 5-1. 도메인 모듈

- auth
- users
- family
- baby
- feeding
- sleep
- diaper
- health
- schedule
- album
- media
- timeline
- notifications
- iot
- llm
- reports
- admin

### 5-2. 레이어 구조

```text
api/
schemas/
services/
repositories/
models/
core/
tasks/
integrations/
```

예시:

- `services/feeding_service.py`
- `repositories/feeding_repository.py`
- `services/paggis_service.py`
- `integrations/storage/s3_client.py`
- `integrations/llm/provider.py`

## 6. DB 초안

### 6-1. 사용자/가족

- users
- family_groups
- family_members
- babies

### 6-2. 육아 기록

- feeding_logs
- sleep_logs
- diaper_logs
- health_logs
- medication_logs
- schedules

### 6-3. 사진/앨범

- media_files
- albums
- album_items
- baby_events
- timeline_items

### 6-4. LLM

- chat_sessions
- chat_messages
- ai_summaries
- ai_insights

### 6-5. IoT

- devices
- device_readings
- device_alerts

### 6-6. 운영

- notifications
- audit_logs

## 7. 주요 API 설계

### 인증

- `POST /auth/signup`
- `POST /auth/login`
- `POST /auth/refresh`

### 가족/아기

- `POST /families`
- `POST /families/{id}/invite`
- `POST /babies`
- `GET /babies/{id}`

### 기록

- `POST /feeding-logs`
- `GET /feeding-logs`
- `POST /sleep-logs`
- `POST /diaper-logs`
- `POST /health-logs`

### 사진

- `POST /media/presign`
- `POST /albums`
- `GET /albums`
- `GET /timeline`
- `POST /baby-events`

### 빠기스

- `POST /llm/chat`
- `POST /llm/parse-record`
- `GET /llm/weekly-summary/{baby_id}`
- `GET /llm/insights/{baby_id}`

### IoT

- `POST /devices/register`
- `POST /devices/{id}/readings`
- `GET /devices/{id}/status`

## 8. 빠기스 LLM 설계

빠기스는 채팅 UI 하나가 아니라 에이전트 + 파서 + 요약기로 구성합니다.

### 8-1. 역할 분리

1. **Record Parser**
   - 자연어를 구조화된 기록으로 변환
   - 예: `오전 9시 10분에 분유 80 먹었어` → feeding log 생성
2. **Insight Generator**
   - 최근 3일/7일 데이터 분석
   - 예: 평균 수면 시간, 수유 간격 변화, 체온 변화 추이
3. **Memory Companion**
   - 사진/이벤트 기반 감성 메모 생성
   - 예: `오늘 첫 뒤집기를 기록했어요`
4. **Care Assistant**
   - 월령/상황 기반 일반 육아 가이드 제공

### 8-2. 주의점

빠기스는 의료 판단 앱처럼 보이면 안 됩니다.

- 진단 금지
- 응급 권고 기준만 안내
- `정확한 판단은 전문가 상담 필요` 문구 포함
- 위험 단어 감지 시 병원 문의 권고

## 9. Flutter 앱 화면 구조

### 탭 구성 추천

- 홈
- 기록
- 빠기스
- 앨범
- 마이

### 화면 상세

- **홈**
  - 오늘 수유/수면/배변 요약
  - 체온/몸무게 최근 기록
  - 빠기스 한마디
  - IoT 상태 카드
- **기록**
  - 수유
  - 수면
  - 배변
  - 건강
  - 일정
  - 원터치 입력 + 음성 입력
- **빠기스**
  - 채팅
  - 추천 질문
  - 최근 요약
  - 기록 자동 인식
- **앨범**
  - 최근 사진
  - 이벤트별 분류
  - 업로드
- **마이**
  - 가족 초대
  - 알림 설정
  - 기기 연동
  - 계정 관리

## 10. React 웹 화면 구조

### 메뉴

- 대시보드
- 사진첩
- 타임라인
- 리포트
- 가족 공유 관리

### 특징

- 데스크탑 중심 UI
- 큰 카드/갤러리 레이아웃
- 인쇄용 레이아웃 제공
- 사진 대량 탐색 최적화

## 11. IoT 적용 포인트

처음부터 무겁게 시작하기보다 단계적으로 적용합니다.

### 1단계

- 온습도 센서
- 공기질 센서
- 알림 중심 제공

### 2단계

- 울음 감지
- 소리 강도/빈도 기록
- 수면 중 뒤척임 추정

### 3단계

- 스마트 조명/백색소음 제어
- 자동화 룰
- 울음 감지 시 알림
- 수면 시간대 조명 변경

## 12. 권한 설계

가족 공유가 있으므로 역할과 접근 범위를 명확히 합니다.

### 역할

- Owner: 가족 그룹 생성자
- Parent: 기록/수정/열람 가능
- Viewer: 사진 열람 중심
- Caregiver: 일부 기록 입력 가능

### 고려 사항

- 아기별 접근권한
- 앨범 공개 범위
- 초대 링크 만료시간
- 활동 로그 기록

## 13. MVP 범위 추천

### 앱

- 로그인
- 아기 등록
- 수유/수면/배변 기록
- 사진 업로드
- 빠기스 자연어 기록
- 가족 초대
- 홈 요약

### 웹

- 사진첩 열람
- 타임라인 열람
- 가족 공유 페이지

### 서버

- 인증
- CRUD API
- 파일 업로드
- LLM 파싱/요약
- 알림 스케줄러

> IoT는 MVP 2차로 분리하는 것이 적절합니다.

## 14. 개발 단계 제안

1. Phase 1. 코어 구축
   - 인증
   - 가족/아기
   - 육아 기록
   - 사진 저장
   - 홈 대시보드
2. Phase 2. 빠기스 탑재
   - 자연어 기록 저장
   - 요약 리포트
   - 대화형 Q&A
3. Phase 3. 웹 앨범
   - 사진첩
   - 타임라인
   - 공유 기능
4. Phase 4. IoT
   - 센서 연동
   - 환경 모니터링
   - 알림 자동화

## 15. 추천 기술 선택

### Flutter

- Flutter
- Riverpod
- GoRouter
- Dio
- Freezed
- Firebase Messaging 또는 OneSignal

### React

- React + TypeScript + Vite
- TanStack Query
- Zustand
- React Router
- Tailwind CSS

### FastAPI

- FastAPI
- SQLAlchemy 2.x
- Alembic
- PostgreSQL
- Redis
- Celery/Dramatiq
- S3 스토리지
- JWT 인증

## 16. 한 줄 제품 정의

> 육아 기록, 사진 추억, 가족 공유, AI 요약을 하나로 묶은 스마트 육아 플랫폼

앱은 입력과 관리, 웹은 열람과 공유, 빠기스는 기억하고 정리해주는 AI 역할을 담당합니다.
