import pygame

class BaseState:
    def __init__(self, screen, state_manager):
        self.screen = screen
        self.state_manager = state_manager
        self.done = False 
        self.next_state = None 

    def startup(self, **kwargs):
        """Called when a state becomes the active state."""
        pass

    def handle_events(self, events):
        """Handle all user input events for the current state."""
        pass

    def update(self, dt):
        """Update the state's internal logic and objects."""
        pass

    def draw(self, screen):
        """Draw the state's graphics to the screen."""
        pass
