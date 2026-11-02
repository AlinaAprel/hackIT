# Задание: Взять код с прошлого урока. Заменить скучный print(score) в 
# консоли на красивый счетчик в левом верхнем углу. Добавить фоновую музыку и "дзинь" при сборе.

import pygame
import random

pygame.init() # Эта команда также автоматически запускает pygame.font и pygame.mixer

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Урок 6: Звук и Текст")
clock = pygame.time.Clock()

# --- ШАГ 1 ДЛЯ ТЕКСТА: Создаем шрифт ---
# Используем системный шрифт Arial, размер 36, жирный=True
my_font = pygame.font.SysFont("Arial", 36, bold=True)
WHITE = (255, 255, 255) # Цвет для текста

# --- НАСТРОЙКА ЗВУКОВ ---
# Загружаем короткий звук (wav/ogg)
coin_fx = pygame.mixer.Sound("coin_sound.wav")
# Настраиваем громкость звука (от 0.0 до 1.0)
coin_fx.set_volume(0.5)

# Загружаем и запускаем фоновую музыку (mp3/ogg)
pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1) # -1 означает "повторять бесконечно"

# --- ИГРОВЫЕ ПЕРЕМЕННЫЕ ---
bg = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))
player_img = pygame.transform.scale(pygame.image.load("player.png"), (80, 80))
coin_img = pygame.transform.scale(pygame.image.load("coin.png"), (40, 40))

player_x, player_y = 400, 300
coin_x, coin_y = random.randint(50, 700), random.randint(50, 500)
score = 0  # Наша переменная счета

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_x -= 6
    if keys[pygame.K_RIGHT]: player_x += 6
    if keys[pygame.K_UP]: player_y -= 6
    if keys[pygame.K_DOWN]: player_y += 6

    # Коллизии
    player_rect = pygame.Rect(player_x, player_y, 80, 80)
    coin_rect = pygame.Rect(coin_x, coin_y, 40, 40)

    if player_rect.colliderect(coin_rect):
        score += 1 # Увеличиваем счет
        coin_fx.play() # ВОСПРОИЗВОДИМ ЗВУК СБОРА!
        # Телепортируем монетку
        coin_x, coin_y = random.randint(50, 700), random.randint(50, 500)

    # Отрисовка картинок
    screen.blit(bg, (0, 0))
    screen.blit(coin_img, (coin_x, coin_y))
    screen.blit(player_img, (player_x, player_y))

    # --- ШАГ 2 ДЛЯ ТЕКСТА: Рендеринг (превращаем строку в картинку) ---
    # Передаем: текст (собираем через f-строку), сглаживание (True), цвет
    score_text = my_font.render(f"Счет: {score}", True, WHITE)
    
    # --- ШАГ 3 ДЛЯ ТЕКСТА: Отрисовка на экране ---
    screen.blit(score_text, (20, 20)) # Рисуем в левом верхнем углу (x=20, y=20)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
