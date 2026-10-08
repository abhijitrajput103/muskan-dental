/* ============================================
   MUSKAN DENTAL — PREMIUM INTERACTIONS
   ============================================ */

function initMuskanScripts() {
  // --- Sticky Header ---
  const header = document.getElementById('header');
  let lastScroll = 0;

  function handleScroll() {
    if (!header) return;
    const currentScroll = window.scrollY;
    if (currentScroll > 60) {
      header.classList.add('header--scrolled');
    } else {
      header.classList.remove('header--scrolled');
    }
    lastScroll = currentScroll;
  }

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll(); // Initial check

  // --- Mobile Menu ---
  const hamburger = document.getElementById('hamburger');
  const mobileNav = document.getElementById('mobileNav');
  const mobileLinks = document.querySelectorAll('[data-mobile-link]');

  function toggleMobileMenu() {
    if (!mobileNav || !hamburger) return;
    const isOpen = mobileNav.classList.contains('active');
    mobileNav.classList.toggle('active');
    hamburger.classList.toggle('active');
    hamburger.setAttribute('aria-expanded', !isOpen);
    document.body.style.overflow = isOpen ? '' : 'hidden';
  }

  if (hamburger) {
    hamburger.addEventListener('click', toggleMobileMenu);
  }

  mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
      if (mobileNav && mobileNav.classList.contains('active')) {
        toggleMobileMenu();
      }
    });
  });

  // --- Scroll Reveal (Intersection Observer) ---
  const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');

  if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          revealObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -40px 0px'
    });

    revealElements.forEach(el => revealObserver.observe(el));
  } else {
    // Fallback: show everything immediately
    revealElements.forEach(el => el.classList.add('revealed'));
  }

  // --- Counter Animation ---
  const counters = document.querySelectorAll('[data-counter]');

  if (counters.length > 0 && 'IntersectionObserver' in window) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.5
    });

    counters.forEach(counter => counterObserver.observe(counter));
  }

  function animateCounter(element) {
    const target = parseInt(element.dataset.counter, 10);
    const suffix = element.dataset.suffix || '';
    const duration = 2000;
    const startTime = performance.now();
    const isYear = target === 1998 || element.dataset.counter === '1998' || element.dataset.noComma === 'true';
    const isLargeNumber = target >= 1000 && !isYear;

    function easeOutCubic(t) {
      return 1 - Math.pow(1 - t, 3);
    }

    function update(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const easedProgress = easeOutCubic(progress);
      const current = Math.round(easedProgress * target);

      if (isYear) {
        element.textContent = current + suffix;
      } else if (isLargeNumber) {
        element.textContent = current.toLocaleString() + suffix;
      } else {
        element.textContent = current + suffix;
      }

      if (progress < 1) {
        requestAnimationFrame(update);
      } else if (isYear) {
        element.textContent = target + suffix;
      }
    }

    requestAnimationFrame(update);
  }

  // --- Smooth Scroll for Anchor Links ---
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;

      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();
        const headerHeight = header ? header.offsetHeight : 0;
        const targetPosition = targetElement.getBoundingClientRect().top + window.scrollY - headerHeight - 20;

        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  // --- Active Nav Link on Scroll ---
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.header__nav-link');

  function updateActiveNav() {
    const scrollPos = window.scrollY + 200;

    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      const sectionId = section.getAttribute('id');

      if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
        navLinks.forEach(link => {
          link.classList.remove('header__nav-link--active');
          if (link.getAttribute('href') === '#' + sectionId) {
            link.classList.add('header__nav-link--active');
          }
        });
      }
    });
  }

  window.addEventListener('scroll', updateActiveNav, { passive: true });

  // --- Parallax effect on hero (subtle) ---
  const heroImage = document.querySelector('.hero__bg img');
  if (heroImage) {
    window.addEventListener('scroll', () => {
      const scrolled = window.scrollY;
      if (scrolled < window.innerHeight) {
        heroImage.style.transform = `scale(1.05) translateY(${scrolled * 0.15}px)`;
      }
    }, { passive: true });
  }
}

// Global delegated FAQ accordion click handler (works even before DOMContentLoaded or if dynamic)
document.addEventListener('click', (e) => {
  const button = e.target.closest('.faq-question');
  if (!button) return;
  e.preventDefault();

  const item = button.closest('.faq-item');
  if (!item) return;

  const isOpen = item.classList.contains('active');

  // Close other open FAQs in same list/container
  const list = item.closest('.faq-list') || item.parentElement;
  if (list) {
    list.querySelectorAll('.faq-item.active').forEach(sibling => {
      if (sibling !== item) {
        sibling.classList.remove('active');
      }
    });
  }

  item.classList.toggle('active', !isOpen);
});

// Run init
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initMuskanScripts);
} else {
  initMuskanScripts();
}
