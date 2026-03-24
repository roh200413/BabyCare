import type { FamilyMember } from '../types/family'

export function getFamilyMembers(): FamilyMember[] {
  return [
    { name: '엄마', role: 'Owner', detail: '모든 기록/앨범 관리' },
    { name: '아빠', role: 'Parent', detail: '기록 수정 및 리포트 열람' },
    { name: '할머니', role: 'Viewer', detail: '공유 앨범과 타임라인 열람' },
  ]
}
