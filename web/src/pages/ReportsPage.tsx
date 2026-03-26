import { getReportRows } from '../api/reports'
import { SectionHeader } from '../components/ui/SectionHeader'

const reportRows = getReportRows()

function downloadWeeklyReport() {
  const content = reportRows
    .map((row) => `${row.title}: ${row.value} (${row.trend})`)
    .join('\n')

  const blob = new Blob([`BabyCare Weekly Report\n\n${content}`], { type: 'text/plain;charset=utf-8' })
  const url = URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.href = url
  link.download = 'babycare-weekly-report.txt'
  link.click()
  URL.revokeObjectURL(url)
}

export function ReportsPage() {
  return (
    <section className="content-section" id="reports">
      <SectionHeader
        eyebrow="Reports"
        title="리포트"
        action={
          <button className="primary-button" onClick={downloadWeeklyReport}>
            리포트 다운로드
          </button>
        }
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
