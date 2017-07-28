# -- Coin
import pygame
from pygame.locals import *
from venture10 import *
from Vlevel import *



class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super(Coin, self).__init__()

        #self.image = pygame.Surface([width, height])
        self.image = pygame.image.load('vlogo.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        #coin_list = pygame.sprite.Group()

        #coin_list.add(self)
    def update(self):
        pass
        #coin_list.update()
