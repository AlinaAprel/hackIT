import pygame
import random
import math
import sys

# Инициализация Pygame
pygame.init()

# Константы игры
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paratrooper Game")
clock = pygame.time.Clock()

# Параметры башни и объектов
tower_x, tower_y = WIDTH // 2, HEIGHT - 50
tower_radius = 30
paratrooper_size = 20
shot_speed = 10

# Игровые переменные
paratroopers = []
shots = []
angle = 90  # Угол стрельбы (в градусах, вертикально вверх)
score = 0
game_over = False

# Шрифт
font = pygame.font.SysFont("Arial", 24)

def draw_tower():
    """Отрисовка башни."""
    pygame.draw.circle(screen, GREEN, (tower_x, tower_y), tower_radius)

def draw_paratroopers():
    """Отрисовка парашютистов."""
    for paratrooper in paratroopers:
        pygame.draw.circle(screen, RED, paratrooper, paratrooper_size // 2)

def draw_shots():
    """Отрисовка выстрелов."""
    for shot in shots:
        pygame.draw.circle(screen, WHITE, (int(shot[0]), int(shot[1])), 5)

def spawn_paratrooper():
    """Создание нового парашютиста."""
    if random.random() < 0.02:  # 2% шанс спавна
        x = random.randint(paratrooper_size, WIDTH - paratrooper_size)
        paratroopers.append([x, 0])

def move_paratroopers():
    """Движение парашютистов вниз."""
    global game_over
    for paratrooper in paratroopers[:]:
        paratrooper[1] += 2
        if paratrooper[1] > HEIGHT - tower_radius:
            game_over = True
            break

def move_shots():
    """Движение выстрелов."""
    for shot in shots[:]:
        shot[0] += shot[2]  # Изменение координаты x по скорости
        shot[1] += shot[3]  # Изменение координаты y по скорости
        if shot[1] < 0 or shot[0] < 0 or shot[0] > WIDTH:  # Если выстрел выходит за экран
            shots.remove(shot)

def handle_collisions():
    """Обработка столкновений выстрелов и парашютистов."""
    global score
    for shot in shots[:]:
        for paratrooper in paratroopers[:]:
            if (paratrooper[0] - paratrooper_size < shot[0] < paratrooper[0] + paratrooper_size and
                paratrooper[1] - paratrooper_size < shot[1] < paratrooper[1] + paratrooper_size):
                shots.remove(shot)
                paratroopers.remove(paratrooper)
                score += 10
                break

def draw_score():
    """Отображение счёта."""
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

def main():
    global angle, shots, paratroopers, score, game_over

    # Игровой цикл
    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Управление углом
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            angle += 2
        if keys[pygame.K_RIGHT]:
            angle -= 2

        # Ограничение угла (0° до 180°)
        angle = max(0, min(180, angle))

        # Выстрелы
        if keys[pygame.K_SPACE]:
            if not shots or shots[-1][1] < tower_y - 20:  # Ограничение частоты выстрелов
                rad = math.radians(angle)
                vx = -shot_speed * math.cos(rad)
                vy = -shot_speed * math.sin(rad)
                shots.append([tower_x, tower_y, vx, vy])

        # Обновление объектов
        spawn_paratrooper()
        move_paratroopers()
        move_shots()
        handle_collisions()

        # Рисуем всё
        draw_tower()
        draw_paratroopers()
        draw_shots()
        draw_score()

        # Рисуем направление выстрела
        rad = math.radians(angle)
        end_x = tower_x - 50 * math.cos(rad)
        end_y = tower_y - 50 * math.sin(rad)
        pygame.draw.line(screen, WHITE, (tower_x, tower_y), (end_x, end_y), 2)

        # Проверка конца игры
        if game_over:
            game_over_text = font.render("Game Over! Press R to Restart", True, RED)
            screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
            pygame.display.flip()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        paratroopers.clear()
                        shots.clear()
                        score = 0
                        game_over = False
                        return

        # Обновление экрана
        pygame.display.flip()
        clock.tick(FPS)

# Запуск игры
if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        pygame.quit()
        sys.exit()
