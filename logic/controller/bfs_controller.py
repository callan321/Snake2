from logic.controller.controller import AIController, DIRECTIONS
from logic.game_objects.snake import Snake


class BFSController(AIController):
    """
    AI controller using Breadth-First Search (BFS) for decision making.
    """

    def __init__(self):
        """
        Initialize the BFSController with default settings.
        """
        super().__init__()

    def get_direction(
        self, snake: Snake, food_pos: tuple[int, int], width, height
    ) -> tuple[int, int]:
        """
        Determine the best direction based on Greedy Best First Search algorithm.

        Args:
            snake (Snake): The snake object.
            food_pos (tuple[int, int]): The position of the food.
            width (int): The width of the game board.
            height (int): The height of the game board.

        Returns:
            tuple[int, int]: The best direction as (x, y) coordinates.
        """
        head = snake.get_head()
        best_distance = float("inf")

        opposite_direction = (-self.direction[0], -self.direction[1])

        for direction in DIRECTIONS.values():
            if direction == opposite_direction:
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

        return self.direction

    def heuristic(self, target: tuple[int, int], goal: tuple[int, int]) -> int:
        """
        Heuristic function to estimate the distance to the goal.

        Args:
            target (tuple[int, int]): The target position.
            goal (tuple[int, int]): The goal position.

        Returns:
            int: The Manhattan distance between the target and the goal.
        """
        return abs(target[0] - goal[0]) + abs(target[1] - goal[1])
