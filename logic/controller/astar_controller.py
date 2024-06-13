from logic.controller.bfs_controller import BFSController
from logic.game_objects.snake import Snake
from queue import PriorityQueue
from typing import Tuple

class AStarController(BFSController):
    """
    AI controller using A* Search for decision making.
    """



    def get_direction(
        self,
        snake: Snake,
        food_pos: Tuple[int, int],
        width: int,
        height: int
    ) -> Tuple[int, int]:
        """
        Determine the best direction based on A* Search algorithm. If no path to food is found, 
        find the longest path to cover the remaining space.

        Args:
            snake (Snake): The snake object.
            food_pos (Tuple[int, int]): The position of the food, or None if no food is present.
            width (int): The width of the game board.
            height (int): The height of the game board.

        Returns:
            Tuple[int, int]: The best direction as (x, y) coordinates.
        """
        if food_pos:
            path_to_food = self.a_star_search(snake, food_pos, width, height)
        else:
            path_to_food = []

        if path_to_food:
            next_position = path_to_food[1]  # Skip the head position, take the next step
        else:
            next_position = self.find_longest_path(snake, width, height)
        
        for direction in self.DIRECTIONS:
            if direction == self.opposite_direction:
                continue
            if (snake.get_head()[0] + direction[0], snake.get_head()[1] + direction[1]) == next_position:
                self.direction = direction
                break

        self.opposite_direction = self.get_opposite_direction(self.direction)
        return self.direction

    def a_star_search(self, snake: Snake, food_pos: Tuple[int, int], width: int, height: int) -> list:
        """
        Perform A* Search to find the shortest path to the food.

        Args:
            snake (Snake): The snake object.
            food_pos (Tuple[int, int]): The position of the food.
            width (int): The width of the game board.
            height (int): The height of the game board.

        Returns:
            list: A list of positions representing the path to the food.
        """
        start = snake.get_head()
        frontier = PriorityQueue()
        frontier.put((0, start))
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            _, current = frontier.get()

            if current == food_pos:
                break

            for direction in self.DIRECTIONS:
                next_position = (current[0] + direction[0], current[1] + direction[1])
                
                if not snake.check_exist(next_position) and not snake.check_bounds(width, height, next_position):
                    new_cost = cost_so_far[current] + 1
                    if next_position not in cost_so_far or new_cost < cost_so_far[next_position]:
                        cost_so_far[next_position] = new_cost
                        priority = new_cost + self.heuristic(next_position, food_pos)
                        frontier.put((priority, next_position))
                        came_from[next_position] = current

        return self.reconstruct_path(came_from, start, food_pos)

    def reconstruct_path(self, came_from, start, goal):
        """
        Reconstruct the path from start to goal.

        Args:
            came_from (dict): A dictionary mapping positions to their predecessors.
            start (Tuple[int, int]): The start position.
            goal (Tuple[int, int]): The goal position.

        Returns:
            list: A list of positions representing the path from start to goal.
        """
        current = goal
        path = []
        while current != start:
            path.append(current)
            current = came_from.get(current)
            if current is None:
                return []
        path.append(start)
        path.reverse()
        return path

    def find_longest_path(self, snake: Snake, width: int, height: int) -> Tuple[int, int]:
        """
        Find the longest path to cover the remaining space if no path to food is found.

        Args:
            snake (Snake): The snake object.
            width (int): The width of the game board.
            height (int): The height of the game board.

        Returns:
            Tuple[int, int]: The next position in the longest path.
        """
        head = snake.get_head()
        longest_path_direction = None
        max_distance = -1
        
        for direction in self.DIRECTIONS:
            next_position = (head[0] + direction[0], head[1] + direction[1])
            if not snake.check_exist(next_position) and not snake.check_bounds(width, height, next_position):
                distance = self.explore_path(snake, next_position, width, height)
                if distance > max_distance:
                    max_distance = distance
                    longest_path_direction = next_position
        
        return longest_path_direction

    def explore_path(self, snake: Snake, position: Tuple[int, int], width: int, height: int) -> int:
        """
        Explore the path from the given position to estimate the longest path.

        Args:
            snake (Snake): The snake object.
            position (Tuple[int, int]): The starting position.
            width (int): The width of the game board.
            height (int): The height of the game board.

        Returns:
            int: The estimated length of the path.
        """
        visited = set()
        queue = [(position, 0)]
        max_distance = 0
        
        while queue:
            current, distance = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)
            max_distance = max(max_distance, distance)
            
            for direction in self.DIRECTIONS:
                next_position = (current[0] + direction[0], current[1] + direction[1])
                if not snake.check_exist(next_position) and not snake.check_bounds(width, height, next_position):
                    queue.append((next_position, distance + 1))
        
        return max_distance
