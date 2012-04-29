import pygame
from hero import *
from gb_space import *
import random

class gb_model():


    def __init__(self):
        
        self.frame_width = 800#640
        self.frame_height = 600#480
        self.keydown = False
        self.keyup = False
        self.keyleft = False
        self.keyright = False
        self.villans = []
        self.hero = None

        self.villan_prob = 0.001                #probability that a villan will spawn each frame
        self.level = 1

    def generate_villan(self, diff=1):
        """ Create a villan, default difficulty is 1(easy)
        """
        vrad = 10
        v_dx = 3
        v_dy = 3
        v_mag = 5
        v_color = (255,0,0)
        
        villan = Ball(random.random()*(self.frame_width-vrad*diff), -vrad, 
                          random.random()*v_dx*diff - v_dx/2, random.random()*v_dy*diff+1, 
                          vrad*diff, v_mag*diff, v_color)
        self.villans.append(villan)
    
    def roll_for_villan(self):
        """Check to see if there will spawn any villans
        """
        if random.random() < self.villan_prob:
            self.generate_villan()

    def set_hero(self):
        """ Creates the hero with default values
        """
        self.hero = Hero(self.frame_width/2, self.frame_height/2, 0, 0, 15, 1, (0,255,0))

    def set_background(self):
        """ Creates the background
        """
        self.background = Gb_space(self.frame_width, self.frame_height)

    def update_model(self):
        """The big update
        """
        self.background.update_stars()
        self.background.draw_surface()
        self.update_hero_movement()
        self.update_villan_movement()
        self.roll_for_villan()
        self.villan_prob += 0.00005

    def update_villan_movement(self):
        """updates the movement and check for collision of all villans
        """
        for v in self.villans:
            for v2 in self.villans:
                if v != v2:
                    if self.check_collision(v,v2):
                        self.collision(v,v2)

            v.x += v.dx
            v.y += v.dy

            if v.y > self.frame_height or v.y < -v.r*2 or v.x > self.frame_width or v.x < -v.r*2:
                self.villans.remove(v)


    def update_hero_movement(self):
        """updates the position of the hero
        """
        for v in self.villans:
            if self.check_collision(self.hero, v):
                self.collision(self.hero, v)


        if self.keyup:
            if self.hero.dy > -self.hero.max_ax:
                self.hero.dy -= 0.5
        if self.keydown:
            if self.hero.dy < self.hero.max_ax:
                self.hero.dy += 0.5
        if self.keyright:
            if self.hero.dx < self.hero.max_ax:
                self.hero.dx += 0.5
        if self.keyleft: 
            if self.hero.dx > -self.hero.max_ax:
                self.hero.dx -= 0.5

        if self.hero.x < 0 or self.hero.x + self.hero.r*2 > self.frame_width:
            self.hero.dx *= -1
        if self.hero.y < 0 or self.hero.y + self.hero.r*2 > self.frame_height:
            self.hero.dy *= -1

        self.hero.x += self.hero.dx
        self.hero.y += self.hero.dy                

    def check_collision(self, a, b):
        """ Check if there has been any collision between object a and b
        """
        distance = math.sqrt(math.pow((a.x+a.r + a.dx) - (b.x+b.r + b.dx),2) +
								math.pow((a.y+a.r + a.dy)-(b.y+b.r + b.dx),2))
        if distance <= (b.r + a.r):
            return True

    def collision(self, a, b):
        """Calculates the new velocity for both object a and b
        """
        kata = a.y - b.y
        katb = a.x - b.x
        hippo = math.sqrt(kata*kata + katb*katb)
        angle = math.asin(kata/hippo)

        ux = a.dx*math.cos(-angle) - a.dy*math.sin(-angle)
        uy = a.dx*math.sin(-angle) + a.dy*math.cos(-angle)

        bux = b.dx*math.cos(-angle) - b.dy*math.sin(-angle)
        buy = b.dx*math.sin(-angle) + b.dy*math.cos(-angle)

        aux =  (ux*(a.mag-b.mag)+2*b.mag*bux)/(a.mag+b.mag)
        abux = (bux*(b.mag-a.mag)+2*a.mag*ux)/(b.mag+a.mag)
        b.dx = abux*math.cos(angle) - buy*math.sin(angle)
        b.dy = abux*math.sin(angle) + buy*math.cos(angle)

        a.dx = aux*math.cos(angle) - uy*math.sin(angle)
        a.dy = aux*math.sin(angle) + uy*math.cos(angle)