#Сделать так, чтобы корабль стрелял не одним лазером из центра,
#  а двумя лазерами по краям крыльев одновременно. 
# Добавить звук выстрела.
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 30, bold=True)

# Опционально: загрузка звуков
# laser_snd = pygame.mixer.Sound("laser.wav")
# explosion_snd = pygame.mixer.Sound("explosion.wav")

bg = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))
player_img = pygame.transform.scale(pygame.image.load("player.png"), (60, 60))
meteor_img = pygame.transform.scale(pygame.image.load("meteor.png"), (50, 50))

player_x, player_y = 270, 700
player_speed = 7
score = 0

bullets = []
bullet_speed = 15
YELLOW = (255, 255, 0)

meteors = []
for i in range(7):
    meteors.append(pygame.Rect(random.randint(0, WIDTH-50), random.randint(-500, -50), 50, 50))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # --- ДВОЙНОЙ ВЫСТРЕЛ ---
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # laser_snd.play() # Звук выстрела
                
                # Левая пуля
                b_left = pygame.Rect(player_x + 5, player_y + 20, 4, 15)
                # Правая пуля
                b_right = pygame.Rect(player_x + 51, player_y + 20, 4, 15)
                
                bullets.append(b_left)
                bullets.append(b_right)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0: player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 60: player_x += player_speed

    # Движение пуль
    for b in bullets[:]:
        b.y -= bullet_speed
        if b.y < 0:
            bullets.remove(b)

    # --- ЛОГИКА МЕТЕОРИТОВ И СТОЛКНОВЕНИЙ СО СТРЕЛЬБОЙ ---
    for m in meteors:
        m.y += 5
        if m.y > HEIGHT:
            m.y = random.randint(-500, -50)
            m.x = random.randint(0, WIDTH - 50)
            
        # Проверяем, не попала ли в этот метеорит какая-нибудь пуля
        for b in bullets[:]: # Снова используем копию, так как можем удалить пулю!
            if m.colliderect(b):
                # ВЗРЫВ!
                # explosion_snd.play()
                score += 10 # Даем очки
                
                # Телепортируем метеорит наверх (он "возродился")
                m.y = random.randint(-500, -50)
                m.x = random.randint(0, WIDTH - 50)
                
                # Удаляем пулю, чтобы она не пролетела насквозь и не убила еще кого-то
                if b in bullets:
                    bullets.remove(b)
                
                break # Выходим из внутреннего цикла (пуля уже уничтожена)

    # Отрисовка
    screen.blit(bg, (0, 0))
    screen.blit(player_img, (player_x, player_y))
    
    for m in meteors:
        screen.blit(meteor_img, (m.x, m.y))
        
    for b in bullets:
        pygame.draw.rect(screen, YELLOW, b)
        
    # Отрисовка счета
    score_text = font.render(f"Счет: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()