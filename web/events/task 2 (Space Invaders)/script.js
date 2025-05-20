// Получаем элементы DOM
const gameArea = document.getElementById('game-area');
const spaceship = document.getElementById('spaceship');
const scoreElement = document.getElementById('score');
const livesElement = document.getElementById('lives');

// Игровые переменные
let spaceshipX = 275;
let score = 0;
let lives = 3;
let gameInterval;
let meteorInterval;
let bullets = [];
let meteors = [];
let isGameRunning = false;

// Начальные настройки игры
function initGame() {
    spaceshipX = 275;
    score = 0;
    lives = 3;
    bullets = [];
    meteors = [];
    
    // Очищаем игровую область
    gameArea.innerHTML = '';
    gameArea.appendChild(spaceship);
    
    // Обновляем UI
    updateScore();
    updateLives();
    
    // Устанавливаем начальную позицию корабля
    spaceship.style.left = spaceshipX + 'px';
    
    // Запускаем игровые интервалы
    if (!isGameRunning) {
        isGameRunning = true;
        gameInterval = setInterval(updateGame, 20);
        meteorInterval = setInterval(createMeteor, 1000);
    }
}

// Обновление игрового состояния
function updateGame() {
    moveBullets();
    moveMeteors();
    checkCollisions();
}

// Создание метеорита
function createMeteor() {
    if (!isGameRunning) return;
    
    const meteor = document.createElement('div');
    meteor.className = 'meteor';
    const meteorX = Math.random() * 570; // 600 - 30 (ширина метеорита)
    meteor.style.left = meteorX + 'px';
    gameArea.appendChild(meteor);
    
    meteors.push({
        element: meteor,
        x: meteorX,
        y: 0,
        speed: 1 + Math.random() * 2
    });
}

// Движение пуль
function moveBullets() {
    for (let i = bullets.length - 1; i >= 0; i--) {
        const bullet = bullets[i];
        bullet.y -= 5;
        bullet.element.style.bottom = bullet.y + 'px';
        
        // Удаляем пули, которые вышли за пределы экрана
        if (bullet.y < 0) {
            gameArea.removeChild(bullet.element);
            bullets.splice(i, 1);
        }
    }
}

// Движение метеоритов
function moveMeteors() {
    for (let i = meteors.length - 1; i >= 0; i--) {
        const meteor = meteors[i];
        meteor.y += meteor.speed;
        meteor.element.style.top = meteor.y + 'px';
        
        // Удаляем метеориты, которые вышли за пределы экрана
        if (meteor.y > 400) {
            gameArea.removeChild(meteor.element);
            meteors.splice(i, 1);
        }
    }
}

// Проверка столкновений
function checkCollisions() {
    // Проверка попадания пули в метеорит
    for (let i = bullets.length - 1; i >= 0; i--) {
        const bullet = bullets[i];
        
        for (let j = meteors.length - 1; j >= 0; j--) {
            const meteor = meteors[j];
            
            if (
                bullet.x < meteor.x + 30 &&
                bullet.x + 4 > meteor.x &&
                bullet.y < meteor.y + 30 &&
                bullet.y + 15 > meteor.y
            ) {
                // Попадание!
                gameArea.removeChild(bullet.element);
                gameArea.removeChild(meteor.element);
                bullets.splice(i, 1);
                meteors.splice(j, 1);
                
                score += 10;
                updateScore();
                break;
            }
        }
    }
    
    // Проверка столкновения корабля с метеоритом
    for (let i = meteors.length - 1; i >= 0; i--) {
        const meteor = meteors[i];
        
        if (
            spaceshipX < meteor.x + 30 &&
            spaceshipX + 50 > meteor.x &&
            370 < meteor.y + 30 &&
            400 > meteor.y
        ) {
            // Столкновение!
            gameArea.removeChild(meteor.element);
            meteors.splice(i, 1);
            
            lives--;
            updateLives();
            
            if (lives <= 0) {
                gameOver();
            }
            break;
        }
    }
}

// Стрельба
function fireBullet() {
    if (!isGameRunning) return;
    
    const bullet = document.createElement('div');
    bullet.className = 'bullet';
    const bulletX = spaceshipX + 23; // Центр корабля
    bullet.style.left = bulletX + 'px';
    bullet.style.bottom = '50px';
    gameArea.appendChild(bullet);
    
    bullets.push({
        element: bullet,
        x: bulletX,
        y: 350 // Начальная позиция пули
    });
}

// Обновление счета
function updateScore() {
    scoreElement.textContent = score;
}

// Обновление жизней
function updateLives() {
    livesElement.textContent = lives;
}

// Конец игры
function gameOver() {
    isGameRunning = false;
    clearInterval(gameInterval);
    clearInterval(meteorInterval);
    
    alert(`Игра окончена! Ваш счет: ${score}`);
    initGame(); // Перезапуск игры
}

// Обработка нажатий клавиш
document.addEventListener('keydown', function(event) {
    if (!isGameRunning) return;
    
    switch(event.key) {
        case 'ArrowLeft':
            if (spaceshipX > 0) {
                spaceshipX -= 10;
                spaceship.style.left = spaceshipX + 'px';
            }
            break;
        case 'ArrowRight':
            if (spaceshipX < 550) { // 600 - 50 (ширина корабля)
                spaceshipX += 10;
                spaceship.style.left = spaceshipX + 'px';
            }
            break;
        case ' ':
            fireBullet();
            break;
    }
});

// Запуск игры при загрузке страницы
window.onload = initGame;