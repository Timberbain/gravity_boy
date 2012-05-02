import pygame
from ball import *
from hero import *
from gb_model import *
from gb_space import *
from gb_view import *


def main():
    pygame.init()

    model.set_background()
    model.set_hero()
    model.generate_villan()
    model.generate_villan()
    model.generate_villan()

    clock = pygame.time.Clock()
    running = True
    while running:                  #The main loop
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            check_movement(event)

        model.update_model()
        view.draw()


def check_movement(event):
    """ Check the eventhandler for keyboard input 
    that controlls the hero
    """

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            model.keyup = True
        if event.key == pygame.K_DOWN:
            model.keydown = True
        if event.key == pygame.K_RIGHT:
            model.keyright = True
        if event.key == pygame.K_LEFT:
            model.keyleft = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            model.keyup = False
        if event.key == pygame.K_DOWN:
            model.keydown = False
        if event.key == pygame.K_RIGHT:
            model.keyright = False
        if event.key == pygame.K_LEFT:
            model.keyleft = False

if __name__ == "__main__":
    model = Gb_model(800, 600)
    view = Gb_view(model)
    main()
