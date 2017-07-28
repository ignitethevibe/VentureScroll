# -- Levels
import pygame
from pygame.locals import *
from Vplatform import *
from Vplayer import *
from Vcoin import *
from Vconstants import *
from vscore import *
# -- Import Each Level so main program can run from
#import level_01, level_02, level_03, level_04, level_05, level_06

class Level():
    # This is a generic super-class to define a level
    # Create a child class for each level with level specific info

    def __init__(self, player, coin, score):
        # Constructor. Pass in a handle to player. Needed for when moving platforms
        # collide with the player

        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()

        # -- 7/27
        self.extra_list = pygame.sprite.Group()

        self.player = player

        self.coin = coin
        self.score = Score()
        # how far world has been scrolled
        self.world_shift = 0


    def update(self):
        self.platform_list.update()
        self.enemy_list.update()

        # -- 7/27
        self.extra_list.update()

        ## IT WORKED!!!!
        hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, True)
        for coin in hit_list:
            coin.kill()
            self.score.add()




    def draw(self, screen):

        # Draw Background
        screen.blit(hallway, (0,0))
        self.score.draw(screen)

        # Draw all sprite lists
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

        # -- 7/27
        self.extra_list.draw(screen)

    def shift_world(self, shift_x):

        # keep track of shift amount
        self.world_shift += shift_x

        # go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

        for extra in self.extra_list:
            extra.rect.x += shift_x


# create platforms for levels
class Level_01(Level):
                            # Add Coin variable
    def __init__(self, player, coin, score):

        # Call the parent Constructor
        Level.__init__(self, player, coin, score)

        self.level_limit = -1800

        # Array with wdith, height, x y of platform
        level = [[210, 70, 500, 500],
                [210, 70, 800, 400],
                [210, 70, 1000, 500],
                [210, 70, 1120, 280],
                [210, 40, 1325, 200],
                [100, 60, 1635, 150],
                [210, 50, 1850, 100],
                ]

        # go through array and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

            # Add Coins above platforms
        for coin in level:
            item = Coin()
            item.rect.x = coin[2]+40
            item.rect.y = coin[3]-75
            item.player = self.player
            self.enemy_list.add(item)

        # -- Needs Work
        #if player.rect.x == 1200:
        #h21 = Extras('h21.png', 48, 76)
        #h21.rect.x = 1255
        #h21.rect.y = 400
        #width_change = 6
        #height_change = 6
        #width_max = 100
        #height_max = 178
        #h21.level = self
        #self.extra_list.add(h21)

class Level_02(Level):

    def __init__(self, player, coin, score):


        # call parent constructor
        Level.__init__(self, player, coin, score)

        self.level_limit = -1500

        # array of platform (w,h), (x,y)
        level = [[210, 30, 450 ,570],
                [210, 30, 850, 420],
                [125, 45, 925, 150],
                [210, 30, 1110, 530],
                [210, 30, 1120, 280],
                [90, 45, 1425, 185],
                ]


        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for coin in level:
            item = Coin()
            item.rect.x = coin[2]+40
            item.rect.y = coin[3]-75
            item.player = self.player
            self.enemy_list.add(item)


        # -- Extras 7/27

        orph = MovingExtra('docOrph.png', 95, 150)
        orph.rect.x = 1550
        orph.rect.y = SCREEN_HEIGHT - 150
        orph.boundary_left = 1550
        orph.boundary_right = 1800
        orph.change_x = 2
        orph.level = self
        self.extra_list.add(orph)


class Level_03(Level):

    def __init__(self, player, coin, score):


        # call parent constructor
        Level.__init__(self, player, coin, score)

        self.level_limit = -1500

        # array of platform (w,h), (x,y)
        level = [[190, 30, 500 ,550],
                [195, 50, 820, 420],
                [200, 30, 1220, 410],
                [150, 40, 1100, 270],
                [210, 30, 1700, 220],
                ]


        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for coin in level:
            item = Coin()
            item.rect.x = coin[2]+40
            item.rect.y = coin[3]-75
            item.player = self.player
            self.enemy_list.add(item)

        # Add a custom moving platform
        block = MovingPlatform(70, 40)
        block.rect.x = 1350
        block.rect.y = 280
        block.boundary_left = 1350
        block.boundary_right = 1600
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


class Level_04(Level):

    def __init__(self, player, coin, score):


        # call parent constructor
        Level.__init__(self, player, coin, score)

        self.level_limit = -1400

        # array of platform (w,h), (x,y)
        level = [[210, 30, 450 ,570],
                [125, 30, 650, 420],
                [80, 30, 850, 350],
                [95, 30, 1000, 475],
                [150, 30, 1120, 245],
                [150, 40, 1300, 420],
                [175, 40, 1475, 200],
                ]


        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for coin in level:
            item = Coin()
            item.rect.x = coin[2]+40
            item.rect.y = coin[3]-75
            item.player = self.player
            self.enemy_list.add(item)


class Level_05(Level):

    def __init__(self, player, coin, score):


        # call parent constructor
        Level.__init__(self, player, coin, score)

        self.level_limit = -1500

        # array of platform (w,h), (x,y)
        level = [[210,400, 625, 300],
                [200, 40, 925, 300],
                [185, 250, 1250, 235],
                [175, 30, 1515, 190],
                [150, 20, 1760, 300],
                ]


        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for coin in level:
            item = Coin()
            item.rect.x = coin[2]+40
            item.rect.y = coin[3]-75
            item.player = self.player
            self.enemy_list.add(item)

        # Add a custom moving platform
        block = MovingPlatform(175, 35) # Add Width & Height
        block.rect.x = 450 # X-axis
        block.rect.y = 290 # Y-Axis
        block.boundary_bottom = 565 # Choose Boundries
        block.boundary_top = 290 # Choose End Boundry
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

class Level_06(Level):

    def __init__(self, player, coin, score):


        # call parent constructor
        Level.__init__(self, player, coin, score)

        self.level_limit = -2050

        # array of platform (w,h), (x,y)
        level = [[200, 50, 500, 525],
                [120, 75, 800, 375],
                [120, 75, 1000, 300],
                [100, 50, 1420, 145],
                [100, 100, 1540, 500],
                [100, 55, 1900, 145],
                [100, 50, 1850, 445],
                [100, 70, 2450, 310],
                ]


        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)

        for coin in level:
            item = Coin()
            item.rect.x = coin[2]+40
            item.rect.y = coin[3]-75
            item.player = self.player
            self.enemy_list.add(item)

        # Add a custom moving platform
        block = MovingPlatform(130, 35) # Add Width & Height
        block.rect.x = 1200 # X-axis
        block.rect.y = 285 # Y-Axis
        block.boundary_left = 1200 # Choose Boundries
        block.boundary_right = 1365 # Choose End Boundry
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving platform
        block = MovingPlatform(130, 35) # Add Width & Height
        block.rect.x = 1600 # X-axis
        block.rect.y = 285 # Y-Axis
        block.boundary_left = 1600 # Choose Boundries
        block.boundary_right = 1725 # Choose End Boundry
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        # Add a custom moving platform
        block = MovingPlatform(130, 35) # Add Width & Height
        block.rect.x = 2150 # X-axis
        block.rect.y = 220 # Y-Axis
        block.boundary_left = 2150 # Choose Boundries
        block.boundary_right = 2300 # Choose End Boundry
        block.boundary_bottom = 485
        block.boundary_top = 220
        block.change_x = 1
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
