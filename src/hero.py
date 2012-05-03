import pygame
from ball import *

class Hero(Ball):

    def __init__(self,(frame_width, frame_height), x, y, dx, dy, r=5, mag=1, color=(255,0,0), max_ax = 10):

        Ball.__init__(self,(frame_width, frame_height), x, y, dx, dy, r, mag, color, surface = None)

        self.max_ax = max_ax
        self.image, self.rect = Loader.load_image('anime','gravityboy_stand.png', -1)
        #self.nranimation = [(Direction.NONE, 1), (Direction.UP, 10), (Direction.RIGHT, 10), (Direction.DOWN, 10), (Direction.LEFT, 10)]
        self.nranimation = [(Direction.RIGHT, 10)]
        self.animatrix = {}
        self.load_animations()

    def load_animations(self):
        suffix = '.png'
        directory = 'anime'
        for d, n in self.nranimation:
            for i in range(n):
                filename = 'hero_' + str(d) + '_' + str(i) + suffix
                print filename
                anim, rect = Loader.load_image(directory, filename, -1)
                if not self.animatrix.has_key(d):
                    self.animatrix[d] = []
                self.animatrix[d].append((anim, rect))




    def update(self):
        t_image, t_rect = self.animatrix[Direction.RIGHT].pop(0)
        self.animatrix[Direction.RIGHT].append((t_image, t_rect))
        self.image = t_image
        #self.rect = t_rect
        #print self.animatrix[Direction.RIGHT]

        #if self.rect.w <> self.r*2 or self.rect.h <> self.r*2:
        self.rect.w = self.r*2
        self.rect.h = self.r*2
        self.image = pygame.transform.scale(self.image, (self.r*2, self.r*2))
        
    def move(self):
        if self.x - self.r < 0 or self.x + self.r > self.frame_width:
            self.dx *= -1
        if self.y - self.r < 0 or self.y + self.r > self.frame_height:
            self.dy *= -1

        self.x += self.dx
        self.y += self.dy
        
        self.rect.left = self.x-self.r
        self.rect.top = self.y-self.r