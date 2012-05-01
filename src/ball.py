import pygame

class Ball():

    def __init__(self, x, y, dx, dy, r=5, mag=1, color=(255,0,0), surface = None):
        
        self.surface = surface
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.mag = mag
        self.color = color
        self.colliding = False

        if self.surface == None:
            self.__create_surface()


    def __create_surface(self):
        """ Create a surface for the ball
        """
        self.surface = pygame.Surface((self.r*2,self.r*2)).convert()
        self.surface.set_colorkey((0,0,0))
        pygame.draw.circle(self.surface, self.color, (self.r,self.r), self.r)