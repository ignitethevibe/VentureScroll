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

    titleFont = pygame.font.Font('freesansbold.ttf', 90)
    titleSurf = titleFont.render('WINNER!!', True, purple)



    while True:

        screen.blit(pygame.transform.scale(vbros, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0,0))

        titleRect = titleSurf.get_rect()
        titleRect.topleft = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        screen.blit(titleSurf, titleRect)



        #if checkForKeyPress():
            #pygame.event.get()
            #return
        pygame.display.update()
        clock.tick(frame_rate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
