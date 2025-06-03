import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill() # remove hit asteroid
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            velocity1 = pygame.math.Vector2.rotate(self.velocity, angle)
            velocity2 = pygame.math.Vector2.rotate(self.velocity, -angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            print(f"Velocity1 {velocity1}, Velocity2 {velocity2}, new_radius {new_radius}")
            # after getting a random new angle and setting it both positive and negative, spawn 2 new asteroids on these angles and multiply their speed by 1.2
            A1 = Asteroid(self.position.x, self.position.y, new_radius)
            A1.velocity = velocity1 * 1.2
            A2 = Asteroid(self.position.x, self.position.y, new_radius)
            A2.velocity = velocity2 * 1.2