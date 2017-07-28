# -- Game Over Screen
import sys
import pygame
from pygame.locals import *
from Vconstants import *


# Set the screen dimensions
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Helper's Venture")

clock = pygame.time.Clock()

zoneImg = pygame.image.load('loadzone.png')
spidey = pygame.image.load('spidey.png')
sadhench = pygame.image.load('sadhench.png')
bathank = pygame.image.load('bathank.png')


def gameOver():
    pygame.init()

    overfont = pygame.font.Font('freesansbold.ttf', 65, owidth=10, ocolor=black)
    overText1 = overfont.render('T.H.E', True, blue)
    overText2 = overfont.render('E.N.D', True, blue )

    # ----Spidey
    spidey_x = 340
    spidey_y = -250

    spideyy_change = 2

    # --- BatHanks
    bhank1_x = 150
    bhank2_x = 475
    bhank_y = -125

    bhanky_change = 5

    # ---Text
    overRect1_x = 10
    overRect1_y = 250

    overRect2_x = 670
    overRect2_y = 250

    overRect1x_change = 5
    overRect2x_change = -5




    while True:

        overRect1_x += overRect1x_change
        overRect2_x += overRect2x_change

        if overRect1_x > 300 or overRect1_x < 0:
            overRect1x_change = overRect1x_change * -1
        if overRect2_x > 670 or overRect2_x < 400:
            overRect2x_change = overRect2x_change * -1

        # Spidey Animation
        spidey_y += spideyy_change

        if spidey_y > -10 or spidey_y < -255:
            spideyy_change = spideyy_change * -1

        # -- BatHanks Animation
        bhank_y += bhanky_change

        if bhank_y > 601:
            bhank_y = -125

        # Add BG
        screen.blit(pygame.transform.scale(sadhench, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0,0))

        overRect1 = overText1.get_rect()
        overRect1.topleft = (overRect1_x, overRect1_y)


        overRect2 = overText2.get_rect()
        overRect2.topleft = (overRect2_x, overRect2_y)

        screen.blit(overText1, overRect1)
        screen.blit(overText2, overRect2)
        screen.blit(spidey, [spidey_x, spidey_y])
        screen.blit(bathank, [bhank1_x, bhank_y])
        screen.blit(bathank, [bhank2_x, bhank_y])

        clock.tick(60)

        pygame.display.flip()

        #overRect1x_change = 5
        #overRect2x_change = 5


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def drawPressKeyMsg(SCREEN_WIDTH, SCREEN_HEIGHT): # Displays 'Press a Key' in bottom center of screen
    pressKeySurf = font.render('Press a Key', True, red)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 30)
    screen.blit(pressKeySurf, pressKeyRect)

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        pygame.quit()
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        pygame.quit()
    return keyUpEvents[0].key

def terminate():
    pygame.quit()
    sys.exit()
