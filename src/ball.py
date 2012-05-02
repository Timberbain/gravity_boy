from pygame import *
from enum import *

class Ball(sprite.Sprite):

    def __init__(self,(frame_width, frame_height), x, y, dx, dy, r=5, mag=1, color=(255,0,0), surface = None):
        sprite.Sprite.__init__(self)
        
        self.surface = surface
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.mag = mag
        self.color = color
        self.colliding = False
        self.frame_height = frame_height
        self.frame_width = frame_width

        self.image = None
        self.rect = None

        self.direction = Direction.NONE

        if self.surface == None:
            self.__create_surface()



    def __create_surface(self):
        """ Create a surface for the ball
        """
        self.surface = Surface((self.r*2,self.r*2)).convert()
        self.surface.set_colorkey((0,0,0))
        draw.circle(self.surface, self.color, (self.r,self.r), self.r)