import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt) # update everything in the updatable sprite.Group
        
        for asteroid in asteroids:
            if asteroid.collision(player): # if an asteroid collides with the player, then print game over and exit
                print("Game over!")
                sys.exit()
            
            for shot in shots: # iterate over all the bullets in the shots group, since collision expects a single object not a group
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black") # make the background color black

        for obj in drawable: # go over every object in the drawable sprite group and draw them
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()