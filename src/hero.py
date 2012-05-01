import pygame
from ball import *
from gb_loader import *

class Hero(Ball):

    def __init__(self,(frame_width, frame_height), x, y, dx, dy, r=5, mag=1, color=(255,0,0), max_ax = 10):
        self.frame_height = frame_height
        self.frame_width = frame_width
        Ball.__init__(self, x, y, dx, dy, r, mag, color, surface = None)

        self.max_ax = max_ax
        self.image, self.rect = Loader.load_image('gravityboy_stand.png', -1)

    def move(self):
        if self.x < 0 or self.x + self.r*2 > self.frame_width:
            self.dx *= -1
        if self.y < 0 or self.y + self.r*2 > self.frame_height:
            self.dy *= -1

        self.x += self.dx
        self.y += self.dy
        
        self.rect.left = self.x
        self.rect.top = self.y