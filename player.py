import pygame
from circleshape import *
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.x = x
        self.y = y

        
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c] # return the 3 points of a triangle
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2) # draw a polygon with the 3 points of a triangle as input

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt # += to make sure the ship continues turning when pressing a key

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # create a new vector pointing from 0,0 to 0,1 then rotate that to player's rotation
        self.position += forward * PLAYER_SPEED * dt # then multiply vector by playerspeed * dt (larger vector = faster movement) and then add vector to player position
        
    def shoot(self, dt):
        shot_velocity = pygame.Vector2(0, 1) # new forward pointing vector
        shot_velocity =  shot_velocity.rotate(self.rotation) # rotate vector to ship rotation
        shot_velocity = shot_velocity * PLAYER_SHOOT_SPEED # scale vector with PLAYER_SHOOT_SPEED
        
        Shot(self.position.x, self.position.y, shot_velocity) # self.position is a vector, this way we can forward x and y coordinates to spawn a new Shot

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1) # turn left after pressing a, negative dt
        if keys[pygame.K_d]:
            self.rotate(dt) # turn right after pressing d, positive dt
        if keys[pygame.K_w]:
            self.move(dt) # move forward after pressing w, positive dt
        if keys[pygame.K_s]:
            self.move(dt * -1) # move backward after pressing s, negative dt
        if keys[pygame.K_SPACE]:
            self.shoot(dt)