from logic.controller.controller import Controller
from logic.game_objects.snake import Snake
from typing import Tuple, List, Dict


class GreedyController(Controller):
    """
    AI controller using Greedy-First Search for decision making.
    """

    def get_direction(
        self,
        snake: Snake,
        food_pos: Tuple[int, int],
        width: int,
        height: int,
        snakes: Dict[int, Snake], 
        keys: List[int]
    ) -> Tuple[int, int]:
        """
        Determine the best direction based on Breadth-First Search algorithm.

        Args:
            snake (Snake): The snake object.
            food_pos (Tuple[int, int]): The position of the food.
            width (int): The width of the game board.
            height (int): The height of the game board.
            snakes (List[Snake]): List of all snakes in the game.

        Returns:
            Tuple[int, int]: The best direction as (x, y) coordinates.
        """
        head = snake.get_head()
        best_distance = float("inf")
        best_direction = self.direction  # Keep current direction as default

        for direction in self.DIRECTIONS:
            if direction == self.opposite_direction:
                continue

            next_position = (head[0] + direction[0], head[1] + direction[1])

            if not snake.check_bounds(
                width, height, next_position
            ) and not self.check_position_in_snakes(next_position, snakes, keys):

                if food_pos is None:
                    self.direction = direction
                    return self.direction

                distance = self.heuristic(next_position, food_pos)

                if distance < best_distance:
                    best_distance = distance
                    best_direction = direction

        self.direction = best_direction
        self.opposite_direction = self.get_opposite_direction(self.direction)
        return self.direction

    def heuristic(self, target: Tuple[int, int], goal: Tuple[int, int]) -> int:
        """
        Heuristic function to estimate the distance to the goal.

        Args:
            target (Tuple[int, int]): The target position.
            goal (Tuple[int, int]): The goal position.

        Returns:
            int: The Manhattan distance between the target and the goal.
        """
        return abs(target[0] - goal[0]) + abs(target[1] - goal[1])

    def check_position_in_snakes(
        self, position: Tuple[int, int], snakes: Dict[int, Snake], keys: List[int]
    ) -> bool:
        """
        Check if the position collides with any other snake.

        Args:
            position (Tuple[int, int]): The position to check.
            snakes (List[Snake]): List of all snakes in the game.

        Returns:
            bool: True if there is a collision, False otherwise.
        """
        
        for key in keys:
            snake = snakes[key]
            if snake.check_position_exists(position):
                return True
        return False

    def get_opposite_direction(self, direction: Tuple[int, int]) -> Tuple[int, int]:
        """
        Get the opposite direction of the current direction.

        Args:
            direction (Tuple[int, int]): The current direction.

        Returns:
            Tuple[int, int]: The opposite direction.
        """
        return (-direction[0], -direction[1])
