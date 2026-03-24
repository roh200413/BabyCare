import type { SummaryCardItem } from '../../types/dashboard'

export function SummaryCard({ title, value, description }: SummaryCardItem) {
  return (
    <article className="summary-card">
      <p className="summary-title">{title}</p>
      <strong className="summary-value">{value}</strong>
      <p className="summary-description">{description}</p>
    </article>
  )
}
