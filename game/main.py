import pygame
from core.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from core.statemanager import Statemanager
from states.gameplaystate import GameplayState
from states.gameoverstate import GameoverState


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    font = pygame.font.Font("freesansbold.ttf", 32)

    clock = pygame.time.Clock()

    state_manager = Statemanager(screen)

    state_manager.add_state("gameplay", GameplayState(screen, state_manager, font))
    state_manager.add_state("game_over", GameoverState(screen, state_manager, font))

    state_manager.set_state("gameplay")

    while state_manager.is_running:
        events = pygame.event.get()

        state_manager.handle_events(events)
        dt = clock.tick(60) / 1000

        state_manager.update(dt)

        state_manager.draw()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
