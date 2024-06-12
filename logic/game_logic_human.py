from logic.controller.human_controllers import HumanController
from logic.game_objects.snake import Snake
from typing import Tuple
from logic.game_logic import GameLogic

class GameLogicHuman(GameLogic):
    """
    Manages the game logic for a snake game controlled by a human.

    Attributes:
        width (int): The width of the game area.
        height (int): The height of the game area.
        snakes (List[Snake]): The list of snake objects.
        spawn_generator (SpawnGenerator): The spawn generator for food.
        food (Food): The food object.
        controllers (List[Controller]): The controllers for the snakes' movement.
        step_count (int): The number of steps taken in the current game.
    """

    def __init__(self, width: int, height: int, controller_type: str = "Human", snake_size: int = 3, num_snakes: int = 1) -> None:
        """
        Initialize the game logic with the given parameters.

        Args:
            width (int): The width of the game area.
            height (int): The height of the game area.
            controller_type (str): The type of controller (default is 'Human').
            snake_size (int): The initial size of the snake (default is 3).
            num_snakes (int): The number of snakes in the game (default is 1).
        """
        super().__init__(width, height, controller_type, snake_size, num_snakes)

    def get_direction(self, snake_id: int) -> Tuple[int, int]:
        """
        Get the direction from the controller.

        Args:
            snake_id (int): The ID of the snake.

        Returns:
            Tuple[int, int]: The direction vector.
        """
        controller = self.controllers[snake_id]
        if isinstance(controller, HumanController):
            return controller.get_direction()
        
        snake = self.snakes[snake_id]
        return controller.get_direction(
            snake, self.food.get_position(), self.width, self.height
        )

    def update_snake(self, snake_id: int, snake: Snake) -> None:
        """
        Update the snake's position based on the direction.
        """
        direction = self.get_direction(snake_id)
        snake.update(direction, self.food.get_position())
