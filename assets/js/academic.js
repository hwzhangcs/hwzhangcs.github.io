(() => {
  const root = document.documentElement;
  const toggle = document.querySelector('.theme-toggle');
  const media = window.matchMedia('(prefers-color-scheme: dark)');
  let preference;
  try { preference = localStorage.getItem('theme'); } catch (_) { /* Storage may be disabled. */ }
  const applyTheme = () => {
    const dark = preference === 'dark' || (preference !== 'light' && media.matches);
    if (dark) root.dataset.theme = 'dark'; else root.removeAttribute('data-theme');
    toggle.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
    toggle.title = toggle.getAttribute('aria-label');
    toggle.querySelector('i').className = dark ? 'fas fa-sun' : 'fas fa-moon';
  };
  applyTheme();
  toggle.addEventListener('click', () => {
    preference = root.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('theme', preference); } catch (_) { /* Keep session choice. */ }
    applyTheme();
  });
  media.addEventListener('change', applyTheme);

  // Mark the homepage section currently in view in the main navigation.
  const sectionLinks = Array.from(document.querySelectorAll('.nav-links a[href*="#"]'))
    .map(link => ({ link, section: location.pathname === new URL(link.href).pathname && document.getElementById(new URL(link.href).hash.slice(1)) }))
    .filter(item => item.section);
  if (sectionLinks.length && 'IntersectionObserver' in window) {
    const visible = new Set();
    const update = () => {
      const current = sectionLinks.find(item => visible.has(item.section));
      sectionLinks.forEach(item => {
        if (item === current) item.link.setAttribute('aria-current', 'location'); else item.link.removeAttribute('aria-current');
      });
    };
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => { if (entry.isIntersecting) visible.add(entry.target); else visible.delete(entry.target); });
      update();
    }, { rootMargin: '-35% 0px -55% 0px' });
    sectionLinks.forEach(item => observer.observe(item.section));
  }

  const details = Array.from(document.querySelectorAll('.cv-content details'));
  let printState;
  window.addEventListener('beforeprint', () => {
    if (printState) return;
    printState = details.map(detail => detail.open);
    details.forEach(detail => { detail.open = true; });
  });
  window.addEventListener('afterprint', () => {
    if (!printState) return;
    details.forEach((detail, index) => { detail.open = printState[index]; });
    printState = undefined;
  });
  document.querySelector('[data-print]')?.addEventListener('click', () => window.print());
})();
