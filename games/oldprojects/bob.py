import pygame
import math
BLACK = (0,0,0)

class Bob(pygame.sprite.Sprite):
  def __init__(self, color , height , width):
    super().__init__()
    self.image = pygame.Surface([width , height])
    self.image.fill(BLACK)
    self.image.set_colorkey(BLACK)
    
    #Loading the image for the character
    self.img = pygame.image.load("char.jfif")
    #creating a copy of the image
    self.img_orig = self.img.copy()
    #defining the starting angle of the character image
    self.angle = 0
    
    self.velocity = 5
    self.rect = self.img_orig.get_rect()
    self.x, self.y = self.rect.center
    
  def rotate(self, change_angle):
    self.angle += change_angle
    self.img = pygame.transform.rotate(self.img_orig, self.angle)
    self.rect = self.img.get_rect(center = self.rect.center)
    
  def move(self, distance):
    self.x += distance * math.cos(math.radians(self.angle + 90))
    self.y -= distance * math.sin(math.radians(self.angle + 90))
    self.rect.center = round(self.x), round(self.y)
    
  def moveLeft(self):
    self.rotate(1) 
  def moveRight(self):
    self.rotate(-1)
    
  def moveForward(self):
    self.move(self.velocity)
  def moveDown(self):
    self.move(-self.velocity)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
      pSprite.moveForward()
    if keys[pygame.K_DOWN]:
      pSprite.moveDown()
    if keys[pygame.K_LEFT]:
      pSprite.moveLeft()
    if keys[pygame.K_RIGHT]:
      pSprite.moveRight()

    #---- Game Logic Here
    
      
    #--- Drawing Code Here
    #Reset the screen to blank
    screen.fill(BLUE)
    #Draw Play Area
    
    #Draw Sprites
    screen.blit(pSprite.img,(pSprite.rect.x, pSprite.rect.y))
