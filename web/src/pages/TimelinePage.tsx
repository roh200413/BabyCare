import { getTimelineEntries } from '../api/timeline'
import { SectionHeader } from '../components/ui/SectionHeader'

const timeline = getTimelineEntries()

export function TimelinePage() {
  return (
    <section className="content-section" id="timeline">
      <SectionHeader eyebrow="Timeline" title="성장 타임라인" />
      <div className="timeline-list">
        {timeline.map((entry) => (
          <article key={entry.title} className="timeline-item">
            <span className="timeline-date">{entry.date}</span>
            <div>
              <h3>{entry.title}</h3>
              <p>{entry.body}</p>
            </div>
          </article>
        ))}
      </div>
    </section>
  )
}
