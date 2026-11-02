# Сейчас все астероиды падают с одинаковой скоростью 5. Это скучно.
#Чтобы каждый метеорит имел свою скорость, списка из pygame.Rect недостаточно 
# (он хранит только x, y, ширину, высоту).
#Давайте сделаем список списков: [ [хитбокс1, скорость1], [хитбокс2, скорость2] ].

import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 36, bold=True)

bg = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))
player_img = pygame.transform.scale(pygame.image.load("player.png"), (60, 60))
meteor_img = pygame.transform.scale(pygame.image.load("meteor.png"), (50, 50))

player_x = WIDTH // 2 - 30
player_y = HEIGHT - 100
player_speed = 7
lives = 3 # Жизни игрока (из Задания 2)

meteors = [] 

# Создаем 10 метеоритов
for i in range(10):
    m_x = random.randint(0, WIDTH - 50)
    m_y = random.randint(-800, -50)
    m_rect = pygame.Rect(m_x, m_y, 50, 50)
    
    m_speed = random.randint(3, 9) # Генерируем случайную скорость для ЭТОГО метеорита
    
    # Кладем в список не просто Rect, а мини-список из двух элементов: [Rect, Скорость]
    meteors.append([m_rect, m_speed])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 60:
        player_x += player_speed

    # Обновляем хитбокс игрока каждый кадр
    player_rect = pygame.Rect(player_x, player_y, 60, 60)

    # --- ЛОГИКА МЕТЕОРИТОВ ---
    # Перебираем наш список списков
    for m in meteors:
        # m[0] - это хитбокс (Rect)
        # m[1] - это скорость
        
        m[0].y += m[1]  # Двигаем хитбокс на его собственную скорость

        # Если упал за экран (Задание 1)
        if m[0].y > HEIGHT:
            m[0].y = random.randint(-500, -50)
            m[0].x = random.randint(0, WIDTH - 50)
            
            # Можно заодно поменять ему скорость на новую, чтобы было непредсказуемо!
            m[1] = random.randint(3, 9)

        # Коллизии с игроком (Задание 2)
        if player_rect.colliderect(m[0]):
            lives -= 1
            # Телепортируем метеорит наверх после удара!
            m[0].y = random.randint(-500, -50)
            m[0].x = random.randint(0, WIDTH - 50)

    # --- ОТРИСОВКА ---
    screen.blit(bg, (0, 0))
    screen.blit(player_img, (player_x, player_y))
    
    # Рисуем все метеориты
    for m in meteors:
        screen.blit(meteor_img, (m[0].x, m[0].y))

    # Выводим жизни на экран
    lives_text = font.render(f"Жизни: {lives}", True, (255, 50, 50))
    screen.blit(lives_text, (20, 20))

    # Временный костыль: если жизни упали ниже 0, просто выходим
    if lives <= 0:
        print("ИГРА ОКОНЧЕНА!")
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()