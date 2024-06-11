from logic.controller.controller import Controller, DIRECTIONS, UP, DOWN, LEFT, RIGHT
import pygame

class HumanController(Controller):
    """
    Base class for human-controlled controllers.

    Attributes:
        key_mappings (dict): The key mappings for direction control.
        changed_direction (bool): Flag to indicate if the direction has changed.
    """

    key_mappings = {}

    def __init__(self):
        """
        Initialize the HumanController with default settings.
        """
        super().__init__()
        self.changed_direction = False

    def handle_keydown(self, event: pygame.event.EventType) -> None:
        """
        Handle keydown events based on key mappings.

        Args:
            event (pygame.event.EventType): The keydown event to handle.
        """
        new_direction = None
        if not self.changed_direction:
            for key, direction in self.key_mappings.items():
                if (
                    event.key == key
                    and self.direction != DIRECTIONS[direction["opposite"]]
                ):
                    new_direction = DIRECTIONS[direction["move"]]
                    break

        if new_direction:
            self.direction = new_direction
            self.changed_direction = True

    def get_direction(self) -> tuple[int, int]:
        """
        Return the current direction and reset the changed_direction flag.

        Returns:
            tuple[int, int]: The current direction as (x, y) coordinates.
        """
        self.changed_direction = False
        return self.direction


class ArrowKeyController(HumanController):
    """
    Controller for handling arrow key inputs.
    """

    key_mappings = {
        pygame.K_RIGHT: {"move": RIGHT, "opposite": LEFT},
        pygame.K_LEFT: {"move": LEFT, "opposite": RIGHT},
        pygame.K_DOWN: {"move": DOWN, "opposite": UP},
        pygame.K_UP: {"move": UP, "opposite": DOWN},
    }


class WASDController(HumanController):
    """
    Controller for handling WASD key inputs.
    """

    key_mappings = {
        pygame.K_d: {"move": RIGHT, "opposite": LEFT},
        pygame.K_a: {"move": LEFT, "opposite": RIGHT},
        pygame.K_s: {"move": DOWN, "opposite": UP},
        pygame.K_w: {"move": UP, "opposite": DOWN},
    }


class CombinedController(HumanController):
    """
    Controller for handling both arrow and WASD key inputs.
    """

    key_mappings = {
        pygame.K_RIGHT: {"move": RIGHT, "opposite": LEFT},
        pygame.K_d: {"move": RIGHT, "opposite": LEFT},
        pygame.K_LEFT: {"move": LEFT, "opposite": RIGHT},
        pygame.K_a: {"move": LEFT, "opposite": RIGHT},
        pygame.K_DOWN: {"move": DOWN, "opposite": UP},
        pygame.K_s: {"move": DOWN, "opposite": UP},
        pygame.K_UP: {"move": UP, "opposite": DOWN},
        pygame.K_w: {"move": UP, "opposite": DOWN},
    }
