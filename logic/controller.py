import pygame
from game_objects.snake import Snake

# Direction Constants
RIGHT = "R"
LEFT = "L"
DOWN = "D"
UP = "U"

# Direction mappings
DIRECTIONS = {UP: (0, -1), DOWN: (0, 1), LEFT: (-1, 0), RIGHT: (1, 0)}

moves = [RIGHT, LEFT, DOWN, UP]

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
    
    def get_move(self):
        return self.current_move

    @staticmethod
    def select(controller_type: str) -> "Controller":
        """Select and return the appropriate controller based on type.

        Args:
            controller_type (str): The type of controller to select.

        Returns:
            Controller: An instance of the selected controller type.

        Raises:
            ValueError: If the controller type is unknown.
        """
        controllers = {
            "AI": BFSController,
            "Arrow": ArrowKeyController,
            "WASD": WASDController,
            "Human": CombinedController,
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
    def __init__(self):
        super().__init__()
        
    def handle_keydown(self, event: pygame.event.EventType) -> None:
        """AI controllers do not handle keydown events."""
        pass

class BFSController(AIController):
    def __init__(self):
        super().__init__()

    def get_direction(self, snake: Snake, food_pos: tuple[int, int], width, height) -> tuple[int, int]:
        head = snake.get_head()
        best_distance = float('inf')
        
        # Define opposite directions to prevent moving backwards
        opposite_direction = (-self.direction[0], -self.direction[1])
        
        for move in moves:
            # Skip the direction if it's the opposite of the last move
            if DIRECTIONS[move] == opposite_direction:
                continue
                
            next_position = tuple(sum(x) for x in zip(head, DIRECTIONS[move]))
            
            if not snake.check_other(next_position) and not snake.check_bounds(width, height, next_position):
                if food_pos is None:
                    self.current_move = move
                    self.direction = DIRECTIONS[move]
                    return self.direction 
                distance = self.heuristic(next_position, food_pos)
                
                if distance < best_distance:
                    best_distance = distance
                    self.current_move = move
                    self.direction = DIRECTIONS[move]
        
        return self.direction

    def heuristic(self, target: tuple[int, int], goal: tuple[int, int]) -> int:
        return abs(target[0] - goal[0]) + abs(target[1] - goal[1])