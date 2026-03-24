import type { PhotoAlbumItem } from '../types/album'

export function getPhotoAlbumItems(): PhotoAlbumItem[] {
  return [
    { title: '첫 뒤집기', date: '2026.03.14', tag: '이벤트' },
    { title: '주말 산책', date: '2026.03.16', tag: '가족' },
    { title: '첫 이유식', date: '2026.03.20', tag: '식사' },
    { title: '낮잠 후 미소', date: '2026.03.21', tag: '일상' },
  ]
}
