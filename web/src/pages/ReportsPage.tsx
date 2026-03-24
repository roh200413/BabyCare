import { getReportRows } from '../api/reports'
import { SectionHeader } from '../components/ui/SectionHeader'

const reportRows = getReportRows()

export function ReportsPage() {
  return (
    <section className="content-section">
      <SectionHeader
        eyebrow="Reports"
        title="리포트"
        action={<button className="primary-button">PDF 저장</button>}
      />
      <div className="report-table">
        {reportRows.map((row) => (
          <div key={row.title} className="report-row">
            <strong>{row.title}</strong>
            <span>{row.value}</span>
            <span>{row.trend}</span>
          </div>
        ))}
      </div>
    </section>
  )
}
