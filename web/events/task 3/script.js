// Создай переменную colors с 5 любыми цветами в формате HEX

const btn = document.getElementById('colorBtn');
// #2 //

btn.addEventListener('click', function() {
  const randomColor = colors[Math.floor(Math.random() * colors.length)];

  document.body.style.backgroundColor = randomColor;
});