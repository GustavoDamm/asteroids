from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        #destroy
        self.kill()

        #Destroy if below minimum radius
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        #Random angle
        random_angle = random.uniform(20, 50)

        # Two new velocity
        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)

        #Calc new radius
        splitted_new_radius = self.radius - ASTEROID_MIN_RADIUS

        #Create new asteroid + update the speed
        a1 = Asteroid(self.position.x, self.position.y, splitted_new_radius)
        a1.velocity = v1 * 1.2

        a2 = Asteroid(self.position.x, self.position.y, splitted_new_radius)
        a2.velocity = v2 * 1.2
