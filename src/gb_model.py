import pygame
from hero import *
from villan import *
from gb_space import *
import random

class Gb_model():


    def __init__(self, frame_width, frame_height):
        
        self.frame_width = frame_width#800#640
        self.frame_height = frame_height#600#480
        self.keydown = False
        self.keyup = False
        self.keyleft = False
        self.keyright = False
        self.villans = []
        self.hero = None
        self.gameobjects = pygame.sprite.RenderPlain()
        self.in_collision = []

        self.villan_prob = 0.001                #probability that a villan will spawn each frame
        self.level = 1

    def generate_villan(self, diff=1):
        """ Create a villan, default difficulty is 1(easy)
        """
        vrad = 10
        v_dx = 3.0
        v_dy = 3.0
        v_mag = 5
        v_color = (255,0,0)
        
        villan = Villan((self.frame_width, self.frame_height), random.random()*(self.frame_width-vrad*diff), -vrad, 
                          random.random()*v_dx*diff - v_dx/2, random.random()*v_dy*diff+1, 
                          vrad*diff, v_mag*diff, v_color)
        self.villans.append(villan)
        self.gameobjects.add(villan)
    
    def roll_for_villan(self):
        """Check to see if there will spawn any villans
        """
        if random.random() < self.villan_prob:
            self.generate_villan()

    def set_hero(self):
        """ Creates the hero with default values
        """
        self.hero = Hero((self.frame_width, self.frame_height),self.frame_width/2, self.frame_height/2, 0.0, 0.0, 15, 1, (0,255,0))
        self.gameobjects.add(self.hero)

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
        self.gameobjects.update()




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
            if v.dy < 3:
                v.dy += 0.1

            if v.y+v.r > self.frame_height or v.y - v.r < -v.r*2 or v.x + v.r > self.frame_width or v.x - v.r < -v.r*2:
                self.villans.remove(v)
                self.gameobjects.remove(v)


    def update_hero_movement(self):
        """updates the position of the hero
        """
        for v in self.villans:
            if self.check_collision(self.hero, v):
                if self.in_collision.count((self.hero, v)) == 0:
                    self.collision(self.hero, v)
                    self.in_collision.append((self.hero, v))
                    print 'collision'
                    #self.hero.r +=1
            elif self.in_collision.count((self.hero, v)) > 0:
                self.in_collision.remove((self.hero, v))


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

        self.hero.move()
             

    def check_collision(self, a, b):
        """ Check if there has been any collision between object a and b
        """

        #dis_x = abs((a.x+a.r + a.dx)-(b.x+b.r + b.dx))
        #dis_y = abs((a.y+a.r + a.dy)-(b.y+b.r + b.dy))
        #dis_x = a.x - b.x
        #dis_y = a.y - b.y
        #distance = dis_x*dis_x + dis_y*dis_y

        #min_distance = (b.r + a.r)

        #if distance <= min_distance * min_distance:

        #    return True

        #distance = math.sqrt(math.pow((a.x + a.dx) - (b.x + b.dx),2) + 
        #                     math.pow((a.y + a.dy)-(b.y + b.dx),2))
        #if distance < (b.r + a.r):
        #    return True
        return sprite.collide_circle(a,b)


    def collision(self, a, b):
        """Calculates the new velocity for both object a and b
        """
        kata = a.y - b.y
        katb = a.x - b.x
        print kata,katb


        hippo = math.sqrt(kata*kata + katb*katb)
        angle = math.asin(kata/hippo)
        
        #print angle

        ux = a.dx*math.cos(angle) - a.dy*math.sin(angle)      #Rotation
        uy = a.dx*math.sin(angle) + a.dy*math.cos(angle)

        bux = b.dx*math.cos(angle) - b.dy*math.sin(angle)
        buy = b.dx*math.sin(angle) + b.dy*math.cos(angle)

        aux =  (ux*(a.mag-b.mag)+2*b.mag*bux)/(a.mag+b.mag)     #Calculate Velocity
        abux = (bux*(b.mag-a.mag)+2*a.mag*ux)/(b.mag+a.mag)

        b.dx = abux*math.cos(-angle) - buy*math.sin(-angle)       #Rotation back
        b.dy = abux*math.sin(-angle) + buy*math.cos(-angle)

        a.dx = aux*math.cos(angle) + uy*math.sin(angle)
        a.dy = -aux*math.sin(angle) + uy*math.cos(angle)

