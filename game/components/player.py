import pygame
from util.circleShape import CircleShape
from components.shot import Shot
from core.constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SHOOT_SPEED,
    INVINCIBLE_FOR,
)


class Player(CircleShape):
    def __init__(
        self,
        x,
        y,
        radius=PLAYER_RADIUS,
        turn_speed=PLAYER_TURN_SPEED,
        player_speed=PLAYER_SPEED,
        shot_speed=PLAYER_SHOOT_SPEED,
    ):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y

        self.turn_speed = turn_speed
        self.player_speed = player_speed
        self.rotation = 0

        self.player_shoot_speed = shot_speed
        self.cooldown = 0

        self.is_invincible = False
        self.invincibility_timer = 0
        self.flash_rate = 0.1

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def respawn(self, other):
        respawned_player = Player(self.x, self.y)
        respawned_player.is_invincible = True
        respawned_player.invincibility_timer = INVINCIBLE_FOR

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.player_speed * dt

    def rotate(self, dt, direction=1):
        self.rotation += self.turn_speed * direction * dt

    def shoot(self):
        if self.cooldown > 0:
            return
        self.cooldown = PLAYER_SHOOT_COOLDOWN
        x, y = self.position
        shot = Shot(x=x, y=y)
        shot.velocity = (
            pygame.Vector2(0, 1).rotate(self.rotation) * self.player_shoot_speed
        )

    def draw(self, screen):

        if not self.is_invincible or int(self.invincibility_timer * 10) % 2 == 0:
            points = self.triangle()
            pygame.draw.polygon(surface=screen, color="white", points=points, width=2)

    def update(self, dt):
        self.cooldown -= dt

        if self.is_invincible:
            self.invincibility_timer -= dt
            if self.invincibility_timer <= 0:
                self.is_invincible = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt, -1)
        if keys[pygame.K_d]:
            self.rotate(dt, 1)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
