from logic.game_objects.snake import Snake
from logic.game_objects.food import Food
from logic.game_objects.spawn_generator import SpawnGenerator
from logic.controller.controller import Controller, AIController
from typing import Tuple

class GameLogicAI:
    """
    Manages the game logic for a snake game controlled by AI.

    Attributes:
        width (int): The width of the game area.
        height (int): The height of the game area.
        snake (Snake): The snake object.
        spawn_generator (SpawnGenerator): The spawn generator for food.
        food (Food): The food object.
        controller (Controller): The controller for the snake's movement.
        last_direction (tuple[int, int]): The last direction the snake moved in.
        opposite_direction (tuple[int, int]): The opposite of the last direction the snake moved in.
    """

    def __init__(self, width: int, height: int, controller_type: str = "AI", snake_size: int = 3) -> None:
        """
        Initialize the game logic with the given parameters.

        Args:
            width (int): The width of the game area.
            height (int): The height of the game area.
            controller_type (str): The type of controller (default is 'AI').
            snake_size (int): The initial size of the snake (default is 3).
        """
        start_x = (width // 2) - 1 if width % 2 == 0 else width // 2
        start_pos: Tuple[int, int] = (start_x, 0)
        self.width = width
        self.height = height
        self.snake = Snake(start_pos, snake_size)
        self.spawn_generator = SpawnGenerator(self.width, self.height, start_pos)
        self.food = Food()
        self.controller = Controller.select(controller_type)
        self.last_direction = None
        self.opposite_direction = None

    def update(self) -> bool:
        """
        Update the game state for the next frame.

        Returns:
            bool: True if the game continues, False if there's a collision.
        """
        self.update_snake()
        self.update_spawns()
        self.check_food_collision()
        self.update_food()
        return not self.check_collisions()

    def update_snake(self) -> None:
        """
        Update the snake's position based on the direction.
        """
        direction = self.get_direction()
        if not self.is_opposite_direction(direction):
            self.snake.update(direction, self.food.get_position())
            self.last_direction = direction
            self.opposite_direction = self.get_opposite_direction(direction)
        else:
            self.snake.update(self.last_direction, self.food.get_position())

    def get_direction(self) -> Tuple[int, int]:
        """
        Get the direction from the controller.

        Returns:
            Tuple[int, int]: The direction vector.
        """
        return self.controller.get_direction(self.snake, self.food.get_position(), self.width, self.height, self.opposite_direction)

    def get_opposite_direction(self, direction: Tuple[int, int]) -> Tuple[int, int]:
        """
        Calculate the opposite direction.

        Args:
            direction (Tuple[int, int]): The current direction vector.

        Returns:
            Tuple[int, int]: The opposite direction vector.
        """
        return (-direction[0], -direction[1])

    def is_opposite_direction(self, direction: Tuple[int, int]) -> bool:
        """
        Check if the given direction is opposite to the last direction.

        Args:
            direction (Tuple[int, int]): The current direction vector.

        Returns:
            bool: True if the direction is opposite, False otherwise.
        """
        return direction == self.opposite_direction

    def update_spawns(self) -> None:
        """
        Update the spawn generator.
        """
        head_pos = self.snake.get_head()
        tail_pos = self.snake.get_last_tail()
        self.spawn_generator.insert(tail_pos)
        self.spawn_generator.remove(head_pos)

    def check_food_collision(self) -> None:
        """
        Check if the snake has eaten the food and update the game state accordingly.
        """
        if self.snake.check_ate():
            self.food.remove()

    def update_food(self) -> None:
        """
        Update the food's position if it has been eaten or despawned.
        """
        if not self.food.exists():
            self.food.update(self.spawn_generator.get_random())

    def check_collisions(self) -> bool:
        """
        Check for collisions with the walls or the snake itself.

        Returns:
            bool: True if there is a collision, False otherwise.
        """
        return self.snake.check_collision(self.width, self.height)
