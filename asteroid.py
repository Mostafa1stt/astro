import random
from circleshape import *
from constants import *
import pygame


class Asteroid(CircleShape):
    def __init__(self, x, y, raduis):
        super().__init__(x, y, raduis)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 1)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)

            new_vel = self.velocity.rotate(random_angle) * 1.2
            new_vel_2 = self.velocity.rotate(-random_angle) * 1.2

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            small_aster_1 = Asteroid(self.position.x, self.position.y, new_radius)
            small_aster_2 = Asteroid(self.position.x, self.position.y, new_radius)

            small_aster_1.velocity = new_vel
            small_aster_2.velocity = new_vel_2
