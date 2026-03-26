import type { DashboardWidget, SummaryCardItem } from '../types/dashboard'

export function getDashboardCards(): SummaryCardItem[] {
  return [
    { title: '오늘 수유', value: '7회', description: '평균 간격 2시간 45분' },
    { title: '오늘 수면', value: '11시간 20분', description: '낮잠 3회 포함' },
    { title: '배변 기록', value: '4회', description: '최근 기록 14:10' },
    { title: '아기방 상태', value: '24.1°C / 46%', description: '공기질 좋음 · 소리 안정' },
  ]
}

export function getDashboardWidgets(): DashboardWidget[] {
  return [
    {
      title: '빠기스 주간 코멘트',
      body: '이번 주는 수면 흐름이 지난주보다 안정적이에요. 밤잠 진입 시간이 25분 빨라졌어요.',
    },
    {
      title: '예방접종 일정',
      body: '4월 2일 DTaP-IPV-Hib 예약 · 병원 방문 전 예진표 확인 필요',
    },
    {
      title: 'IoT 알림',
      body: '아기방 카메라 온라인 · 울음 감지 없음 · 움직임 감지 2회',
    },
  ]
}
