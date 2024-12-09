import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 235)
GREEN = (0, 255, 0)

# Переменные для игры
gravity = 0.25
bird_movement = 0
game_active = True
score = 0

# Загрузка изображений
bird = pygame.image.load("./bird.png").convert_alpha()
bird = pygame.transform.scale(bird, (50, 50))
bird_rect = bird.get_rect(center=(100, HEIGHT // 2))

pipe_surface = pygame.Surface((70, 400))
pipe_surface.fill(GREEN)

# Функции
def create_pipe():
    pipe_height = random.randint(200, 400)
    top_pipe = pipe_surface.get_rect(midbottom=(WIDTH + 50, pipe_height - 150))
    bottom_pipe = pipe_surface.get_rect(midtop=(WIDTH + 50, pipe_height))
    return top_pipe, bottom_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return [pipe for pipe in pipes if pipe.right > 0]

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= HEIGHT:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= HEIGHT:
        return False
    return True

# Таймер для создания труб
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipes = []

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 8
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                pipes.clear()
                bird_rect.center = (100, HEIGHT // 2)
                bird_movement = 0
                score = 0
        if event.type == SPAWNPIPE:
            pipes.extend(create_pipe())

    # Рисование фона
    screen.fill(BLUE)

    if game_active:
        # Птица
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird, bird_rect)

        # Трубы
        pipes = move_pipes(pipes)
        draw_pipes(pipes)

        # Проверка столкновений
        game_active = check_collision(pipes)

        # Учет очков
        for pipe in pipes:
            if 95 < pipe.centerx < 105:
                score += 1
    else:
        font = pygame.font.Font(None, 50)
        text_surface = font.render(f'Game Over! Score: {score}', True, BLACK)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_surface, text_rect)

    # Обновление экрана
    pygame.display.update()
    clock.tick(60)
