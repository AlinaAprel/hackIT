const gameArea = document.getElementById('game-area');
const scoreDisplay = document.getElementById('score');
let score = 0;

function getRandomPosition(max) {
  return Math.floor(Math.random() * max);
}

function createCube() {
  const cube = document.createElement('div');
  cube.className = 'cube';

  // Случайная позиция
  cube.style.left = getRandomPosition(gameArea.clientWidth - 50) + 'px';
  cube.style.top = getRandomPosition(gameArea.clientHeight - 50) + 'px';

  // Случайный цвет
  cube.style.backgroundColor = `hsl(${Math.random() * 360}, 70%, 60%)`;

  cube.addEventListener('click', () => {
    score++;
    scoreDisplay.textContent = score;
    cube.remove();
  });

  gameArea.appendChild(cube);

  // Удаляем кубик через 1.2 секунды, если не успели кликнуть
  setTimeout(() => {
    if (gameArea.contains(cube)) cube.remove();
  }, 1200);
}

// Появление нового кубика каждые 1.5 секунды
setInterval(createCube, 1500);
