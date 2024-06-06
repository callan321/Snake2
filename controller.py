import pygame

# Direction Constants
RIGHT = "R"
LEFT = "L"
DOWN = "D"
UP = "U"

# Direction mappings
DIRECTIONS = {UP: (0, -1), DOWN: (0, 1), LEFT: (-1, 0), RIGHT: (1, 0)}


class Controller:
    def __init__(self):
        self.current_move = DOWN
        self.direction = DIRECTIONS[self.current_move]

    def handle_keydown(self, event: pygame.event.EventType) -> None:
        """Handle keydown events. Should be overridden by subclasses."""
        raise NotImplementedError("This method should be overridden by subclasses")

    def get_direction(self) -> tuple[int, int]:
        """Return the current direction as a tuple of (x, y) coordinates."""
        return self.direction

    @staticmethod
    def select(controller_type: str) -> 'Controller':
        """Select and return the appropriate controller based on type.

        Args:
            controller_type (str): The type of controller to select.

        Returns:
            Controller: An instance of the selected controller type.

        Raises:
            ValueError: If the controller type is unknown.
        """
        controllers = {
            "AI": TESTController,
            "Arrow": ArrowKeyController,
            "WASD": WASDController,
            "Combined": CombinedController,
        }
        if controller_type in controllers:
            return controllers[controller_type]()
        else:
            raise ValueError(f"Unknown controller type: {controller_type}")


class HumanController(Controller):
    key_mappings = {}

    def __init__(self):
        super().__init__()
        self.changed_direction = False

    def handle_keydown(self, event: pygame.event.EventType) -> None:
        """Handle keydown events for given key mappings."""
        new_direction = None
        if not self.changed_direction:
            for key, direction in self.key_mappings.items():
                if event.key == key and self.current_move != direction["opposite"]:
                    new_direction = direction["move"]
                    break

        if new_direction:
            self.current_move = new_direction
            self.direction = DIRECTIONS[self.current_move]
            self.changed_direction = True

    def get_direction(self) -> tuple[int, int]:
        """Return the current direction and reset the changed_direction flag."""
        self.changed_direction = False
        return self.direction


class ArrowKeyController(HumanController):
    key_mappings = {
        pygame.K_RIGHT: {"move": RIGHT, "opposite": LEFT},
        pygame.K_LEFT: {"move": LEFT, "opposite": RIGHT},
        pygame.K_DOWN: {"move": DOWN, "opposite": UP},
        pygame.K_UP: {"move": UP, "opposite": DOWN},
    }


class WASDController(HumanController):
    key_mappings = {
        pygame.K_d: {"move": RIGHT, "opposite": LEFT},
        pygame.K_a: {"move": LEFT, "opposite": RIGHT},
        pygame.K_s: {"move": DOWN, "opposite": UP},
        pygame.K_w: {"move": UP, "opposite": DOWN},
    }


class CombinedController(HumanController):
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


class AIController(Controller):
    def handle_keydown(self, event: pygame.event.EventType) -> None:
        """AI controllers do not handle keydown events."""
        pass


class TESTController(AIController):
    def __init__(self):
        super().__init__()

    def get_direction(self, snake_head: tuple[int, int], food_pos: tuple[int, int] | None) -> tuple[int, int]:
        """Determine the direction based on snake head and food positions.

        Args:
            snake_head (tuple[int, int]): The current position of the snake's head.
            food_pos (tuple[int, int] | None): The position of the food. None if no food is present.

        Returns:
            tuple[int, int]: The new direction as a tuple of (x, y) coordinates.
        """
        head_x, head_y = snake_head

        if food_pos is None:
            self.current_move = DOWN
            self.direction = DIRECTIONS[self.current_move]
            return self.direction

        food_x, food_y = food_pos

        if head_x < food_x:
            new_direction = RIGHT
        elif head_x > food_x:
            new_direction = LEFT
        elif head_y < food_y:
            new_direction = DOWN
        elif head_y > food_y:
            new_direction = UP
        else:
            new_direction = self.current_move

        self.current_move = new_direction
        self.direction = DIRECTIONS.get(self.current_move, (0, 1))  # Default to moving down if direction not found
        return self.direction
