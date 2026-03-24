const navItems = ['대시보드', '사진첩', '타임라인', '리포트', '가족 공유']

export function TopNav() {
  return (
    <header className="top-nav">
      <div>
        <p className="brand">BabyCare</p>
        <p className="sub-brand">View & Share Portal</p>
      </div>
      <nav>
        <ul className="nav-list">
          {navItems.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </nav>
    </header>
  )
}
