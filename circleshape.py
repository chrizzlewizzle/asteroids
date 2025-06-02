import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collision(self, other):
        
        # Calculate distance from two vectors
        distance = self.position.distance_to(other.position)
                
        # Calculate the size of both of the circles
        size = self.radius + other.radius
        # If distance is smaller than both radiusses combined, there must be a colision        
        if distance <= size:
            return True
        else:
            return False