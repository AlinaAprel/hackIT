// Получаем элементы DOM
const hero = document.querySelector('#hero');

// По аналогии с переменной hero, создай переменные:
//    1. moveLeftBtn
//    2. moveRightBtn
//    3. jumpBtn
// Далее ищем обработчики событий для кнопок

// #1 //
// #2 //
// #3 //

// Начальные параметры героя
let position = 225; // начальная позиция по X
let isJumping = false;

// Функция для обновления позиции героя
function updateHeroPosition() {
    hero.style.left = position + 'px';
}

// Обработчики событий для кнопок
moveLeftBtn.onclick = function() {
    if (position > 0) {
        position -= 20;
        updateHeroPosition();
    }
};

// По аналогии обработчика события для moveLeftBtn, создаем:
// 1. Обработчик события для moveRightBtn
//    Внутри проверка:
//        if (position < 450) {
//            position += 20;
//           updateHeroPosition();
//       }

// 2. Обработчик события для jumpBtn
//    Внутри проверка:
//        if (!isJumping) {
//            jump();
//        }
// Далее переходим к обработчикам событий дл клавиатуры

// Функция прыжка
function jump() {
    isJumping = true;
    let jumpHeight = 0;
    const jumpUp = setInterval(() => {
        jumpHeight += 5;
        hero.style.bottom = (50 + jumpHeight) + 'px';
        
        if (jumpHeight >= 100) {
            clearInterval(jumpUp);
            const jumpDown = setInterval(() => {
                jumpHeight -= 5;
                hero.style.bottom = (50 + jumpHeight) + 'px';
                
                if (jumpHeight <= 0) {
                    clearInterval(jumpDown);
                    hero.style.bottom = '50px';
                    isJumping = false;
                }
            }, 20);
        }
    }, 20);
}

// Обработчики событий клавиатуры

// По аналогии с ArrowLeft прописываем:
// 1. ArrowRight с условием position меньше 450. Увеличиваем position на 20,
//    вызываем функцию updateHeroPosition()

// 2. ArrowUp с условием !isJumping. Внутри вызов функции jump()
document.onkeydown = function(event) {
    switch(event.key) {
        case 'ArrowLeft':
            if (position > 0) {
                position -= 20;
                updateHeroPosition();
            }
            break;
        // 1 //
        
        // 2 //
    }
};