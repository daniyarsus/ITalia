import pygame

class Actor(pygame.sprite.Sprite):
    def __init__(self, pos, *grps):
        super().__init__(*grps)
        self.image = pygame.image.load('dEWaX.png').convert_alpha()
        self.image_org = self.image.copy()
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(pos)
        self.direction = pygame.Vector2((0, -1))
        
    def update(self, events, dt):
        pressed = pygame.key.get_pressed()
        
        # if a is pressed, rotate left with 360 degress per second
        if pressed[pygame.K_a]: self.direction.rotate_ip(dt * -360) 
        # if d is pressed, rotate right with 360 degress per second
        if pressed[pygame.K_d]: self.direction.rotate_ip(dt *  360)

        # check if should move forward or backward
        movement = 0
        if pressed[pygame.K_w]: movement =  1
        if pressed[pygame.K_s]: movement = -1
        movement_v = self.direction * movement
        if movement_v.length() > 0:
            movement_v.normalize_ip()
            # move 100px per second in the direction we're facing
            self.pos += movement_v * dt * 100
        
        # rotate the image
        self.image = pygame.transform.rotate(self.image_org, self.direction.angle_to((0, -1)))
        self.rect = self.image.get_rect(center=self.pos)
        

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 480))
    sprites = pygame.sprite.Group()
    Actor((100, 100), sprites)
    clock, dt = pygame.time.Clock(), 0
    while True:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                return
        screen.fill('grey')
        sprites.draw(screen)
        sprites.update(events, dt)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
main()
