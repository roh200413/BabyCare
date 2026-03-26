import { useState } from 'react'

import { getFamilyMembers } from '../api/family'
import { SectionHeader } from '../components/ui/SectionHeader'

const invitees = getFamilyMembers()

function makeInviteLink() {
  const token = Math.random().toString(36).slice(2, 8).toUpperCase()
  return `https://babycare.app/invite/${token}`
}

export function FamilySharePage() {
  const [inviteLink, setInviteLink] = useState('')

  const createInviteLink = async () => {
    const nextLink = makeInviteLink()
    setInviteLink(nextLink)

    if (navigator.clipboard?.writeText) {
      await navigator.clipboard.writeText(nextLink)
    }
  }

  return (
    <section className="content-section" id="family-share">
      <SectionHeader
        eyebrow="Family Share"
        title="가족 공유 관리"
        action={
          <button className="primary-button" onClick={createInviteLink}>
            초대 링크 생성
          </button>
        }
      />
      {inviteLink ? <p className="section-meta">생성된 링크(클립보드 복사): {inviteLink}</p> : null}
      <div className="two-column-grid">
        <article className="panel-card">
          <h3>공유 권한</h3>
          <ul className="share-list">
            {invitees.map((member) => (
              <li key={member.name}>
                <strong>
                  {member.name} · {member.role}
                </strong>
                <p>{member.detail}</p>
              </li>
            ))}
          </ul>
        </article>
        <article className="panel-card accent-card">
          <h3>공유 정책</h3>
          <ul className="policy-list">
            <li>초대 링크 72시간 만료</li>
            <li>비공개 앨범은 Viewer 접근 제한</li>
            <li>다운로드/공유 기록은 활동 로그에 저장</li>
          </ul>
        </article>
      </div>
    </section>
  )
}
