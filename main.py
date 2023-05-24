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
enemyX = random.randint(0,736)
enemyY = random.randint(50, 150)
enemyX_change = 1
enemyY_change = 40
enemy_state = "alive"

def enemy(x,y):
    if enemy_state == "alive":
        screen.blit(enemyImg,(enemyX,enemyY))
    if enemy_state == "dead":
        print ("GOOD JOB")
    

# bullet 
bulletImg = pygame.image.load('bullet.png')
bulletY = 480
bulletY_change = -2
bullet_state = "ready"  #ready you dont see the bullet / fire yes


def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x, y))

# def kill_monster(xmonster,ymonster,xbullet,ybullet):
#     if xmonster and ymonster == xbullet and ybullet:
#         global bullet_state
#         global enemy_state
#         bullet_state = "ready" 
#         enemy_state = "dead"


    

# Game running
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
   
    
# to quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# keystroke to move the spaceship and bullets
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if bullet_state == 'ready':
                bulletX = playerX
                fire_bullet(bulletX,bulletY)

            
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


# enemy movements
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 1
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -1
        enemyY += enemyY_change

# bullet movements 
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY += bulletY_change
        
        
    
       
# called function
    
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
