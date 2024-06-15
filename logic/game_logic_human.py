from logic.controller.human_controllers import HumanController
from logic.game_objects.snake import Snake
from typing import Tuple, Dict, List, Deque
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

    def count_human_controllers(self) -> int:
        """
        Count the number of controllers that are of type HumanController.

        Returns:
            int: The number of human controllers.
        """
        return sum(1 for controller in self.controllers if isinstance(controller, HumanController))
    
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
