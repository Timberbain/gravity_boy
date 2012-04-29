import pygame
from ball import *

class Hero(Ball):

    def __init__(self, x, y, dx, dy, r=5, mag=1, color=(255,0,0), max_ax = 10):
        Ball.__init__(self, x, y, dx, dy, r, mag, color, surface = None)

        self.max_ax = max_ax