import pygame
from pygame.locals import *
import random
import sys
from Vplayer import *
from Vplatform import *
from Vlevel import *
from Vcoin import *



class Score():

    def __init__(self):


        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 25)

    def draw(self, screen):
        scoretext = self.font.render('Score = '+str(self.score),1,(purple))
        screen.blit(scoretext, (650,5))

    def add(self):
        self.score += 1

    def val(self):
        return self.score
