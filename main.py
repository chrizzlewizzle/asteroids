# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # initialize a screen the size of the SCREEN_WIDTH and SCREEN_HEIGHT in constants
    black = (0, 0, 0) # set the color black to the correct RGB values

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group() # new group for objects that can be updated
    drawable = pygame.sprite.Group() # new group for objects that can be drawn

    Player.containers = (updatable, drawable) # both groups are containers for the player
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) # create a new player

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(black) # make the entire screen black
        updatable.update(dt) # update everything in the updatable group
        
        for thing in drawable:
            thing.draw(screen) # render everything in the drawable group to the screen
        
        
        pygame.display.flip() # push the screen to the display
        
        dt = clock.tick(60) / 1000 # limit framerate to 60 fps

        

if __name__ == "__main__":
    main()