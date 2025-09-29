from core.constants import PLAYER_LIVES, RESPAWN_TIMER


class DynamicText:
    """A class to handle updating text that changes frequently."""

    def __init__(self, font, color, pos, initial_text=""):
        self.font = font
        self.color = color
        self.pos = pos
        self._text = initial_text
        self.image = None
        self.rect = None
        self.update_image()  # Initial render

    def update_image(self):
        self.image = self.font.render(self._text, True, self.color)
        self.rect = self.image.get_rect(center=self.pos)

    def set_text(self, new_text):
        if str(new_text) != self._text:
            self._text = str(new_text)
            self.update_image()

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class ScoreText(DynamicText):
    """A specialized text display for a player's score."""

    def __init__(self, font, color, pos):
        super().__init__(font, color, pos, "Score: 0")

    def update_score(self, score):
        self.set_text(f"Score: {score}")


class LiveText(DynamicText):

    def __init__(self, font, color, pos):
        super().__init__(font, color, pos, f"Lives: {PLAYER_LIVES}")

    def update_life(self, life):
        self.set_text(f"Lives: {life}")


class RespawnText(DynamicText):
    def __init__(self, font, color, pos):
        super().__init__(font, color, pos, f"Respawning in: {RESPAWN_TIMER}")

    def update_timer(self, resp_timer):
        self.set_text(f"Respawning in: {RESPAWN_TIMER}")
