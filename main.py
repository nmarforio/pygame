# doing my first commit

import pygame

# initialisation 
pygame.init()

#screen

screen = pygame.display.set_mode((800,600))

#caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("arcade.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

def player (x,y):
    screen.blit(playerImg, (x,y))

# Game running

running = True
while running:
    screen.fill((0,0,0))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# keystroke to move the spaceship
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX -= 0.5
        elif event.key == pygame.K_RIGHT:
            playerX += 0.5
    

    

    playerX_change + playerX
    player(playerX,playerY)
    pygame.display.update()
