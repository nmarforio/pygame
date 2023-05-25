# doing my first commit

import pygame
import random
import math
from pygame import mixer
# initialisation 
pygame.init()

#screen --> creating the high and the width of the window
screen = pygame.display.set_mode((800,600)) 
# background
background = pygame.image.load('background.jpg')
#background music
mixer.music.load('background.mp3')
mixer.music.play(-1)

#caption and Icon  --> to change the Icon when you open the program
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("arcade.png")
pygame.display.set_icon(icon)

# score
score_value= 0
font = pygame.font.Font('freesansbold.ttf', 32) #freesans only free font in pygame, 32 is the size
textX = 10
textY = 540
def show_score (x,y):
    score = font.render('Score: '+ str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))

# player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

def player (x,y):
    screen.blit(playerImg, (x,y))  #blit is to draw in your window without nothing is showing 

# list of enemy --> is the sqarebrakets if you wanna use it must be .append in a for loop
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_enemies = 6

for i in range (num_enemies):
    enemyImg.append(pygame.image.load("monster.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1) 
    enemyY_change.append(40)


def enemy(x, y ,i):
        screen.blit(enemyImg[i],(x,y))
    

# bullet 
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = -2
bullet_state = "ready"  #ready you dont see the bullet / fire yes


def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x, y))

def kill_monster(monsterX,monsterY,bulletX,bulletY):
    distance = math.sqrt((math.pow(monsterX-bulletX, 2)) + (math.pow(monsterY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
    

   
    
# Game running
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    show_score(textX,textY)
   
    
# to quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# keystroke to move the spaceship and bullets
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if bullet_state == 'ready':
                bullet_sound = mixer.Sound('laser.wav')
                bullet_sound.play()
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
    for i in range (num_enemies):
        enemyX[i] += enemyX_change[i] #the [i] is to know which of the 6 enemies we are pointing that's why is everywhere 
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]
        # collision
        collision = kill_monster(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            collision_sound= mixer.Sound('kill.mp3')
            collision_sound.play()
            bulletY = 480
            bullet_state = 'ready'     
            score_value += 1
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)
    

# bullet movements 
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY += bulletY_change
       

       
# called function
    player(playerX,playerY)
    pygame.display.update()
