from game_objects.snake import Snake
from game_objects.food import Food
from game_objects.spawn_generator import SpawnGenerator
from logic.controller import Controller, AIController
from typing import Tuple

class GameLogicAI:
    """Manages the game logic for AI controller."""

    def __init__(self, width: int, height: int, controller_type: str = 'AI', snake_size: int = 3) -> None:
        """Initialize the game logic for AI.
        
        Args:
            width (int): The width of the game area.
            height (int): The height of the game area.
            controller_type (str): The type of controller (default is 'AI').
            snake_size (int): The initial size of the snake.
        """
        adjust_start_x = lambda x: x - 1 if width % 2 == 0 else x
        start_x = adjust_start_x(width // 2)
        start_pos: Tuple[int, int] = (start_x, 0)
        self.width, self.height = width, height
        self.snake = Snake(start_pos, snake_size)
        self.spawn_generator = SpawnGenerator(self.width, self.height, start_pos)
        self.food = Food()
        self.controller = Controller.select(controller_type, self.width, self.height)

    def update(self) -> None:
        """Update the game logic."""
        direction = self.get_direction()
        self.snake.update(direction, self.food.get_position())
        self.manage_snake_movement()
        self.check_food_collision()
        self.update_food()
        self.check_collisions()

    def get_direction(self) -> Tuple[int, int]:
        """Get the direction for the snake to move.
        
        Returns:
            Tuple[int, int]: The direction for the snake to move.
        """
        return self.controller.get_direction(self.snake, self.food.get_position(), self.width, self.height)

    def manage_snake_movement(self) -> None:
        """Manage the snake's movement."""
        head_pos = self.snake.get_head()
        tail_pos = self.snake.get_last_tail()
        self.spawn_generator.insert(tail_pos)
        self.spawn_generator.remove(head_pos)

    def check_food_collision(self) -> None:
        """Check if the snake has collided with the food."""
        if self.snake.check_ate():
            self.food.remove()

    def update_food(self) -> None:
        """Update the food's position if it has despawned."""
        if self.food.check_if_despawned():
            self.food.update(self.spawn_generator.get_random())

    def check_collisions(self) -> None:
        """Check for collisions with walls or self."""
        if self.snake.check_collision(self.width, self.height):
            self.running = False


class GameLogic(GameLogicAI):
    """Manages the game logic for both AI and human controllers."""

    def __init__(self, width: int, height: int, controller_type: str = 'AI', snake_size: int = 3) -> None:
        """Initialize the game logic.
        
        Args:
            width (int): The width of the game area.
            height (int): The height of the game area.
            controller_type (str): The type of controller (default is 'AI').
            snake_size (int): The initial size of the snake.
        """
        super().__init__(width, height, controller_type, snake_size)

    def get_direction(self) -> Tuple[int, int]:
        """Get the direction for the snake to move.
        
        Returns:
            Tuple[int, int]: The direction for the snake to move.
        """
        if isinstance(self.controller, AIController):
            return self.controller.get_direction(self.snake, self.food.get_position())
        return self.controller.get_direction()
