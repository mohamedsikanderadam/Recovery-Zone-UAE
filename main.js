/* The Recovery Zone — minimal page behaviour. No dependencies. */

// PLACEHOLDER: set FRESHA_URL to the studio's real Fresha booking page.
// Until it is set, every "Book on Fresha" control scrolls to the booking section
// instead of sending people to a dead external link.
const FRESHA_URL = '';

(function () {
  'use strict';

  const freshaLinks = document.querySelectorAll('[data-fresha]');
  freshaLinks.forEach((link) => {
    if (FRESHA_URL) {
      link.href = FRESHA_URL;
      return;
    }
    link.removeAttribute('target');
    link.removeAttribute('rel');
    link.setAttribute('title', 'Fresha booking link pending');
  });

  const drawer = document.getElementById('navdrawer');
  const backdrop = document.querySelector('.drawer-backdrop');
  const openBtn = document.querySelector('[data-menu-open]');

  function setDrawer(open) {
    drawer.classList.toggle('is-open', open);
    drawer.setAttribute('aria-hidden', String(!open));
    if (open) {
      drawer.removeAttribute('inert');
    } else {
      drawer.setAttribute('inert', '');
    }
    backdrop.hidden = !open;
    document.documentElement.classList.toggle('locked', open);
    document.body.classList.toggle('locked', open);
    openBtn.setAttribute('aria-expanded', String(open));
    if (open) {
      const first = drawer.querySelector('a');
      if (first) first.focus({ preventScroll: true });
    } else {
      openBtn.focus({ preventScroll: true });
    }
  }

  openBtn.addEventListener('click', () => setDrawer(true));
  document.querySelectorAll('[data-menu-close]').forEach((el) => {
    el.addEventListener('click', () => setDrawer(false));
  });
  drawer.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => setDrawer(false)));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('is-open')) setDrawer(false);
  });

  // The header sits over the hero image in white, and turns solid once past it.
  const header = document.querySelector('[data-header]');
  const hero = document.querySelector('.hero');
  if (header && hero) {
    const onScroll = () => {
      header.classList.toggle('is-solid', window.scrollY > hero.offsetHeight - 90);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onScroll, { passive: true });
  } else if (header) {
    header.classList.add('is-solid');
  }

  // Hovering a zone in the list previews it in the sticky image beside it.
  const svcImg = document.querySelector('[data-svc-img]');
  if (svcImg) {
    const original = svcImg.getAttribute('src');
    document.querySelectorAll('[data-svc]').forEach((link) => {
      const show = () => { svcImg.src = link.dataset.svc; };
      const restore = () => { svcImg.src = original; };
      link.addEventListener('mouseenter', show);
      link.addEventListener('focus', show);
      link.addEventListener('mouseleave', restore);
      link.addEventListener('blur', restore);
    });
  }

  const year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());
})();
