import { getDashboardCards } from '../api/dashboard'
import { TopNav } from '../components/layout/TopNav'
import { SummaryCard } from '../components/ui/SummaryCard'
import { DashboardPage } from '../pages/DashboardPage'
import { FamilySharePage } from '../pages/FamilySharePage'
import { PhotoAlbumPage } from '../pages/PhotoAlbumPage'
import { ReportsPage } from '../pages/ReportsPage'
import { TimelinePage } from '../pages/TimelinePage'

const dashboardCards = getDashboardCards()

export default function App() {
  return (
    <div className="app-shell">
      <TopNav />
      <main className="page-content">
        <section className="hero-panel">
          <div>
            <p className="eyebrow">BabyCare Web</p>
            <h1>열람과 공유에 최적화된 가족형 육아 대시보드</h1>
            <p className="hero-copy">
              사진첩, 성장 타임라인, 주간 리포트, 가족 공유를 큰 화면에서 편하게 확인할 수 있는
              웹 경험을 먼저 구성했습니다.
            </p>
          </div>
          <div className="hero-grid">
            {dashboardCards.map((card) => (
              <SummaryCard key={card.title} {...card} />
            ))}
          </div>
        </section>
        <DashboardPage />
        <PhotoAlbumPage />
        <TimelinePage />
        <ReportsPage />
        <FamilySharePage />
      </main>
    </div>
  )
}
