import pygame


class Statemanager:
    def __init__(self, screen):
        self.screen = screen
        self.states = {}
        self.current_state = None
        self.__is_running = True

    def add_state(self, state_name, state):
        self.states[state_name] = state

    def set_state(self, state_name, **kwargs):
        if state_name not in self.states:
            print(f"Error occured: {state_name} not found in {self.states}")
            self.is_running = False

        self.current_state = self.states[state_name]

        if state_name == "game_over":
            self.current_state.startup(score=kwargs.get("score", 0))
        else:
            self.current_state.startup()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.is_running = False
            else:
                if self.current_state.handle_events:
                    self.current_state.handle_events(event)

    @property
    def is_running(self):
        return self.__is_running

    @is_running.setter
    def is_running(self, value):
        if not isinstance(value, bool):
            raise ValueError("is_running must be a boolean value")
        self.__is_running = value

    def quit(self):
        self.is_running = False

    def update(self, dt):
        self.current_state.update(dt)

    def draw(self):
        self.current_state.draw(self.screen)
