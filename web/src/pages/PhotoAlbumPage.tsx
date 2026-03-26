import { useMemo, useState } from 'react'

import { getPhotoAlbumItems } from '../api/album'
import { SectionHeader } from '../components/ui/SectionHeader'

const photos = getPhotoAlbumItems()

export function PhotoAlbumPage() {
  const [filter, setFilter] = useState<'all' | 'event'>('all')

  const visiblePhotos = useMemo(() => {
    if (filter === 'all') {
      return photos
    }
    return photos.filter((photo) => photo.tag === '이벤트')
  }, [filter])

  const toggleFilter = () => {
    setFilter((prev) => (prev === 'all' ? 'event' : 'all'))
  }

  return (
    <section className="content-section" id="album">
      <SectionHeader
        eyebrow="Album"
        title="사진첩"
        action={
          <button className="ghost-button" onClick={toggleFilter}>
            {filter === 'all' ? '이벤트만 보기' : '전체 보기'}
          </button>
        }
      />
      <p className="section-meta">현재 {visiblePhotos.length}개의 사진이 표시됩니다.</p>
      <div className="photo-grid">
        {visiblePhotos.map((photo) => (
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
