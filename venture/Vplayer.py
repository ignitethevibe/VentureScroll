# - Player
import pygame
from pygame.locals import *
from Vconstants import *
from os import path

img_dir = path.join(path.dirname(__file__), 'img')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load(path.join(img_dir, 'helperR.png'))
        self.image = pygame.transform.scale(self.image, (65, 95))
        self.rect = self.image.get_rect()

        # Set vector speed
        self.change_x = 0
        self.change_y = 0

        self.level = None

    def update(self):
        # Move Player

        # Gravity
        self.calc_grav()

        # move left/right
        self.rect.x += self.change_x

        # see if we hit anything x-axis
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # set side to opposite side of obj hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        # move up/down
        self.rect.y += self.change_y

        #check to see if hit anything y-axis
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset position based on the top/bottom of the obj
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # stop vertical movement
            self.change_y = 0

        #self.itemsCollision(items)
        #self.render()



    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # check if on ground
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def jump(self):
        # check if there is platform
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it's ok to jump, set speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10


    # Player Movements
    def go_left(self):
        # called w/ LEFT arrow
        self.change_x = -6

    def go_right(self):
        # right arrow
        self.change_x = 6

    def stop(self):
        self.change_x = 0

    # Collision Detection
    def itemsCollision(self, coin):
        if pygame.sprite.collide_rect(self, enemy_list) == True:
            item.kill()
