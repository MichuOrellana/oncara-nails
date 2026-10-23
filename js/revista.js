/**
 * ONCARA MAG — Revista digital
 * Two-page spreads on desktop, one page at a time on phones.
 */

document.addEventListener('DOMContentLoaded', initRevista);

function initRevista() {
  const book = document.querySelector('.mag-book');
  if (!book) return;

  const spreads = [...book.querySelectorAll('.mag-spread')];
  const prevBtn = document.querySelector('.mag-prev');
  const nextBtn = document.querySelector('.mag-next');
  const label = document.querySelector('.mag-progress-label');
  const bar = document.querySelector('.mag-progress-bar');
  const singlePage = window.matchMedia('(max-width: 820px)');

  // Page numbers: the cover is page 1, folios are printed from page 2 on
  let pageNum = 0;
  spreads.forEach(spread => {
    spread.querySelectorAll('.mag-page').forEach(page => {
      pageNum++;
      page.dataset.folio = pageNum;
      const folio = page.querySelector('.folio-num');
      if (folio) folio.textContent = String(pageNum).padStart(2, '0');
    });
  });

  document.querySelectorAll('.toc-num').forEach(num => {
    const target = document.getElementById(num.dataset.for);
    const first = target && target.querySelector('.mag-page');
    if (first) num.textContent = String(first.dataset.folio).padStart(2, '0');
  });

  // A "view" is what is on screen: a whole spread, or a single page on phones
  let views = [];
  let current = -1;

  function buildViews() {
    views = singlePage.matches
      ? spreads.flatMap((spread, si) => [...spread.querySelectorAll('.mag-page')].map(page => ({ si, page })))
      : spreads.map((spread, si) => ({ si, page: null }));
  }

  function show(index, direction) {
    index = Math.max(0, Math.min(views.length - 1, index));
    const view = views[index];
    const spread = spreads[view.si];

    spreads.forEach((s, si) => {
      const active = si === view.si;
      s.classList.toggle('is-active', active);
      s.inert = !active;
    });

    const pages = [...spread.querySelectorAll('.mag-page')];
    pages.forEach(p => p.classList.toggle('is-current', !view.page || p === view.page));

    const animated = view.page || spread;
    animated.classList.remove('mag-turn-next', 'mag-turn-prev');
    if (direction) {
      void animated.offsetWidth;
      animated.classList.add(direction > 0 ? 'mag-turn-next' : 'mag-turn-prev');
    }

    current = index;

    const shown = view.page ? [view.page] : pages;
    const folios = shown.map(p => p.dataset.folio);
    const pagesText = folios.length > 1 ? `PÁGS. ${folios[0]}–${folios[1]}` : `PÁG. ${folios[0]}`;
    label.textContent = `${pagesText} · ${spread.dataset.title.toUpperCase()}`;
    bar.style.width = `${(index / (views.length - 1)) * 100}%`;

    prevBtn.disabled = index === 0;
    nextBtn.disabled = index === views.length - 1;

    const hash = view.si === 0 ? '' : `#${spread.id}`;
    if (location.hash !== hash) {
      history.replaceState(null, '', hash || location.pathname + location.search);
    }
  }

  function go(step) {
    const target = current + step;
    if (target < 0 || target >= views.length) return;
    show(target, step);
  }

  function goToSpread(id) {
    const index = views.findIndex(v => spreads[v.si].id === id);
    if (index === -1) return false;
    show(index, index === current ? 0 : Math.sign(index - current));
    return true;
  }

  prevBtn.addEventListener('click', () => go(-1));
  nextBtn.addEventListener('click', () => go(1));

  // In-magazine links (índice, contratapa, top bar) turn pages instead of scrolling
  document.addEventListener('click', (e) => {
    const link = e.target.closest('a[href^="#"]');
    if (!link) return;
    const id = link.getAttribute('href').slice(1);
    if (id === 'revista') return; // skip link
    if (goToSpread(id)) e.preventDefault();
  });

  window.addEventListener('hashchange', () => goToSpread(location.hash.slice(1)));

  document.addEventListener('keydown', (e) => {
    if (e.target.closest('input, textarea, select') || document.querySelector('.cart-drawer.open')) return;
    if (e.key === 'ArrowRight' || e.key === 'PageDown') { e.preventDefault(); go(1); }
    if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); go(-1); }
    if (e.key === 'Home') { e.preventDefault(); show(0, -1); }
    if (e.key === 'End') { e.preventDefault(); show(views.length - 1, 1); }
  });

  // Swipe to turn pages
  let touchX = null;
  let touchY = null;
  book.addEventListener('touchstart', (e) => {
    touchX = e.touches[0].clientX;
    touchY = e.touches[0].clientY;
  }, { passive: true });
  book.addEventListener('touchend', (e) => {
    if (touchX === null) return;
    const dx = e.changedTouches[0].clientX - touchX;
    const dy = e.changedTouches[0].clientY - touchY;
    touchX = null;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.5) go(dx < 0 ? 1 : -1);
  }, { passive: true });

  // Switching between one and two pages keeps the reader on the same spread
  singlePage.addEventListener('change', () => {
    const si = current >= 0 ? views[current].si : 0;
    buildViews();
    show(views.findIndex(v => v.si === si), 0);
  });

  buildViews();
  if (!goToSpread(location.hash.slice(1))) show(0, 0);
}
