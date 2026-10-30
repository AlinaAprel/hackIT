#Продолжаем работать в том же файле. Давай добавим "прицел" (маленький красный кружок), который будет всегда следовать за курсором мыши.

import pygame

pygame.init()

# Настройки окна
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Управление клавиатурой и мышью")

# Цвета
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()
FPS = 60

# --- ПЕРЕМЕННЫЕ ИГРОКА (Клавиатура) ---
player_x = 400
player_y = 300
player_size = 50
player_speed = 5

running = True
while running:
    # 1. ОБРАБОТКА СОБЫТИЙ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. ОБНОВЛЕНИЕ ЛОГИКИ
    
    # --- Логика Клавиатуры (Игрок) ---
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:    # Идем влево
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:   # Идем вправо
        player_x += player_speed
    if keys[pygame.K_UP]:      # Идем вверх
        player_y -= player_speed
    if keys[pygame.K_DOWN]:    # Идем вниз
        player_y += player_speed

    # --- Логика Мыши (Прицел) ---
    # Получаем текущие координаты курсора мыши на экране
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # 3. ОТРИСОВКА
    screen.fill(BLACK)  # Очищаем экран
    
    # Рисуем игрока (желтый квадрат)
    pygame.draw.rect(screen, YELLOW, (player_x, player_y, player_size, player_size))
    
    # Рисуем прицел (красный кружок) в координатах мыши
    # Радиус круга делаем небольшим, например 10
    pygame.draw.circle(screen, RED, (mouse_x, mouse_y), 10)

    pygame.display.flip()  # Показываем новый кадр
    clock.tick(FPS)        # Держим 60 кадров в секунду

pygame.quit()