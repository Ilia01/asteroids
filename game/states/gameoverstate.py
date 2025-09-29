from states.baseState import BaseState
import pygame
from core.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from util.button import Button
from util.text_classes import ScoreText, DynamicText


class GameoverState(BaseState):
    def __init__(self, screen, state_manager, font):
        super().__init__(screen, state_manager)
        self.font = font
        self.score = 0
        self.buttons = []
        self.text_elements = {}

    def startup(self, **kwargs):
        self.score = kwargs.get("score", 0)
        print(f"Game Over! Your score: {self.score}")
        self.create_text_elements()
        self.create_buttons()

    def create_text_elements(self):
        self.text_elements["game_over"] = DynamicText(
            font=self.font,
            color=(255, 0, 0),
            pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3),
            initial_text="Game Over!",
        )
        self.text_elements["score"] = ScoreText(
            font=self.font,
            color=(255, 255, 255),
            pos=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2),
        )
        self.text_elements["score"].update_score(self.score)

    def create_buttons(self):
        self.buttons = [
            Button(
                text="Restart",
                font=self.font,
                x=SCREEN_WIDTH / 2 - self.text_elements["game_over"].rect.width / 2,
                y=SCREEN_HEIGHT / 1.5,
                width=200,
                height=50,
                callback=lambda: self.state_manager.set_state("gameplay"),
            ),
            Button(
                text="Quit",
                font=self.font,
                x=SCREEN_WIDTH / 2 - self.text_elements["game_over"].rect.width / 2,
                y=SCREEN_HEIGHT / 1.2,
                width=200,
                height=50,
                callback=lambda: self.state_manager.quit(),
            ),
        ]

    def handle_events(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def update(self, dt):
        pass  # No logic needs to run continuously in this state

    def draw(self, screen):
        screen.fill("black")

        self.text_elements["game_over"].draw(screen)
        self.text_elements["score"].draw(screen)

        for button in self.buttons:
            button.draw(screen)
