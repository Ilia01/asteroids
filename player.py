import pygame
from circleShape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_COOLDOWN, PLAYER_SHOOT_SPEED

class Player(CircleShape):
  def __init__(self, x, y, radius=PLAYER_RADIUS, turn_speed=PLAYER_TURN_SPEED, player_speed=PLAYER_SPEED, shot_speed=PLAYER_SHOOT_SPEED):
    super().__init__(x, y, radius)
    self.turn_speed = turn_speed
    self.player_speed = player_speed
    self.rotation = 0

    self.player_shoot_speed = shot_speed
    self.cooldown = 0

  def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
      a = self.position + forward * self.radius
      b = self.position - forward * self.radius - right
      c = self.position - forward * self.radius + right
      return [a, b, c]

  def move(self, dt):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += forward * self.player_speed * dt

  def rotate(self, dt):
    self.rotation += self.turn_speed * dt

  def shoot(self):
    if self.cooldown > 0:
      return
    self.cooldown = PLAYER_SHOOT_COOLDOWN
    x, y =self.position
    shot = Shot(x=x, y=y)
    shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * self.player_shoot_speed
    
  def draw(self, screen):
     points = self.triangle()
     return pygame.draw.polygon(surface=screen, color="white", points=points, width=2)

  def update(self, dt):
        self.cooldown -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            print("a key pressed")
            self.rotate(60-dt)
        if keys[pygame.K_d]:
            print("d key pressed")
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
