import type { TimelineEntry } from '../types/timeline'

export function getTimelineEntries(): TimelineEntry[] {
  return [
    { date: '2026.03.14', title: '첫 뒤집기', body: '사진 1장 · 빠기스 추억 코멘트 생성' },
    { date: '2026.03.18', title: '분유량 증가', body: '최근 7일 평균 수유량 12% 증가' },
    { date: '2026.03.20', title: '첫 이유식', body: '쌀미음 40ml 기록 · 표정 사진 저장' },
    { date: '2026.03.21', title: '수면 패턴 안정', body: '밤잠 시작 시간이 22:10 → 21:45로 개선' },
  ]
}
