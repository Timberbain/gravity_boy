from pygame import *
from ball import *

class Villan(Ball):

    def __init__(self,(frame_width, frame_height), x, y, dx, dy, r=5, mag=1, color=(255,0,0), surface = None):
        Ball.__init__(self,(frame_width, frame_height), x, y, dx, dy, r, mag, color, surface = None)

        self.image, self.rect = Loader.load_image('anime','villan.png', -1)

    def update(self):
        self.rect.left = self.x-self.r
        self.rect.top = self.y-self.r