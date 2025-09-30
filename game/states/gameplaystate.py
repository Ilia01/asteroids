import pygame
from states.baseState import BaseState
from components.asteroid import Asteroid
from components.asteroidfield import AsteroidField
from components.shot import Shot
from components.player import Player
from core.constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_LIVES, RESPAWN_TIMER
from util.text_classes import ScoreText, LiveText, DynamicText, RespawnText


class GameplayState(BaseState):
    def __init__(self, screen, state_manager, font):
        super().__init__(screen, state_manager)
        self.font = font

        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)
        AsteroidField.containers = self.updatable
        Shot.containers = (self.bullets, self.updatable, self.drawable)
        Player.containers = (self.updatable, self.drawable)

        self.asteroid_field = None
        self.player = None
        self.score = 0
        self.score_display = None

        self.player_lives = 0
        self.player_lives_display = None

        self.is_respawning = False
        self.respawn_timer = 0
        self.respawn_surface = None
        self.respawn_text_display = None

    def startup(self, **kwargs):
        self.score = 0
        self.player_lives = PLAYER_LIVES

        self.score_display = ScoreText(
            self.font, (255, 255, 255), (SCREEN_WIDTH / 1.2, 30)
        )
        self.player_lives_display = LiveText(
            self.font,
            (255, 255, 255),
            (SCREEN_WIDTH / 5, 30),
        )

        self.respawn_text_display = RespawnText(
            self.font, "white", (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        )

        self.updatable.empty()
        self.drawable.empty()
        self.asteroids.empty()
        self.bullets.empty()

        self.asteroid_field = AsteroidField()
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        self.respawn_surface = pygame.surface.Surface(
            flags=pygame.SRCALPHA,
            size=(SCREEN_WIDTH, SCREEN_HEIGHT),
        )

    def handle_events(self, events):
        pass

    def update(self, dt):
        self.updatable.update(dt)

        if self.is_respawning:
            self.respawn_timer -= dt
            self.respawn_text_display.set_text(
                f"Respawning in {self.respawn_timer:0.2f}"
            )
            if self.respawn_timer <= 0:
                if self.player_lives > 0:
                    self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                else:
                    self.state_manager.set_state("game_over", score=self.score)

                self.is_respawning = False

        if not self.is_respawning and self.player is not None:
            for asteroid in self.asteroids:
                for bullet in self.bullets:
                    if bullet.collides_with(asteroid):
                        self.score += 1
                        self.score_display.update_score(self.score)
                        asteroid.split()
                        bullet.kill()

            for asteroid in self.asteroids:
                if self.player is None:
                    break

                if not self.player.is_invincible:
                    if asteroid.collides_with(self.player):
                        self.player_lives -= 1
                        self.player_lives_display.update_life(self.player_lives)
                        self.player.kill()
                        self.player = None

                        if self.player_lives > 0:
                            self.is_respawning = True
                            self.respawn_timer = RESPAWN_TIMER
                        else:
                            self.state_manager.set_state("game_over", score=self.score)

    def draw(self, screen):
        screen.fill("black")
        for obj in self.drawable:
            obj.draw(screen)

        self.score_display.draw(screen)
        self.player_lives_display.draw(screen)

        if self.is_respawning:
            self.respawn_surface.fill(color=(0, 0, 0, 150))

            screen.blit(self.respawn_surface, (0, 0))

            self.respawn_text_display.draw(self.screen)
