import pygame
from ball import *
from hero import *
from gb_model import *
from gb_space import *


class Gb_view():

    def __init__(self, model):
        
        self.model = model
        self.screen = pygame.display.set_mode((self.model.frame_width, 
                                               self.model.frame_height))

    def draw(self):
        self.screen.blit(self.model.background.surface, (0,0))

        self.model.gameobjects.draw(self.screen)
        self.screen.set_at((int(self.model.hero.x), int(self.model.hero.y)), (255,255,255))
        self.screen.blit(self.model.hero.surface, (self.model.hero.x-self.model.hero.r
                                           , self.model.hero.y-self.model.hero.r))
        #for v in self.model.villans:
        #    self.screen.blit(v.surface, (v.x-v.r, v.y-v.r))
        #    self.screen.set_at((int(v.x), int(v.y)), (255,255,255))

        pygame.display.flip()