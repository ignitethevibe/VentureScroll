import pygame
from pygame.locals import *
from Vconstants import *
from Vlevel import *
from Vplayer import *

# -- Class to add images to levels and option to animate

class Extras(pygame.sprite.Sprite):
    def __init__(self, image, width, height):
        super(Extras, self).__init__()

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, [width, height])

        self.rect = self.image.get_rect()


class MovingExtra(Extras):

        change_x = 0
        change_y = 0

        boundary_top= 0
        boundary_bottom = 0
        boundary_left = 0
        boundary_right = 0

        width_change = 0
        height_change = 0

        width_max = 0
        height_max = 0

        player = None

        level = None

        def update(self):

            # -- Move Left/Right
            self.rect.x += self.change_x

            # -- Move Up/Down
            self.rect.y += self.change_y

            # -- Needs Work
            # -- Size Change
            #self.width += self.width_change
            #self.height += self.height_change

            # Check the boundaries and see if we need to reverse
            if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
                self.change_y *= -1

            cur_pos = self.rect.x - self.level.world_shift
            if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
                self.change_x *= -1


                # --- Needs Work 
            # -- Size control-- Growing until Max Height
            #if self.width > self.width_max:
                #self.width_change = 0

            #if self.height > self.height_max:
                #self.height_change = 0
