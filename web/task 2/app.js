const colors = {
    '#e54040': 'красный',
    '#60e659': 'зеленый',
    '#59b2e6': 'синий',
    '#e6df59': 'желтый'
};

const colorKeys = Object.keys(colors); // Массив HEX-кодов

const gameArea = document.getElementById('gameArea');
const targetColorElement = document.getElementById('targetColor');
const instructionElement = document.getElementById('instruction');
const scoreElement = document.getElementById('score');
const timerElement = document.getElementById('timer');
const startButton = document.getElementById('startButton');

let score = 0;
let timeLeft = 0;
let timerInterval;
let targetColor;

function getRandomColor() {
    return colorKeys[Math.floor(Math.random() * colorKeys.length)]; // Возвращаем случайный HEX-код
}

function generateCircles() {
    gameArea.innerHTML = '';
    const numberOfCircles = Math.floor(Math.random() * 5) + 3; // От 3 до 7 кружков
    const availableColors = [];

    // Сначала генерируем кружки и собираем их цвета
    for (let i = 0; i < numberOfCircles; i++) {
        const color = getRandomColor();
        availableColors.push(color);

        const circle = document.createElement('div');
        circle.classList.add('circle');
        circle.style.backgroundColor = color;
        circle.addEventListener('click', () => handleCircleClick(color));
        gameArea.appendChild(circle);
    }

    // Теперь выбираем случайный цвет из доступных
    targetColor = availableColors[Math.floor(Math.random() * availableColors.length)];
    targetColorElement.textContent = colors[targetColor]; // Используем название цвета
    targetColorElement.style.color = targetColor; // Устанавливаем цвет текста
}

function handleCircleClick(color) {
    if (color === targetColor) {
        score += 10;
    } else {
        score -= 10;
    }
    scoreElement.textContent = `Очки: ${score}`;
    generateCircles();
}

function startGame() {
    score = 0;
    timeLeft = 30; // Установите желаемое время
    scoreElement.textContent = `Очки: ${score}`;
    timerElement.textContent = `Время: ${timeLeft}`;
    generateCircles();

    clearInterval(timerInterval);
    timerInterval = setInterval(() => {
        timeLeft--;
        timerElement.textContent = `Время: ${timeLeft}`;
        if (timeLeft <= 0) {
            clearInterval(timerInterval);
            alert(`Игра окончена! Ваш счет: ${score}`);
        }
    }, 1000);
}

startButton.addEventListener('click', startGame);