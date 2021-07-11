#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pygame
import random
import math


# In[15]:


pygame.init()


# In[19]:


screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('game_icon.png')
pygame.display.set_icon(icon)

background_image = pygame.image.load('background.jpg')


playerImage = pygame.image.load('player.png')
playerX = 370
playerY = 500
playerX_change = 0
playerY_change = 0

enemyImage = pygame.image.load('alien.png')
enemyX = random.randint(0,768)
enemyY = random.randint(50, 150)
enemyX_change = 0.5
enemyY_change = 40

bullet_image = pygame.image.load('bullet.png')
bulletX = 370
bulletY = 500
bulletY_change = 1
bullet_state = "ready"



def player(x,y):
    screen.blit(playerImage, (x, y))

def enemy(x,y):
    screen.blit(enemyImage, (x, y))

    
def bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image, (x+16,y+16))

    
def collision(bulletX, bulletY, enemyX, enemyY):
    dis = math.sqrt( (bulletX-enemyX)**2 + (bulletY-enemyY)**2 )
    if dis < 27:
        return True
    else:
        return False

score = 0
font_object = pygame.font.Font('freesansbold.ttf', 32)

text_rectangle = score_text.get_rect()
text_rectangle.center = (100,100)
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background_image, (0,0))
    score_text = font_object.render(str(score),True,(105,105,105), (0,0,0))
    screen.blit(score_text, text_rectangle)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            print("A different key was pressed")
            if event.key == pygame.K_LEFT:
                print("Left arrow key is pressed")
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                print("Right arrow key is pressed")
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                print("Bullet was fired")
                if bullet_state == "ready":
                    bulletX = playerX
                    bullet(bulletX,bulletY)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("A left or right arrow key was lifted")
                playerX_change = 0
                
    playerX = playerX + playerX_change
    if playerX <=0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768
    player(playerX,playerY)
    
    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"
        
    
    if bullet_state == "fire":
        bullet(bulletX, bulletY)
        bulletY = bulletY - bulletY_change
    
    enemyX = enemyX + enemyX_change
    if enemyX >=768:
        enemyX_change = -0.5
        enemyY = enemyY + enemyY_change
    if enemyX <=0:
        enemyX_change = 0.5
        enemyY = enemyY + enemyY_change
    
    if(collision(bulletX,bulletY,enemyX,enemyY)):
        bulletY = 480
        bullet_state = "ready"
        score = score + 1
        print(score)
        enemyX = random.randint(0,768)
        enemyY = random.randint(50, 150)
    
    
    enemy(enemyX, enemyY)
    pygame.display.update()


# In[ ]:




