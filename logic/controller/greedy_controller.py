from logic.controller.controller import Controller 
from logic.game_objects.snake import Snake
from typing import Tuple

class GreedyController(Controller):
    """
    AI controller using Breadth-First Search (BFS) for decision making.
    """



    def get_direction(
        self,
        snake: Snake,
        food_pos: Tuple[int, int],
        width: int,
        height: int
    ) -> Tuple[int, int]:
        """
        Determine the best direction based on Breadth-First Search algorithm.

        Args:
            snake (Snake): The snake object.
            food_pos (Tuple[int, int]): The position of the food.
            width (int): The width of the game board.
            height (int): The height of the game board.

        Returns:
            Tuple[int, int]: The best direction as (x, y) coordinates.
        """
        head = snake.get_head()
        best_distance = float("inf")

        for direction in self.DIRECTIONS:
            if direction == self.opposite_direction:
                continue

            next_position = (head[0] + direction[0], head[1] + direction[1])

            if not snake.check_exist(next_position) and not snake.check_bounds(
                width, height, next_position
            ):
                if food_pos is None:
                    self.direction = direction
                    return self.direction

                distance = self.heuristic(next_position, food_pos)

                if distance < best_distance:
                    best_distance = distance
                    self.direction = direction

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
