import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Магическая Кисть (Paint)")

WHITE = (255, 255, 255)

clock = pygame.time.Clock()
FPS = 120  # Делаем FPS повыше, чтобы линия от мышки была более плавной

# Заливаем экран белым цветом ОДИН РАЗ до начала цикла
screen.fill(WHITE)

# Текущий цвет кисти (изначально черный)
brush_color = (0, 0, 0)
brush_size = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Очистка экрана по пробелу (разовое нажатие!)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill(WHITE)  # Заливаем экран заново
            # Если нажать 'C', меняем цвет на случайный
            if event.key == pygame.K_c:
                brush_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # --- ЛОГИКА РИСОВАНИЯ ---
    # Получаем координаты мыши
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # Получаем состояние кнопок мыши. 
    # Это список (Левая, Колесико, Правая). Индекс 0 - это левая кнопка.
    mouse_buttons = pygame.mouse.get_pressed()
    
    # Если зажата левая кнопка мыши
    if mouse_buttons[0]:
        # Рисуем круг в координатах мыши
        # ВАЖНО: Мы не делаем screen.fill() в цикле, поэтому круги остаются на экране!
        pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), brush_size)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()