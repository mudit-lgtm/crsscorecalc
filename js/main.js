/**
 * CRS Score Calculator - Main UI JavaScript
 * Navigation, interactions, FAQ accordion
 * Site: crsscorecalculator.vercel.app
 */

'use strict';

// =========================================================
// NAVIGATION
// =========================================================

function initNavigation() {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.main-nav');
  const navLinks = document.querySelectorAll('.nav-link');

  if (!toggle || !nav) return;

  // Mobile menu toggle
  toggle.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('open');
    toggle.classList.toggle('active', isOpen);
    toggle.setAttribute('aria-expanded', isOpen);
    document.body.style.overflow = isOpen ? 'hidden' : '';
  });

  // Mobile dropdown toggles
  navLinks.forEach(link => {
    if (link.nextElementSibling?.classList.contains('dropdown')) {
      link.addEventListener('click', (e) => {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          const navItem = link.closest('.nav-item');
          const isOpen = navItem.classList.toggle('mobile-open');
          link.querySelector('.arrow').style.transform = isOpen ? 'rotate(180deg)' : '';
        }
      });
    }
  });

  // Close nav on outside click
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.site-header')) {
      nav.classList.remove('open');
      toggle.classList.remove('active');
      document.body.style.overflow = '';
    }
  });

  // Close nav on resize
  window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
      nav.classList.remove('open');
      toggle.classList.remove('active');
      document.body.style.overflow = '';
    }
  });

  // Highlight current page in nav
  const currentPath = window.location.pathname.replace(/\/$/, '') || '/';
  document.querySelectorAll('.main-nav a, .dropdown a').forEach(a => {
    const href = a.getAttribute('href');
    if (href) {
      const normalizedHref = href.replace(/\/$/, '');
      if (normalizedHref === currentPath || (currentPath === '' && normalizedHref === '/index.html')) {
        a.style.color = 'var(--primary)';
        a.style.fontWeight = '700';
      }
    }
  });
}

// =========================================================
// FAQ ACCORDION
// =========================================================

function initFAQ() {
  document.querySelectorAll('.faq-question').forEach(question => {
    question.addEventListener('click', () => {
      const item = question.closest('.faq-item');
      if (!item) return;

      const isOpen = item.classList.contains('open');

      // Close all FAQ items in same list
      const list = question.closest('.faq-list');
      if (list) {
        list.querySelectorAll('.faq-item.open').forEach(openItem => {
          openItem.classList.remove('open');
        });
      }

      if (!isOpen) {
        item.classList.add('open');
      }
    });
  });
}

// =========================================================
// SCROLL EFFECTS
// =========================================================

function initScrollEffects() {
  // Sticky header shadow
  const header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', () => {
      header.style.boxShadow = window.scrollY > 10
        ? '0 4px 20px rgba(0,0,0,0.15)'
        : '0 2px 10px rgba(0,0,0,0.1)';
    }, { passive: true });
  }

  // Back to top (create button if doesn't exist)
  if (!document.querySelector('.back-to-top')) {
    const btn = document.createElement('button');
    btn.className = 'back-to-top';
    btn.innerHTML = '↑';
    btn.setAttribute('aria-label', 'Back to top');
    btn.style.cssText = `
      position: fixed; bottom: 24px; right: 24px;
      width: 44px; height: 44px; border-radius: 50%;
      background: var(--primary); color: white;
      border: none; cursor: pointer; font-size: 1.1rem;
      box-shadow: 0 4px 12px rgba(204,0,0,0.4);
      display: none; z-index: 500; transition: all 0.3s;
      font-weight: bold;
    `;
    document.body.appendChild(btn);

    btn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    window.addEventListener('scroll', () => {
      btn.style.display = window.scrollY > 300 ? 'block' : 'none';
    }, { passive: true });
  }
}

// =========================================================
// SMOOTH ANCHOR SCROLLING
// =========================================================

function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const navHeight = document.querySelector('.site-header')?.offsetHeight || 70;
        const y = target.getBoundingClientRect().top + window.pageYOffset - navHeight - 16;
        window.scrollTo({ top: y, behavior: 'smooth' });
      }
    });
  });
}

// =========================================================
// EXTERNAL LINKS
// =========================================================

function initExternalLinks() {
  document.querySelectorAll('a[href^="http"]').forEach(link => {
    const href = link.getAttribute('href');
    if (!href.includes('crsscorecalculator.vercel.app')) {
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener noreferrer');
      if (!link.querySelector('.sr-only')) {
        link.insertAdjacentHTML('beforeend', '<span class="sr-only"> (opens in new tab)</span>');
      }
    }
  });
}

// =========================================================
// LAZY LOAD IMAGES
// =========================================================

function initLazyLoad() {
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          if (img.dataset.src) {
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
          }
          observer.unobserve(img);
        }
      });
    });
    document.querySelectorAll('img[data-src]').forEach(img => observer.observe(img));
  }
}

// =========================================================
// DRAWS TABLE — update dynamically (static data)
// =========================================================

const RECENT_DRAWS = [
  { num: 318, date: 'Apr 9, 2025', type: 'No Program Specified', minCRS: 489, itas: 1000 },
  { num: 317, date: 'Mar 26, 2025', type: 'French Language Proficiency', minCRS: 379, itas: 800 },
  { num: 316, date: 'Mar 12, 2025', type: 'No Program Specified', minCRS: 491, itas: 1000 },
  { num: 315, date: 'Feb 26, 2025', type: 'Provincial Nominee Program', minCRS: 791, itas: 598 },
  { num: 314, date: 'Feb 12, 2025', type: 'No Program Specified', minCRS: 493, itas: 1000 },
  { num: 313, date: 'Jan 29, 2025', type: 'French Language Proficiency', minCRS: 377, itas: 700 },
  { num: 312, date: 'Jan 15, 2025', type: 'No Program Specified', minCRS: 496, itas: 1100 },
  { num: 311, date: 'Jan 8, 2025', type: 'No Program Specified', minCRS: 498, itas: 1500 },
  { num: 310, date: 'Dec 18, 2024', type: 'No Program Specified', minCRS: 494, itas: 1200 },
  { num: 309, date: 'Dec 4, 2024', type: 'French Language Proficiency', minCRS: 375, itas: 600 }
];

function renderDrawsTable() {
  const tbody = document.getElementById('draws-tbody');
  if (!tbody) return;

  tbody.innerHTML = RECENT_DRAWS.map(draw => {
    let typeBadge = 'badge-new';
    if (draw.type.includes('Provincial')) typeBadge = 'badge-pnp';
    if (draw.type.includes('French')) typeBadge = 'badge-good';

    return `
      <tr>
        <td>#${draw.num}</td>
        <td>${draw.date}</td>
        <td><span class="badge ${typeBadge}">${draw.type}</span></td>
        <td><strong>${draw.minCRS}</strong></td>
        <td>${draw.itas.toLocaleString()}</td>
      </tr>
    `;
  }).join('');
}

// =========================================================
// INIT ALL
// =========================================================

function init() {
  initNavigation();
  initFAQ();
  initScrollEffects();
  initSmoothScroll();
  initExternalLinks();
  initLazyLoad();
  renderDrawsTable();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
