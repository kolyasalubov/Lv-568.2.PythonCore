import pygame
import random
import math
from pygame import mixer
import kanji_data_prosess as kanji
import sys
from pygame.locals import *

####################
#   MAIN SETTINGS  #
####################

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (214, 0, 55)

# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# This sets the name of the window
pygame.display.set_caption('Catch Kanji!')
 
clock = pygame.time.Clock()

#set custom icon for our game
#Icon made by Freepik from www.flaticon.com
icon = pygame.image.load(r"onigiri_icon.png")
pygame.display.set_icon(icon)
font = pygame.font.Font(r"NightinTokyo.ttf", 32)
font1 = pygame.font.Font(r"NotoSerifJP-Bold.otf", 40)
#обновляємо екран 
pygame.display.update()
 
# Set positions of graphics

background_position = [0, 0]
background1 = pygame.image.load(r"back_2.jpg")

background_position = [0, 0]
background2 = pygame.image.load(r"back_1.jpg")


mixer.music.load(r"RUDE-Eternal-Youth.mp3")
mixer.music.play(-1)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


#################
#   MAIN LOOPS  #
#################
 
def main_menu():
    while True:
        
        screen.blit(background2, (0, 0))
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(300, 100, 200, 50)
        button_2 = pygame.Rect(300, 160, 200, 50)
        button_3 = pygame.Rect(300, 220, 200, 50)
        button_4 = pygame.Rect(300, 280, 200, 50)
        button_5 = pygame.Rect(300, 340, 200, 50)
        button_6 = pygame.Rect(300, 400, 200, 50)
        button_7 = pygame.Rect(300, 460, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game(1)
        if button_2.collidepoint((mx, my)):
            if click:
                game(2)
        if button_3.collidepoint((mx, my)):
            if click:
                game(3)
        if button_4.collidepoint((mx, my)):
            if click:
                game(4)
        if button_5.collidepoint((mx, my)):
            if click:
                game(5)
        if button_6.collidepoint((mx, my)):
            if click:
                game(6)
        if button_7.collidepoint((mx, my)):
            if click:
                game(7)
        pygame.draw.rect(screen, (PINK), button_1)
        pygame.draw.rect(screen, (PINK), button_2)
        pygame.draw.rect(screen, (PINK), button_3)
        pygame.draw.rect(screen, (PINK), button_4)
        pygame.draw.rect(screen, (PINK), button_5)
        pygame.draw.rect(screen, (PINK), button_6)
        pygame.draw.rect(screen, (PINK), button_7)
        draw_text('main menu', font, PINK, screen, 323, 30)
        draw_text('level 1', font, WHITE, screen, 347, 110)
        draw_text('level 2', font, WHITE, screen, 347, 170)
        draw_text('level 3', font, WHITE, screen, 347, 230)
        draw_text('level 4', font, WHITE, screen, 347, 290)
        draw_text('level 5', font, WHITE, screen, 347, 350)
        draw_text('level 6', font, WHITE, screen, 347, 410)
        draw_text('level 7', font, WHITE, screen, 347, 470)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        clock.tick(60)
 
def game(level):
    player_image = pygame.image.load(r"bowl_fly.png").convert()
    play_x = 370
    play_y = 530
    palyer_step = 8
    #Якщо в зображення не має прозорого слою, то щоб його встановити,
    #необхідно використати метод set_colorkey() класу Surface:
    player_image.set_colorkey(BLACK)
    

    #playing function, copy image on screen

    def player(x, y):
        screen.blit(player_image, (x, y))

    #falling stuff
    falling_image = []
    catch_x = []
    catch_y = []
    num_of_falling = 5



    for i in range(num_of_falling):
        res = key = random.choice(list(kanji.getting_kanji(level).keys())) 
        falling_image.append(font1.render(res, True, PINK ))
        #falling_image[i].set_colorkey(WHITE)
        rand_posit = 0
        rand_posit = random.randint(0, 736)
        catch_x.append(rand_posit)
        catch_y.append(-50)

    def fall_catch(x, y, i):
        screen.blit(falling_image[i], (x, y))

    def is_caught(fall_x, fall_y, caugher_x, caughter_y):
        distance = math.sqrt((math.pow(caugher_x-fall_x,2)) + (math.pow(caughter_y-fall_y,2)))
        if distance < 50:
            return True
        else:
            return False

    #score
    score_value = 0

    scoreX = 10 
    scoreY = 10
    def show_score (x, y, score_value):
        score = font.render('Score: ' + str(score_value), True, PINK)
        screen.blit(score, (x, y))

    failed_value = 0
    failedX = 10
    failedY = 40
    def show_failed (x, y, failed_value):
        score = font.render('Failed: ' + str(failed_value), True, PINK)
        screen.blit(score, (x, y))

    ##################################################################################################
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False           
    
        #screen.fill(0,0,0)
        screen.blit(background1, (0, 0))
        # Get the current mouse position. This returns the position 
        # as a list of two numbers.
        #повертає поточну позицію мишки на екрані
        
        player(play_x, play_y)

        for i in range(num_of_falling):
            if catch_y[i]<650 and catch_y[i]!=650:
                catch_y[i]+=5
            else:
                catch_y[i]=0
                catch_x[i] = random.randint(0, 736)
                failed_value+=1

            #caughting process
            collision = is_caught(catch_x[i], catch_y[i], play_x, play_y)
            if collision==True:
                nya = mixer.Sound(r"nya.wav")
                nya.play()
                score_value+=1
                catch_y[i]=0
                catch_x[i] = random.randint(0, 736)
                
            fall_catch(catch_x[i], catch_y[i], i)

        show_failed(failedX, failedY, failed_value)

        keys=pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and play_x>palyer_step:
            play_x-=palyer_step
        if keys[pygame.K_a] and play_x>palyer_step:
            play_x-=palyer_step
        if keys[pygame.K_RIGHT] and play_x<800-64-palyer_step:
            play_x+=palyer_step
        if keys[pygame.K_d] and play_x<800-64-palyer_step:
            play_x+=palyer_step




        player(play_x, play_y)

        show_score(scoreX, scoreY, score_value)   
    
        #обновляємо екран
        pygame.display.flip()
    
        clock.tick(60)

click = False
main_menu()