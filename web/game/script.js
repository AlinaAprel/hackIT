// script.js

// Инициализация переменных
let score = 0;
let timeLeft = 30;
let gameInterval;

// Получаем элементы DOM
const cat = document.getElementById('cat');
const scoreDisplay = document.getElementById('score');
const timeDisplay = document.getElementById('time');
const meowSound = document.getElementById('meowSound');
const gameOverSound = document.getElementById('gameOverSound');

// Функция для случайного перемещения кота
function moveCat() {
    const containerWidth = window.innerWidth - 100; // Ширина контейнера минус размер кота
    const containerHeight = window.innerHeight - 100; // Высота контейнера минус размер кота

    const randomX = Math.floor(Math.random() * containerWidth);
    const randomY = Math.floor(Math.random() * containerHeight);

    // Добавляем анимацию перемещения
    cat.style.transition = 'transform 0.5s ease-in-out';
    cat.style.left = `${randomX}px`;
    cat.style.top = `${randomY}px`;

    setTimeout(() => {
        cat.style.transition = 'none'; // Убираем анимацию после завершения
    }, 500);
}

// Функция для обработки клика по коту
cat.addEventListener('click', () => {
    score++;
    scoreDisplay.textContent = score;
    meowSound.currentTime = 0; // Перезапуск звука
    meowSound.play(); // Воспроизводим "мяу"
    moveCat();
});

// Функция для обратного отсчета времени
function startTimer() {
    gameInterval = setInterval(() => {
        timeLeft--;
        timeDisplay.textContent = timeLeft;

        if (timeLeft <= 0) {
            clearInterval(gameInterval);
            gameOverSound.play(); // Воспроизводим звук окончания игры
            alert(`Игра окончена! Ваш счет: ${score}`);
            resetGame();
        }
    }, 1000);
}

// Функция для сброса игры
function resetGame() {
    score = 0;
    timeLeft = 30;
    scoreDisplay.textContent = score;
    timeDisplay.textContent = timeLeft;
    moveCat();
    setTimeout(startTimer, 1000); // Перезапуск таймера через секунду
}

// Запуск игры
moveCat(); // Перемещаем кота в случайную позицию при загрузке
startTimer(); // Запускаем таймер