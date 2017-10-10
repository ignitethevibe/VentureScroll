# -- Coin
import pygame
from pygame.locals import *
from venture10 import *
from Vlevel import *
from Vconstants import *





class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super(Coin, self).__init__()

        #self.image = pygame.Surface([width, height])
        self.image = coinImg
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()


    def update(self):
        pass
