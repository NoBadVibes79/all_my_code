// Сворачивание разворачивание
const accordions = document.querySelectorAll('.accordion');

accordions.forEach((accordion) => {
  const header = accordion.querySelector('.accordion-header');
  const content = accordion.querySelector('.accordion-content');

  header.addEventListener('click', () => {
    if (content.classList.contains('active')) {
      content.classList.remove('active');
    } else {
      content.classList.add('active');
    }
  });
});