import pygame
from ball import *
from hero import *
from gb_model import *
from gb_space import *




def main():
    pygame.init()

    screen = pygame.display.set_mode((model.frame_width,model.frame_height))
    
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

        screen.blit(model.background.surface, (0,0))

        model.gameobjects.draw(screen)
        #screen.blit(model.hero.surface, (model.hero.x, model.hero.y))
        for v in model.villans:
            screen.blit(v.surface, (v.x, v.y))

        pygame.display.flip()


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
    model = gb_model()
    main()