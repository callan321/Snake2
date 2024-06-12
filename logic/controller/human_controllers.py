from logic.controller.controller import Controller
import pygame


class HumanController(Controller):
    """
    Base class for human-controlled controllers.

    Attributes:
        key_mappings (dict): The key mappings for direction control.
    """

    key_mappings = {}
    
    def get_direction(self):
        """
        Return the current direction.

        Returns:
            Tuple[int, int]: The current direction as (x, y) coordinates.
        """
        return self.direction

    def handle_keydown(self, event: pygame.event.EventType) -> None:
        """
        Handle keydown events based on key mappings.

        Args:
            event (pygame.event.EventType): The keydown event to handle.
        """
        for key, direction in self.key_mappings.items():
            if (
                event.key == key
                and self.direction != self.DIRECTIONS[direction["opposite"]]
            ):
                self.direction = self.DIRECTIONS[direction["move"]]
                break


class ArrowKeyController(HumanController):
    """
    Controller for handling arrow key inputs.
    """

    key_mappings = {
        pygame.K_RIGHT: {"move": Controller.RIGHT, "opposite": Controller.LEFT},
        pygame.K_LEFT: {"move": Controller.LEFT, "opposite": Controller.RIGHT},
        pygame.K_DOWN: {"move": Controller.DOWN, "opposite": Controller.UP},
        pygame.K_UP: {"move": Controller.UP, "opposite": Controller.DOWN},
    }


class WASDController(HumanController):
    """
    Controller for handling WASD key inputs.
    """

    key_mappings = {
        pygame.K_d: {"move": Controller.RIGHT, "opposite": Controller.LEFT},
        pygame.K_a: {"move": Controller.LEFT, "opposite": Controller.RIGHT},
        pygame.K_s: {"move": Controller.DOWN, "opposite": Controller.UP},
        pygame.K_w: {"move": Controller.UP, "opposite": Controller.DOWN},
    }


class CombinedController(HumanController):
    """
    Controller for handling both arrow and WASD key inputs.
    """

    key_mappings = {
        pygame.K_RIGHT: {"move": Controller.RIGHT, "opposite": Controller.LEFT},
        pygame.K_d: {"move": Controller.RIGHT, "opposite": Controller.LEFT},
        pygame.K_LEFT: {"move": Controller.LEFT, "opposite": Controller.RIGHT},
        pygame.K_a: {"move": Controller.LEFT, "opposite": Controller.RIGHT},
        pygame.K_DOWN: {"move": Controller.DOWN, "opposite": Controller.UP},
        pygame.K_s: {"move": Controller.DOWN, "opposite": Controller.UP},
        pygame.K_UP: {"move": Controller.UP, "opposite": Controller.DOWN},
        pygame.K_w: {"move": Controller.UP, "opposite": Controller.DOWN},
    }
