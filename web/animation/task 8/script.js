const player = document.querySelector('.player');
const obstaclesContainer = document.querySelector('.obstacles');
const scoreElement = document.querySelector('.score span');

let score = 0;
let playerX = 50;
let gameSpeed = 2;
let isGameOver = false;

// Управление игроком (← → стрелки)
document.addEventListener('keydown', (e) => {
  if (isGameOver) return;

  if (e.key === 'ArrowLeft' && playerX > 10) {
    playerX -= 10;
  } else if (e.key === 'ArrowRight' && playerX < 90) {
    playerX += 10;
  }

  player.style.left = `${playerX}%`;
});

// Создание препятствий
function createObstacle() {
  if (isGameOver) return;

  const obstacle = document.createElement('div');
  obstacle.classList.add('obstacle');
  
  const randomX = Math.random() * 80 + 10; // 10-90%
  obstacle.style.left = `${randomX}%`;
  obstacle.style.animationDuration = `${Math.random() * 2 + 1}s`; // Разная скорость

  // 3D-эффект
  obstacle.style.transform = `translate3d(0, 0, ${Math.random() * 100 - 50}px) rotateX(${Math.random() * 360}deg) rotateY(${Math.random() * 360}deg)`;

  obstaclesContainer.appendChild(obstacle);

  // Удаление препятствий после падения
  setTimeout(() => {
    obstacle.remove();
  }, 3000);

  // Проверка столкновений
  const checkCollision = setInterval(() => {
    const playerRect = player.getBoundingClientRect();
    const obstacleRect = obstacle.getBoundingClientRect();

    if (
      playerRect.left < obstacleRect.right &&
      playerRect.right > obstacleRect.left &&
      playerRect.top < obstacleRect.bottom &&
      playerRect.bottom > obstacleRect.top
    ) {
      gameOver();
      clearInterval(checkCollision);
    }
  }, 10);

  // Увеличение счёта
  score++;
  scoreElement.textContent = score;

  // Ускорение игры
  if (score % 10 === 0) {
    gameSpeed += 0.2;
    document.querySelectorAll('.obstacle').forEach(obs => {
      obs.style.animationDuration = `${parseFloat(obs.style.animationDuration) * 0.9}s`;
    });
  }
}

// Конец игры
function gameOver() {
  isGameOver = true;
  alert(`Game Over! Score: ${score}`);
  document.querySelectorAll('.obstacle').forEach(obs => obs.remove());
  score = 0;
  scoreElement.textContent = '0';
  playerX = 50;
  player.style.left = '50%';
  isGameOver = false;
}

// Запуск игры
setInterval(createObstacle, 1000);