import pygame as game
import pygame.math as math
from pygame.time import Clock
import random as r


game.init()
game.display.set_caption("Asteroids")
screen = game.display.set_mode([800, 600])

time = 0
gameon = True
bgcolor = game.color.Color("#f6cb39")
black = game.color.Color("black")
clock = Clock()

badguy = game.image.load("asteroid.jpg")
badguy = game.transform.scale(badguy, (50, 50))
badguys = []
SPAWNENEMY = 10
CLOCK = 11

game.time.set_timer(SPAWNENEMY, 800)
game.time.set_timer(CLOCK, 1000)

font=game.font.Font(None,20)
timetext=font.render("Time: 0", 0, black)

while gameon:
    screen.fill(bgcolor)

    event = game.event.poll()
    if event.type == SPAWNENEMY:
        # Select a random initial position vector.
        posn = math.Vector2(r.randint(50, 800), r.randint(50, 600))

        # Create a random speed vector.
        speed = r.randint(1, 10)
        dx = r.random()*speed * r.choice((-1, 1))
        dy = r.random()*speed * r.choice((-1, 1))
        vector = math.Vector2(dx, dy)

        # Each badguy item is a [position, speed vector].
        badguys.append([posn, vector])

    if event.type == game.QUIT:
        gameon = False;

    for bg in badguys:
        # Update positions.
        bg[0] += bg[1]  # Update position using speed vector.

    for bg in badguys:
        screen.blit(badguy, bg[0])

    clock.tick(60)
    game.display.flip()
