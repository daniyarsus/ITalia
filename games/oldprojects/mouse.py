import pygame
pygame.init()
screen = pygame.display.set_mode((550, 550))
 
mouse = pygame.image.load('mouse.jpg')
mouseX = 0
mouseY = 225
 
# Скорость движения объекта
speed = 5
 
while True:
    screen.fill((70, 131, 94))
    pygame.time.delay(30)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
     
    # Изменяем значение координаты X
    mouseX += speed
 
    screen.blit(mouse, (mouseX, mouseY))
    pygame.display.update()
