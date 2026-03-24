import { getDashboardWidgets } from '../api/dashboard'
import { SectionHeader } from '../components/ui/SectionHeader'

const widgets = getDashboardWidgets()

export function DashboardPage() {
  return (
    <section className="content-section">
      <SectionHeader eyebrow="Dashboard" title="오늘 현황" />
      <div className="two-column-grid">
        {widgets.map((widget) => (
          <article key={widget.title} className="panel-card">
            <h3>{widget.title}</h3>
            <p>{widget.body}</p>
          </article>
        ))}
      </div>
    </section>
  )
}
