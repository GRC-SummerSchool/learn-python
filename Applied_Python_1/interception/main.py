import pygame
from function import f1, f2, f3, f4, display_w, display_h
import numpy as np
import sys


intercept = np.load('stieber_scenario_4.npy')
#intercept = intercept * 2


#intercept = None
img_w = 10
img_h = 10
no_of_crumbs = 50

x = np.linspace(0,display_w-350,no_of_crumbs)
y_s = [f1(x), f2(x), f3(x), f4(x)]

if len(sys.argv) > 1:
    y = y_s[int(sys.argv[1])]
else:
    y = y_s[0]

black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption('Interception')
clock = pygame.time.Clock()
gameExit = False
house_img = pygame.image.load('house.jpg')
hansel_gretel_img = pygame.image.load('h_g.jpg')
witch_img = pygame.image.load('game_over.jpg')
hero_img = pygame.image.load('hero.jpg')
winner_img = pygame.image.load('winner.jpg')

def reset_screen():
    gameDisplay.fill(white)
    witches_house(x[no_of_crumbs - 1], y[no_of_crumbs - 1])
    return 0

def breadcrumb(x, y):
    pygame.draw.circle(gameDisplay,black,(int(x),int(y)),3,0)

def witches_house(x, y):
    gameDisplay.blit(house_img, (x + 100,y - 150))

def hansel_gretel(x, y):
    gameDisplay.blit(hansel_gretel_img, (x,y))

def hero(x, y):
    gameDisplay.blit(hero_img, (x, y))

def win(i, x, y):
    gameDisplay.fill(white)
    gameDisplay.blit(winner_img, (x, y))
    return i - 1

def game_over():
    gameDisplay.fill(black)
    gameDisplay.blit(witch_img, (display_w / 2 - 275, display_h / 2 - 250))

gameDisplay.fill(white)

i = reset_screen()
while not gameExit:
    reset_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    if i >= no_of_crumbs:
        #i = reset_screen()
        game_over()

    elif i >= no_of_crumbs + 50:
        i = reset_screen()

    elif i <= no_of_crumbs:
        hansel_gretel(x[i], y[i])
        h_g_collider = pygame.Rect(x[i], y[i], 50, 50)

        if type(intercept) != type(None):
            if i <= no_of_crumbs // 4:
                hold = 2 * i + 10
                hero(x[hold], intercept[hold])
                hero_collider = pygame.Rect(x[hold], intercept[hold], 50, 50)

            else:
                hero(x[hold], intercept[hold])
                hero_collider = pygame.Rect(x[hold], intercept[hold], 50, 50)

        for n in range(i - 1):
            breadcrumb(x[n], y[n])

        if h_g_collider.colliderect(hero_collider):
            i = win(i, 200, 200)

    i += 1

    pygame.time.wait(500)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()

