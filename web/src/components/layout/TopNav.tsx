const navItems = [
  { label: '대시보드', target: 'dashboard' },
  { label: '사진첩', target: 'album' },
  { label: '타임라인', target: 'timeline' },
  { label: '리포트', target: 'reports' },
  { label: '가족 공유', target: 'family-share' },
]

export function TopNav() {
  const moveToSection = (target: string) => {
    const element = document.getElementById(target)
    if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }
  }

  return (
    <header className="top-nav">
      <div>
        <p className="brand">BabyCare</p>
        <p className="sub-brand">View & Share Portal</p>
      </div>
      <nav>
        <ul className="nav-list">
          {navItems.map((item) => (
            <li key={item.label}>
              <button className="nav-button" onClick={() => moveToSection(item.target)}>
                {item.label}
              </button>
            </li>
          ))}
        </ul>
      </nav>
    </header>
  )
}
