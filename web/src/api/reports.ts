import type { ReportRow } from '../types/reports'

export function getReportRows(): ReportRow[] {
  return [
    { title: '주간 수면', value: '평균 11시간 45분', trend: '지난주 대비 +35분' },
    { title: '주간 수유', value: '평균 6.8회', trend: '분유량 90ml 기준 안정' },
    { title: '성장 추이', value: '몸무게 7.1kg', trend: '2주 전 대비 +0.2kg' },
  ]
}
