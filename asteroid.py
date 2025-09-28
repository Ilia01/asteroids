from circleShape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    angle = random.uniform(20, 50)
    vel1 = self.velocity.rotate(angle)
    vel2 = self.velocity.rotate(-angle)
    
    x, y = self.position
    asteroid1 = Asteroid(x, y, new_radius)
    asteroid1.velocity = vel1 * 1.2
    asteroid2 = Asteroid(x, y, new_radius)  
    asteroid2.velocity = vel2 * 1.2


  def draw(self, screen): 
    pygame.draw.circle(surface=screen, color="white",center=self.position, radius=self.radius)

  def update(self, dt):
    self.position += self.velocity * dt
