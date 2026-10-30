#Задание: Создать квадрат (игрока), который плавно перемещается по экрану при удержании стрелочек (или клавиш W, A, S, D).

import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Управление клавиатурой")

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()
FPS = 60

# --- ПЕРЕМЕННЫЕ ИГРОКА ---
player_x = 400  # Начальная позиция по X
player_y = 300  # Начальная позиция по Y
player_size = 50  # Размер квадрата (50x50)
player_speed = 5  # Скорость ходьбы

running = True
while running:
    # 1. ОБРАБОТКА СОБЫТИЙ (Разовые действия)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. ОБНОВЛЕНИЕ ЛОГИКИ (Управление)
    # Получаем список ВСЕХ кнопок на клавиатуре. True - если нажата, False - если нет.
    keys = pygame.key.get_pressed()

    # Проверяем конкретные кнопки (можно использовать pygame.K_w, pygame.K_a и т.д.)
    if keys[pygame.K_LEFT]:    # Если зажата стрелка ВЛЕВО
        player_x -= player_speed     # Уменьшаем X (идем влево)
        
    if keys[pygame.K_RIGHT]:   # Если зажата стрелка ВПРАВО
        player_x += player_speed     # Увеличиваем X (идем вправо)
        
    if keys[pygame.K_UP]:      # Если зажата стрелка ВВЕРХ
        player_y -= player_speed     # Уменьшаем Y (идем вверх - помним про перевернутую ось Y!)
        
    if keys[pygame.K_DOWN]:    # Если зажата стрелка ВНИЗ
        player_y += player_speed     # Увеличиваем Y (идем вниз)

    # 3. ОТРИСОВКА
    screen.fill(BLACK)
    
    # Рисуем игрока
    pygame.draw.rect(screen, YELLOW, (player_x, player_y, player_size, player_size))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()