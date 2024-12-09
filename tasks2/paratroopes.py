import pygame
import random
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

# Игровые ресурсы
tower_width, tower_height = 60, 20
paratrooper_size = 20
shot_width, shot_height = 5, 10

# Позиции
tower_x = WIDTH // 2 - tower_width // 2
tower_y = HEIGHT - tower_height
paratroopers = []
shots = []

# Игровые переменные
score = 0
game_over = False

# Шрифты
font = pygame.font.SysFont("Arial", 24)

def draw_tower():
    """Отрисовка башни."""
    pygame.draw.rect(screen, GREEN, (tower_x, tower_y, tower_width, tower_height))

def draw_paratroopers():
    """Отрисовка парашютистов."""
    for paratrooper in paratroopers:
        pygame.draw.circle(screen, RED, paratrooper, paratrooper_size // 2)

def draw_shots():
    """Отрисовка выстрелов."""
    for shot in shots:
        pygame.draw.rect(screen, WHITE, (shot[0], shot[1], shot_width, shot_height))

def spawn_paratrooper():
    """Создание нового парашютиста."""
    if random.random() < 0.02:  # 2% шанс на спавн каждого кадра
        x = random.randint(paratrooper_size, WIDTH - paratrooper_size)
        paratroopers.append([x, 0])

def move_paratroopers():
    """Движение парашютистов вниз."""
    global game_over
    for paratrooper in paratroopers[:]:
        paratrooper[1] += 2  # Скорость падения
        if paratrooper[1] > HEIGHT - tower_height:
            game_over = True  # Парашютист достиг земли
            break

def move_shots():
    """Движение выстрелов вверх."""
    for shot in shots[:]:
        shot[1] -= 5  # Скорость выстрела
        if shot[1] < 0:
            shots.remove(shot)

def handle_collisions():
    """Обработка столкновений."""
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
    global tower_x, shots, paratroopers, score, game_over

    # Игровой цикл
    running = True
    while running:
        screen.fill(BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and tower_x > 0:
            tower_x -= 5
        if keys[pygame.K_RIGHT] and tower_x < WIDTH - tower_width:
            tower_x += 5
        if keys[pygame.K_SPACE]:
            if not shots or shots[-1][1] < tower_y - 20:  # Ограничение частоты выстрелов
                shots.append([tower_x + tower_width // 2 - shot_width // 2, tower_y])
        
        # Обновление состояния игры
        spawn_paratrooper()
        move_paratroopers()
        move_shots()
        handle_collisions()

        # Рисуем все объекты
        draw_tower()
        draw_paratroopers()
        draw_shots()
        draw_score()

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
