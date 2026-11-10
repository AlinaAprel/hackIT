import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Шутер: Стрельба")
clock = pygame.time.Clock()

bg = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))
player_img = pygame.transform.scale(pygame.image.load("player.png"), (60, 60))
meteor_img = pygame.transform.scale(pygame.image.load("meteor.png"), (50, 50))

player_x, player_y = 270, 700
player_speed = 7

# --- НОВЫЕ ПЕРЕМЕННЫЕ ДЛЯ СТРЕЛЬБЫ ---
bullets = []  # Список для хранения пуль
bullet_speed = 15  # Пуля должна лететь быстрее метеоритов!
YELLOW = (255, 255, 0) # Цвет лазера

# Список метеоритов (сокращенный вариант без разной скорости для простоты)
meteors = []
for i in range(7):
    m = pygame.Rect(random.randint(0, WIDTH-50), random.randint(-500, -50), 50, 50)
    meteors.append(m)

running = True
while running:
    # 1. ОБРАБОТКА СОБЫТИЙ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # --- ЛОГИКА ВЫСТРЕЛА ---
        # Проверяем, было ли нажатие кнопки клавиатуры
        if event.type == pygame.KEYDOWN:
            # Если нажали именно ПРОБЕЛ
            if event.key == pygame.K_SPACE:
                # Создаем пулю (прямоугольник). Ширина 4, высота 15.
                # Координаты: центр корабля по X, верх корабля по Y
                bullet_x = player_x + 30 - 2 # 30 - половина корабля, 2 - половина пули
                bullet_y = player_y
                b_rect = pygame.Rect(bullet_x, bullet_y, 4, 15)
                
                bullets.append(b_rect) # Добавляем пулю в список!

    # 2. УПРАВЛЕНИЕ КОРАБЛЕМ
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0: player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 60: player_x += player_speed

    # 3. ПОЛЕТ ПУЛЬ И УБОРКА МУСОРА
    # Перебираем КОПИЮ списка пуль (bullets[:])
    for b in bullets[:]:
        b.y -= bullet_speed  # Пуля летит ВВЕРХ
        
        # Если пуля улетела за экран (y < 0), удаляем ее из ОРИГИНАЛЬНОГО списка
        if b.y < 0:
            bullets.remove(b)

    # 4. ПОЛЕТ МЕТЕОРИТОВ
    for m in meteors:
        m.y += 5
        if m.y > HEIGHT:
            m.y = random.randint(-500, -50)
            m.x = random.randint(0, WIDTH - 50)

    # 5. ОТРИСОВКА
    screen.blit(bg, (0, 0))
    screen.blit(player_img, (player_x, player_y))
    
    for m in meteors:
        screen.blit(meteor_img, (m.x, m.y))
        
    # Рисуем все пули из списка
    for b in bullets:
        pygame.draw.rect(screen, YELLOW, b)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()