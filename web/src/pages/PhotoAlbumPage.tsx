import { getPhotoAlbumItems } from '../api/album'
import { SectionHeader } from '../components/ui/SectionHeader'

const photos = getPhotoAlbumItems()

export function PhotoAlbumPage() {
  return (
    <section className="content-section">
      <SectionHeader
        eyebrow="Album"
        title="사진첩"
        action={<button className="ghost-button">월별 앨범 보기</button>}
      />
      <div className="photo-grid">
        {photos.map((photo) => (
          <article key={photo.title} className="photo-card">
            <div className="photo-placeholder" />
            <div className="photo-meta">
              <strong>{photo.title}</strong>
              <span>{photo.date}</span>
              <span className="tag">{photo.tag}</span>
            </div>
          </article>
        ))}
      </div>
    </section>
  )
}
