from logic.controller.controller import Controller
from logic.controller.human_controllers import HumanController
from logic.game_objects.snake import Snake
from typing import Tuple, Dict, List, Deque
from logic.game_logic import GameLogic
from logic.game_objects.snake import Snake
from logic.game_objects.food import Food
from logic.game_objects.spawn_generator import SpawnGenerator
from logic.game_objects.snake_spawner import SnakeSpawner
from logic.controller.controller import Controller
from typing import Tuple, List, Deque, Dict
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
    def __init__(
        self, width: int, height: int, controllers: List[str] = ["Greedy"], snake_size: int = 3, num_snakes: int = 1, game_mode: str = 'survival'
    ) -> None:
        super().__init__(width, height, controllers, snake_size, num_snakes, game_mode)
        self.human_controllers = []
        for key in self.keys:
            if isinstance(self.controllers[key], HumanController):
                self.human_controllers.append(key)


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
            snake, self.food.get_position(), self.width, self.height, self.snakes, self.keys
        )

    def update_snake(self, snake_id: int, snake: Snake) -> None:
        """
        Update the snake's position based on the direction.
        """
        direction = self.get_direction(snake_id)
        snake.update(direction, self.food.get_position())


    def get_all_snakes_body_and_direction(
        self
    ) -> List[Tuple[int, Deque[Tuple[int, int]], Tuple[int, int]]]:
        """
        Get the body and the direction of all snakes controlled by their respective controllers.

        Args:
            snakes (Dict[int, 'Snake']): Dictionary of snake IDs and their corresponding Snake objects.
            controllers (Dict[int, 'Controller']): Dictionary of snake IDs and their corresponding Controller objects.

        Returns:
            List[Tuple[int, Deque[Tuple[int, int]], Tuple[int, int]]]: A list of tuples containing snake ID, the body of the snake, and the direction of the controller.
        """
        result = []
        for snake_id, snake in self.snakes.items():
            if snake_id in self.controllers:  
                snake_body = snake.get_body() 
                snake_direction = self.get_controller(snake_id).get_current_direction()  
                result.append((snake_id, snake_body, snake_direction))
        return result


    def remove_key(self, key):
        super().remove_key(key)
        if key in self.human_controllers:
            self.human_controllers.remove(key)
            