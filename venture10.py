# -- main program
import pygame
from pygame.locals import *
import random
import sys
from Vplayer import *
from Vplatform import *
from Vlevel import *
from Vcoin import *
from vscore import *
from game_over import *
from win_screen import *
from Vextras import *
#import level_01, level_02, level_03, level_04, level_05, level_06


## This Version I'd like to:
# Score increased with coins collected




SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
frame_rate = 60


# -- colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
purple = (255,0,255)

# -- Images
#brock = pygame.image.load('brock.png')
#doc = pygame.image.load('doc.png')
dean = pygame.image.load('dean.png')
hank = pygame.image.load('hank.png')
helperR = pygame.image.load('helperR.png')
helperL = pygame.image.load('helperL.png')
hench = pygame.image.load('hench2.png')
#loadzone = pygame.image.load('loadzone.png')
nightzone = pygame.image.load('nightzone.png')
coinImg = 'vlogo.png'
vbstart = pygame.image.load('vbstart.png')
guild = pygame.image.load('guild.png')
#sadhench = pygame.image.load('sadhench.png')
#tmsile = pygame.image.load('tsmile.png')
#vbros = pygame.image.load('vbros.png')
hallway = pygame.image.load('hallway.png')

# init Player
player = Player()
# Sprite Groups
active_sprite_list = pygame.sprite.Group()
coin_collected = pygame.sprite.Group()

#score = 0

player.rect.x = 340
player.rect.y = SCREEN_HEIGHT - player.rect.height
active_sprite_list.add(player)




def main():
    global screen, font, clock
    # -- Main Program ----

    pygame.init()

    # Set the screen dimensions
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Helper's Venture")

    clock = pygame.time.Clock()

    font = pygame.font.Font('freesansbold.ttf', 25)



    while True:
        StartScreen()
        runGame()


    # -- Main Program Loop ---
def runGame():
    # create player


    coin_list = pygame.sprite.Group()
    coin = Coin()
    coin_list.add(coin)
    score = Score()

    # create levels include Coin variable
    level_list = []
    level_list.append(Level_01(player, coin, score))
    level_list.append(Level_02(player, coin, score))
    level_list.append(Level_03(player, coin, score))
    level_list.append(Level_04(player, coin, score))
    level_list.append(Level_05(player, coin, score))
    level_list.append(Level_06(player, coin, score))
    level_list.append(Level_07(player, coin, score))
    level_list.append(Level_08(player, coin, score))

    # set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
    player.level = current_level



     #-- Timer Display Setup
    frame_count = 0

    start_time = 120


    # loop until the user clicks the close button
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()





            # update the player
        active_sprite_list.update()

            #update items in the level
        current_level.update()
        #coin_list.update()



            # If the player gets near the right side, shift world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)

            # if player gets near left side, shift world right (+x)
        if player.rect.left <= 120:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)

            # If player gets to end of level, go to next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # -- Win Screen once player reaches end
        if current_level_no > len(level_list)-2:
            done = True
            winScreen()

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)



        # --- Timer going up ---
        # Calculate total seconds
        #total_seconds = frame_count // frame_rate

        #Calculate for Going Down ---
        total_seconds = start_time - (frame_count // frame_rate)
        if total_seconds < 0:
            total_seconds = 0

        # Divide by 60 to get total minutes
        minutes = total_seconds // 60

        # use remainder to get seconds
        seconds = total_seconds % 60

        # Python string formatting to format into leading zeros
        output_string = "Time Remaining: {0:02}:{1:02}".format(minutes, seconds)

        #blit to screen
        text_time = font.render(output_string, True, red)
        screen.blit(text_time, [15, 5])
        # -------------------Timer-----------
            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        frame_count += 1
            # limit to 60 frames per second
        clock.tick(frame_rate)

            # update screen
        pygame.display.flip()

        if total_seconds == 0:
            done = True
            gameOver()


    # to avoid exit errors
    pygame.quit()

def StartScreen():

    titleFont = pygame.font.Font('freesansbold.ttf', 85)
    titleSurf1 = titleFont.render('Venture', True, green)
    titleSurf2 = titleFont.render('SideScroll', True, blue)

    # car start and move
    vb_x = 5
    vb_y = 25

    vbx_change = 4
    vby_change = 4
    while True:

        vb_x += vbx_change
        vb_y += vby_change

        # car loop around
        if vb_y > 450 or vb_y < 0:
            vby_change = vby_change * -1
        if vb_x > 600 or vb_x < 0:
            vbx_change = vbx_change * -1


        screen.blit(pygame.transform.scale(vbstart, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0,0))

        titleRect1 = titleSurf1.get_rect()
        titleRect1.topleft = (SCREEN_WIDTH - 575, SCREEN_HEIGHT - 600)
        screen.blit(titleSurf1, titleRect1)

        titleRect2 = titleSurf2.get_rect()
        titleRect2.topleft = (SCREEN_WIDTH - 625, SCREEN_HEIGHT - 500)
        screen.blit(titleSurf2, titleRect2)

        screen.blit(hench, [vb_x, vb_y])

        drawPressKeyMsg(SCREEN_WIDTH, SCREEN_HEIGHT)

        if checkForKeyPress():
            pygame.event.get()
            return
        pygame.display.update()
        clock.tick(frame_rate)
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

if __name__ == '__main__':
    main()
