import pygame


class Button:
    def __init__(self, x, y, width, height, text, font, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.callback = callback
        self.color = (100, 100, 100)
        self.hover_color = (150, 150, 150)
        self.text_color = (255, 255, 255)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.callback()

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        current_color = (
            self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        )

        pygame.draw.rect(screen, current_color, self.rect)

        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)
