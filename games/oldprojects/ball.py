import pygame
width = 600
height = 400

ballR = 20

x = width/2
y = height/2

speed_x = 4
speed_y = 4
pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Shar')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    x += speed_x
    y += speed_y
    screen.fill((0, 0, 0))

    ball = pygame.draw.circle(screen, (255, 255, 255), (x, y), ballR)

    if ball.topleft[0] < 0 or ball.bottomright[0] >= width:
        speed_x = -speed_x
    if ball.topleft[1] < 0 or ball.bottomright[1] >= height:
        speed_y = -speed_y
    clock.tick(60)
    pygame.display.update()

