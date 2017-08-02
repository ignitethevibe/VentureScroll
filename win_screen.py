import pygame
import sys
from pygame.locals import *
from Vconstants import *



size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

pygame.display.set_caption('WINNER!')

clock = pygame.time.Clock()

vbros = pygame.image.load('vbros.png')
frame_rate = 60

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
    h21 = pygame.image.load('h21.png')
    h21 = pygame.transform.scale(h21, [95, 135])

    degrees1 = 0
    degrees2 = 0

    while True:

        screen.blit(pygame.transform.scale(vbros, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0,0))

        # -- Adding Rotating Text
        rotatedSurf = pygame.transform.rotate(titleSurf, degrees1)
        rotatedRect = rotatedSurf.get_rect()
        rotatedRect.topleft = (200, SCREEN_HEIGHT / 2)
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
        Rect21.topleft = (300, 120)
        screen.blit(rotate21, Rect21)

        #if checkForKeyPress():
            #pygame.event.get()
            #return
        pygame.display.update()
        clock.tick(frame_rate)
        degrees1 += 3
        degrees2 += 7
        font_change += 3

        if fontsize > 75:
            font_change -= 3
        if fontsize < 30:
            font_change += 3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
