#адание 3 (Сложное / Очень эффектное): Экран "Game Over" по времени (Полный код)
#Объединим все! Сделаем игру "Успей за 30 секунд". Как только таймер достигает 30 секунд:
#1)Музыка останавливается.
#2)Игрок больше не может двигаться (или экран полностью заливается черным).
#3)По центру экрана появляется огромная красная надпись "ВРЕМЯ ВЫШЛО" и финальный счет.

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Два разных шрифта (обычный и огромный)
font_ui = pygame.font.SysFont("Arial", 36, bold=True)
font_big = pygame.font.SysFont("Arial", 80, bold=True)

bg = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))
player_img = pygame.transform.scale(pygame.image.load("player.png"), (80, 80))
coin_img = pygame.transform.scale(pygame.image.load("coin.png"), (40, 40))

# Опционально: загрузка музыки и звуков (если у детей они есть)
# coin_fx = pygame.mixer.Sound("coin_sound.wav")
# pygame.mixer.music.load("bg_music.mp3")
# pygame.mixer.music.play(-1)

player_x, player_y = 400, 300
coin_x, coin_y = random.randint(50, 700), random.randint(50, 500)
score = 0

GAME_TIME = 30 # Длительность игры (в секундах)
game_over = False # Флаг окончания игры

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Считаем сколько секунд прошло с запуска (делим миллисекунды на 1000)
    # Это вычисляется каждый кадр
    current_time = pygame.time.get_ticks() // 1000  
    time_left = GAME_TIME - current_time

    # Проверка на окончание времени
    if time_left <= 0:
        time_left = 0
        game_over = True
        pygame.mixer.music.stop() # Выключаем музыку

    # --- ЛОГИКА ИГРЫ (работает только если игра НЕ окончена) ---
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player_x -= 6
        if keys[pygame.K_RIGHT]: player_x += 6
        if keys[pygame.K_UP]: player_y -= 6
        if keys[pygame.K_DOWN]: player_y += 6

        player_rect = pygame.Rect(player_x, player_y, 80, 80)
        coin_rect = pygame.Rect(coin_x, coin_y, 40, 40)

        if player_rect.colliderect(coin_rect):
            score += 1
            # coin_fx.play() 
            coin_x, coin_y = random.randint(50, 700), random.randint(50, 500)

    # --- ОТРИСОВКА ---
    screen.blit(bg, (0, 0))
    screen.blit(coin_img, (coin_x, coin_y))
    screen.blit(player_img, (player_x, player_y))

    # Рисуем UI (Интерфейс)
    score_text = font_ui.render(f"Счет: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))
    
    # Рисуем таймер. Если осталось мало времени (<=5 сек), красим в красный
    timer_color = (255, 0, 0) if time_left <= 5 else (255, 255, 255)
    timer_text = font_ui.render(f"Время: {time_left}", True, timer_color)
    screen.blit(timer_text, (600, 20)) # Рисуем в правом верхнем углу

    # --- ЭКРАН ПОРАЖЕНИЯ (Рисуем поверх всего) ---
    if game_over:
        # Рисуем полупрозрачную черную подложку (создаем отдельный Surface)
        # Эта концепция (Surface с альфа-каналом) может быть сложной, 
        # поэтому можно просто сделать screen.fill((0,0,0))
        
        gameover_text = font_big.render("ВРЕМЯ ВЫШЛО!", True, (255, 50, 50))
        final_score_text = font_ui.render(f"Ваш результат: {score} монет", True, (255, 255, 255))
        
        # Размещаем по центру (приблизительные координаты)
        screen.blit(gameover_text, (120, 200))
        screen.blit(final_score_text, (250, 300))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()