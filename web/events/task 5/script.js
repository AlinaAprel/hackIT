// 1. Создай переменную follower

// #1 //  
document.addEventListener('mousemove', function(e) {
  follower.style.left = e.clientX - 25 + 'px';
  follower.style.top = e.clientY - 25 + 'px';
});
