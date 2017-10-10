import pygame
import sys
from pygame.locals import *
from Vconstants import *
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

pygame.display.set_caption('WINNER!')

clock = pygame.time.Clock()

vbros = pygame.image.load(path.join(img_dir,'vbros.png')).convert()
cap = pygame.image.load(path.join(img_dir,'capsunR2.png'))
frame_rate = 60

# create rotating image function

def winScreen():
    pygame.init()

    fontsize = 30
    font_change = 0

    titleFont = pygame.font.Font('freesansbold.ttf', 75)
    font_start = pygame.font.Font(None, fontsize)
    titleSurf = titleFont.render('!!WINNER!!', True, purple)
    # -- Attempt at growing text
    titleSurf2 = font_start.render('Success', True, blue)
    # - Hench 21 Image
    h21 = pygame.image.load(path.join(img_dir,'h21.png'))
    h21 = pygame.transform.scale(h21, [95, 135])

    # -- Captain Sunshine
    cap_x = -230
    cap_y = 5

    capx_change = 6
    #capy_change =


    degrees1 = 0
    degrees2 = 0

    while True:

        cap_x += capx_change
        if cap_x > 1015:
            cap_x = -210


        screen.blit(pygame.transform.scale(vbros, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0,0))
        screen.blit(cap, (cap_x, cap_y))
        # -- Adding Rotating Text
        rotatedSurf = pygame.transform.rotate(titleSurf, degrees1)
        rotatedRect = rotatedSurf.get_rect()
        rotatedRect.center = (SCREEN_WIDTH /2, SCREEN_HEIGHT / 2)
        screen.blit(rotatedSurf, rotatedRect)

        fontsize += font_change
        # - Other text
        #growSurf = pygame.transform.scale(titleSurf2, fontsize)
        growRect = titleSurf2.get_rect()
        growRect.topleft = (75, 200)
        #screen.blit(titleSurf2, growRect)

        #-- Add image
        rotate21 = pygame.transform.rotate(h21, degrees2)
        Rect21 = rotate21.get_rect()
        Rect21.center = (650, 500)
        screen.blit(rotate21, Rect21)

        #if checkForKeyPress():
            #pygame.event.get()
            #return
        pygame.display.update()
        clock.tick(frame_rate)
        degrees1 += 3
        degrees2 -= 4
        font_change += 3

        if fontsize > 75:
            font_change -= 3
        if fontsize < 30:
            font_change += 3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
