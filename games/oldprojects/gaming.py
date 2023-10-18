import pygame

pygame.init()
win=pygame.display.set_mode((1200,700))
pygame.display.set_caption("Game")

bg = pygame.image.load('bgg.jpg')

playerLeft = [pygame.image.load('m_pc_stand_3.png'), pygame.image.load('m_pc_stand_4.png'), pygame.image.load('m_pc_stand_3.png'), pygame.image.load('m_pc_stand_4.png'), pygame.image.load('m_pc_stand_3.png'), pygame.image.load('m_pc_stand_4.png'), pygame.image.load('m_pc_stand_3.png'), pygame.image.load('m_pc_stand_4.png')]
playerRight = [pygame.image.load('m_pc_stand.png'), pygame.image.load('m_pc_stand_2.png'), pygame.image.load('m_pc_stand.png'), pygame.image.load('m_pc_stand_2.png'), pygame.image.load('m_pc_stand.png'), pygame.image.load('m_pc_stand_2.png'), pygame.image.load('m_pc_stand_2.png'), pygame.image.load('m_pc_stand_2.png')]
playerUp = [pygame.image.load('m_pc_stand.png'), pygame.image.load('m_pc_stand_2.png'), pygame.image.load('m_pc_stand.png'), pygame.image.load('m_pc_stand_2.png'), pygame.image.load('m_pc_stand.png'), pygame.image.load('m_pc_stand_2.png'), pygame.image.load('m_pc_stand_2.png'), pygame.image.load('m_pc_stand_2.png')]
playerDown = [pygame.image.load('m_pc_stand.png'), pygame.image.load('m_pc_stand_2.png'), pygame.image.load('m_pc_stand.png'), pygame.image.load('m_pc_stand_2.png'), pygame.image.load('m_pc_stand.png'), pygame.image.load('m_pc_stand_2.png'), pygame.image.load('m_pc_stand_2.png'), pygame.image.load('m_pc_stand_2.png')]
playerStand = [pygame.image.load('m_pc_stand.png'), pygame.image.load('m_pc_stand_2.png'), pygame.image.load('m_pc_stand.png'), pygame.image.load('m_pc_stand_2.png'), pygame.image.load('m_pc_stand.png'), pygame.image.load('m_pc_stand_2.png'), pygame.image.load('m_pc_stand_2.png'), pygame.image.load('m_pc_stand_2.png')]

clock=pygame.time.Clock()

x=50
y=425
width=60
height=71
speed=5

up = False
down = False
left= True
right= False
animCount=0

def drawWindow():
    global animCount
    dCount = animCount//5
    print("dCount= ",dCount)
    win.blit(bg,(0,0))

    if animCount + 1 >= 30:
        animCount=0
    elif left:
        win.blit(playerLeft[dCount],(x,y))
        animCount+=1
    elif right:
        win.blit(playerRight[dCount],(x,y))
        animCount+=1
    elif up:
        win.blit(playerUp[dCount],(x,y))
        animCount+=1
    elif down:
        win.blit(playerDown[dCount],(x,y))
        animCount+=1
    else:
        win.blit(playerStand[dCount],(x,y))
        animCount+=1

    pygame.display.update()

run=True

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False

    keys=pygame.key.get_pressed()

    if keys[pygame.K_a]:
        x-=speed
        left=True
        right=False
        down = False
        up = False

    elif keys[pygame.K_d]:
        x+=speed
        left=True
        right=False
        down = False
        up = False

    elif keys[pygame.K_w]:
        y-=speed
        left=False
        right= False
        down = False
        up = True

    elif keys[pygame.K_s]:
        y+=speed
        down = True
        up = False
        left=False
        right= False

    else:
        right=False
        left=False
        up = False
        down = False
        animCount=0

    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()

    drawWindow()