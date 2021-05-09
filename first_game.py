import pygame

# initialize pygame
pygame.init()

# create the screen
screen= pygame.display.set_mode((800,600))

pygame.display.set_caption("SPACE INVADERS")
icon=pygame.image.load("game.png")
pygame.display.set_icon(icon)

# Adding player
playerImg=pygame.image.load('spaceship.png')
playerX=370
playerY=480
playerX_change=0

def player(x,y):
    #blit --> draw
    screen.blit(playerImg,(x,y))


# game loop
running=True
while running:

    # RGB color to RGB background color
    screen.fill((200, 40, 58))

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running = False
        if event.type ==pygame.KEYDOWN:
            if event.type ==pygame.K_LEFT:
                playerX_change= -0.1
            if event.type==pygame.K_RIGHT:
                playerX_change= 0.1

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0

    playerX += playerX_change

    # crate boundaries
    if playerX <= 0:
        playerX=0
    elif playerX >= 736:
        playerX=736

    player(playerX,playerY)

    pygame.display.update()



