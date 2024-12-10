import pygame
import random

# Инициализация pygame
pygame.init()

# Настройка окна
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird с вашим фоном")
clock = pygame.time.Clock()

# Загрузка фона (замените 'background.png' на свой файл)
background = pygame.image.load("background.png")  # Убедитесь, что файл в той же папке
background = pygame.transform.scale(background, (WIDTH, HEIGHT))  # Масштабируем фон под размер окна

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Параметры игры
gravity = 0.25
bird_movement = 0
bird = pygame.Rect(100, HEIGHT // 2, 30, 30)
pipe_list = []
pipe_width = 50
pipe_height = 200
pipe_gap = 150

# Загрузка изображений (можно заменить на собственные)
def draw_bird():
    pygame.draw.ellipse(screen, BLACK, bird)

def draw_pipes():
    for pipe in pipe_list:
        pygame.draw.rect(screen, BLACK, pipe)

# Основной игровой цикл
running = True
pipe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_timer, 1500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = -5
        if event.type == pipe_timer:
            pipe_top = random.randint(0, HEIGHT - pipe_gap)
            pipe_list.append(pygame.Rect(WIDTH, pipe_top - pipe_height, pipe_width, pipe_height))
            pipe_list.append(pygame.Rect(WIDTH, pipe_top + pipe_gap, pipe_width, HEIGHT))

    # Движение птицы
    bird_movement += gravity
    bird.y += bird_movement

    # Обновление труб
    pipe_list = [pipe.move(-5, 0) for pipe in pipe_list if pipe.right > 0]

    # Отрисовка фона
    screen.blit(background, (0, 0))  # Рисуем фон

    # Отрисовка других элементов
    draw_bird()
    draw_pipes()

    pygame.display.update()
    clock.tick(30)

pygame.quit()
