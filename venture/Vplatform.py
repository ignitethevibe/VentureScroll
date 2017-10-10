# Platforms
import pygame
from pygame.locals import *
from Vconstants import *
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

# -- Creating platform the user can jump on
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height):

        super(Platform, self).__init__()

        self.image = pygame.image.load(path.join(img_dir,'tsmile.png')).convert()
        self.image = pygame.transform.scale(self.image, [width, height])


        self.rect = self.image.get_rect()

# --- Fancier platform that can actually move
class MovingPlatform(Platform):

    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    player = None

    level = None

    def update(self):

        # Move left/right
        self.rect.x += self.change_x

        # see if we hit player
        hit = pygame.sprite.collide_rect(self,self.player)
        if hit:
            # Player hit by platform
            # send them flying in opposite direction
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right


        # move up/down
        self.rect.y += self.change_y

        # check and see if hit player top/bottom
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
