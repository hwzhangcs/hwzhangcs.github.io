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

  const menu = document.querySelector('.menu-toggle');
  const links = document.querySelector('.nav-links');
  const closeMenu = () => {
    menu.setAttribute('aria-expanded', 'false');
    links.classList.remove('is-open');
  };
  menu.addEventListener('click', () => {
    const open = menu.getAttribute('aria-expanded') !== 'true';
    menu.setAttribute('aria-expanded', String(open));
    links.classList.toggle('is-open', open);
  });
  links.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') {
      closeMenu(); menu.focus();
    }
  });
  window.matchMedia('(min-width: 1024px)').addEventListener('change', closeMenu);
  const research = document.querySelector('[data-section]');
  const updateSection = () => {
    const target = new URL(research.href);
    if (location.pathname === target.pathname && location.hash === target.hash) research.setAttribute('aria-current', 'location');
    else research.removeAttribute('aria-current');
  };
  if (research) { updateSection(); window.addEventListener('hashchange', updateSection); }

  const details = Array.from(document.querySelectorAll('.cv-content details'));
  let printState;
  const beforePrint = () => {
    if (printState) return;
    printState = details.map(detail => detail.open);
    details.forEach(detail => { detail.open = true; });
  };
  const afterPrint = () => {
    if (!printState) return;
    details.forEach((detail, index) => { detail.open = printState[index]; });
    printState = undefined;
  };
  window.addEventListener('beforeprint', beforePrint);
  window.addEventListener('afterprint', afterPrint);
  document.querySelector('[data-print]')?.addEventListener('click', () => window.print());
})();
