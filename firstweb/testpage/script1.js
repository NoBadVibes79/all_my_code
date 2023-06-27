// Add smooth scrolling to nav links
const navLinks = document.querySelectorAll('nav a');

for (const link of navLinks) {
  link.addEventListener('click', smoothScroll);
}

function smoothScroll(event) {
  event.preventDefault();
  const targetId = this.getAttribute('href');
  const targetPosition = document.querySelector(targetId).offsetTop;
  const startPosition = window.pageYOffset;
  const distance = targetPosition - startPosition;
  const duration = 500;
  let start = null;

  function step(timestamp) {
    if (!start) start = timestamp;
    const progress = timestamp - start;
    window.scrollTo(0, easeInOut(progress, startPosition, distance, duration));
    if (progress < duration) window.requestAnimationFrame(step);
  }

  window.requestAnimationFrame(step);
}

function easeInOut(t, b, c, d) {
  t /= d / 2;
  if (t < 1) return c / 2 * t * t + b;
  t--;
  return -c / 2 * (t * (t - 2) - 1) + b;
}
