import pygame
import sys

pygame.init()

# Размер окна
WIDTH, HEIGHT = 1920, 1080

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("online room")

# Загрузка изображения персонажа
character_image = pygame.image.load("sprites/2d_kakashi/kakashi_down1.png")
character_rect = character_image.get_rect()

# Загрузка изображений для анимации движения
character_images = {
    'left': [pygame.image.load("sprites/2d_kakashi/kakashi_left1.png"), pygame.image.load("sprites/2d_kakashi/kakashi_left2.png"), pygame.image.load("sprites/2d_kakashi/kakashi_left3.png")],
    'right': [pygame.image.load("sprites/2d_kakashi/kakashi_right1.png"), pygame.image.load("sprites/2d_kakashi/kakashi_right2.png"), pygame.image.load("sprites/2d_kakashi/kakashi_right3.png")],
    'up': [pygame.image.load("sprites/2d_kakashi/kakashi_up1.png"), pygame.image.load("sprites/2d_kakashi/kakashi_up2.png"), pygame.image.load("sprites/2d_kakashi/kakashi_up3.png")],
    'down': [pygame.image.load("sprites/2d_kakashi/kakashi_down1.png"), pygame.image.load("sprites/2d_kakashi/kakashi_down2.png"), pygame.image.load("sprites/2d_kakashi/kakashi_down3.png")]
}

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Установка начальных координат персонажа
x = 960
y = 540

# Установка скорости движения персонажа
speed = 5

# Начальное направление движения
direction = 'down'

# Основной игровой цикл
running = True
clock = pygame.time.Clock()  # Создаем объект Clock для ограничения FPS
frame_change_time = 221  # 30 FPS

current_frame = 0
last_frame_change = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление персонажем с клавиатуры
    keys = pygame.key.get_pressed()

    moving = False  # Флаг движения

    if keys[pygame.K_a]:
        x -= speed
        direction = 'left'
        moving = True
    if keys[pygame.K_d]:
        x += speed
        direction = 'right'
        moving = True
    if keys[pygame.K_w]:
        y -= speed
        if not moving:  # Если не двигается в горизонтальном направлении
            direction = 'up'
        moving = True
    if keys[pygame.K_s]:
        y += speed
        if not moving:  # Если не двигается в горизонтальном направлении
            direction = 'down'
        moving = True

    # Обновление кадра анимации
    current_time = pygame.time.get_ticks()
    if current_time - last_frame_change > frame_change_time:
        current_frame = (current_frame + 1) % len(character_images[direction])
        last_frame_change = current_time

    # Отобразить персонажа на экране с учетом текущего кадра анимации
    screen.fill((0, 0, 0))  # Очистить экран
    screen.blit(character_images[direction][current_frame], (x, y))  # Отобразить персонажа

    # Завершение Pygame
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    pygame.display.update()

    # Ограничение частоты обновления до 30 FPS
    clock.tick(30)
