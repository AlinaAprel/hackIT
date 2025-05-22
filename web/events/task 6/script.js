// 1. Создай переменную draggable
// 2. Создай переменную isDragging со значением false
// 3. Создай переменные offsetX, offsetY без значений через ключевое слово let

// #1 //
// #2 //
// #3 //

draggable.addEventListener('mousedown', function(e) {
  isDragging = true;
  offsetX = e.clientX - draggable.offsetLeft;
  offsetY = e.clientY - draggable.offsetTop;
});

document.addEventListener('mousemove', function(e) {
  if (isDragging) {
    draggable.style.left = (e.clientX - offsetX) + 'px';
    draggable.style.top = (e.clientY - offsetY) + 'px';
  }
});

document.addEventListener('mouseup', function() {
  isDragging = false;
});
