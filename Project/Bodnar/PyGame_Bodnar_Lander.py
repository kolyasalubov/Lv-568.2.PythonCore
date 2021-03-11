import math
import random

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('forrest2.jpg')

# Sound
mixer.music.load("Back1.mp3")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Lander")
icon = pygame.image.load('airplane.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('plan3.png')
playerX = 0
playerY = 0
playerX_change = 0
direction = "right"

# Enemy
enemyImg = []
enemyX = []
enemyY = []
num_of_enemies = 15

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('monkey2.png'))
    enemyX.append(random.randint(0, 650))
    enemyY.append(random.randint(150, 580))

# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('bomb1.png')
bulletX = playerX
bulletY = playerY
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Win Game
win_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 163, 26))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 153, 204))
    screen.blit(over_text, (200, 250))

def win_game_text():
    over_text = win_font.render("YOU WIN", True, (255, 51, 51))
    screen.blit(over_text, (250, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 34, y + 34))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 32:
        return True
    else:
        return False
def isCollision1(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt(math.pow(enemyX - playerX, 2) + (math.pow(enemyY - playerY, 2)))
    if distance < 32:
        return True
    else:
        return False

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("Laser1.mp3")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
    
    if direction == "right":
        playerX += 1
        if playerX >= 780:
            if playerY + 20 >= 580:
                direction = "win"
                win_game_text()
            else:
                playerY += 20
                playerX = 0
    if direction == "stop":
          playerX = 330
          playerY = 300
          game_over_text()
    if direction == "win":
          playerX = 330
          playerY = 300
          win_game_text()

    # Enemy 
    for i in range(num_of_enemies):

        # Collisions
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("expl1.mp3")
            explosionSound.play()
            bulletX = -10
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = 1000
            enemyY[i] = 1000

        collision1 = isCollision1(enemyX[i], enemyY[i], playerX, playerY)
        if collision1:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            
            for j in range(num_of_enemies):
                enemyY[j] = 2000
                direction = "stop"
                game_over_text()
            break    
        
        enemy(enemyX[i], enemyY[i], i)
    
    if bulletY > 580:
        bulletY = playerY
        bulletX = playerX
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY += bulletY_change

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
