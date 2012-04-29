import pygame
import random
import math

class Gb_space():

    def __init__(self, width, height, color=(0,0,0), surface = None):
        self.w = width
        self.h = height
        self.surface = surface
        self.color = color

        self.speed = 5

        self.star_number = 50
        self.stars = []
        self.generate_stars()
        if self.surface == None:
            self.__create_surface()


    def __create_surface(self):
        self.surface = pygame.Surface((self.w,self.h)).convert()
        self.draw_surface()

    def generate_stars(self):
        """ fills the list 'stars' with star objects
        """
        for n in range(self.star_number):
            star_x = random.random()*self.w
            star_y = random.random()*self.h
            speed = random.random()*self.speed + 1
            star = _Star(star_x, star_y, speed)
            self.stars.append(star)
    
    def update_stars(self):
        """ Updates the stars position
        """
        for n in self.stars: 
            n.y += n.speed
            if n.y > self.h:
                n.x = random.random()*self.w
                n.y = 0

    def draw_surface(self):
        """ update the background surface
        """
        self.surface.fill((self.color))

        for n in self.stars:
            self.surface.set_at((int(math.ceil(n.x)), int(math.ceil(n.y))), (255,255,255))

class _Star():
    """ Private class that represent a star
    """

    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed