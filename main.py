# doing my first commit

import pygame
import random
# initialisation 
pygame.init()

#screen
screen = pygame.display.set_mode((800,600))
# background
background = pygame.image.load('background.jpg')

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

# enemy
enemyImg = pygame.image.load("monster.png")
enemyX = random.randint(0,768)
enemyY = random.randint(50, 150)
enemyX_change = 1
enemyY_change = 40

def enemy(x,y):
    screen.blit(enemyImg,(enemyX,enemyY))

# Game running

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# keystroke to move the spaceship
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change -= 2
        elif event.key == pygame.K_RIGHT:
            playerX_change += 2
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
    

# player boundries
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

# enemy movement change
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 1
        enemyY += enemyY_change
    elif enemyX >= 768:
        enemyX_change = -1
        enemyY += enemyY_change

    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
