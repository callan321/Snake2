from typing import Tuple, Optional, Deque, List
from logic.game_objects.hash_queue import HashQueue

from typing import Tuple, Optional, Deque, List, Dict

class Snake:
    """
    A class representing the snake in the game, managing its movement, growth, and collision detection.
    """

    def __init__(self, start_pos: Tuple[int, int], size: int = 3) -> None:
        """
        Initialize the snake with a starting position and initial size.

        :param start_pos: The starting position of the snake's head.
        :param size: The initial size of the snake.
        """
        self.body: HashQueue[Tuple[int, int]] = HashQueue()
        self.body.add_back(start_pos)
        for _ in range(size - 1):
            self.grow()
        self.last_tail: Optional[Tuple[int, int]] = None
        self.ate: bool = False
        self.alive: bool = True
        self.exists: bool = True

    def update(self, direction: Tuple[int, int], food_pos: Tuple[int, int]) -> None:
        """
        Update the snake's position based on the direction and check if it eats the food.

        :param direction: The direction in which the snake moves.
        :param food_pos: The position of the food.
        """
        self.ate = False
        if not self.alive:
            return self.remove_tail_dead()
        self.move(direction)
        if self.check_food(food_pos):
            self.grow()
            self.ate = True

    def grow(self) -> None:
        """
        Grow the snake by adding a segment to its body.
        """
        tail_x, tail_y = self.body.peak_back()
        self.body.add_back((tail_x, tail_y))

    def move(self, direction: Tuple[int, int]) -> None:
        """
        Move the snake in the given direction.

        :param direction: The direction in which the snake moves.
        """
        self.add_head(direction)
        self.remove_tail()

    def add_head(self, direction: Tuple[int, int]) -> None:
        """
        Add a new head to the snake in the given direction.

        :param direction: The direction in which the snake moves.
        """
        x, y = direction
        head_x, head_y = self.get_head()
        new_head: Tuple[int, int] = (head_x + x, head_y + y)
        self.body.add_front(new_head)

    def remove_tail(self) -> None:
        """
        Remove the tail of the snake.
        """
        self.last_tail = self.body.pop_back()
        if self.check_position_exists(self.last_tail):
            self.last_tail = None

    def remove_tail_dead(self) -> None:
        """
        Remove the tail of the dead snake.
        """
        self.remove_tail()
        if self.get_size() <= 0:
            self.exists = False

    def remove_head(self) -> None:
        """
        Remove the head of the snake.
        """
        self.body.pop_front()
        if self.get_size() <= 0:
            self.exists = False

    def get_body(self) -> Deque[Tuple[int, int]]:
        """
        Get the current body of the snake.

        :return: The body of the snake as a deque of positions.
        """
        return self.body.get_data()

    def get_head(self) -> Tuple[int, int]:
        """
        Get the current head position of the snake.

        :return: The position of the snake's head.
        """
        return self.body.peak_front()

    def check_food(self, food_pos: Tuple[int, int]) -> bool:
        """
        Check if the snake's head is at the food position.

        :param food_pos: The position of the food.
        :return: True if the snake's head is at the food position, False otherwise.
        """
        return self.get_head() == food_pos

    def get_size(self) -> int:
        """
        Get the current size of the snake.

        :return: The size of the snake.
        """
        return self.body.get_length()

    def get_last_tail(self) -> Optional[Tuple[int, int]]:
        """
        Get the last tail position of the snake.

        :return: The last tail position of the snake, or None if it hasn't moved.
        """
        return self.last_tail



    def check_collision(
        self, width: int, height: int, snakes: Dict[int, 'Snake'], keys: List[int]
    ) -> bool:
        """
        Check if the snake has collided with the walls or itself.

        :param width: The width of the game area.
        :param height: The height of the game area.
        :param snakes: Dictionary of snakes in the game.
        :param keys: List of keys to look up the snakes.
        :return: True if the snake has collided, False otherwise.
        """
        head = self.get_head()
        for key in keys:
            snake = snakes[key]
            if snake and snake is not self and snake.check_position_exists(head):
                self.die()
                return True
        if self.check_bounds(width, height, head):
            self.die()
            return True
        if self.check_self():
            self.die()
            return True
        return False


    def die(self) -> None:
        """
        Mark the snake as dead and remove its head.
        """
        self.alive = False
        self.remove_head()

    def check_bounds(self, width: int, height: int, pos: Tuple[int, int]) -> bool:
        """
        Check if the position is out of the game bounds.

        :param width: The width of the game area.
        :param height: The height of the game area.
        :param pos: The position to check.
        :return: True if the position is out of bounds, False otherwise.
        """
        x, y = pos
        return x < 0 or x >= width or y < 0 or y >= height

    def check_self(self) -> bool:
        """
        Check if the snake has collided with itself.

        :return: True if the snake has collided with itself, False otherwise.
        """
        return self.body.has_multi(self.get_head())

    def check_position_exists(self, pos: Tuple[int, int]) -> bool:
        """
        Check if the position exists in the snake's body.

        :param pos: The position to check.
        :return: True if the position exists in the snake's body, False otherwise.
        """
        return self.body.has_one(pos)

    def check_ate(self) -> bool:
        """
        Check if the snake has just eaten food.

        :return: True if the snake has just eaten food, False otherwise.
        """
        return self.ate

    def check_alive(self) -> bool:
        """
        Check if the snake is alive.

        :return: True if the snake is alive, False otherwise.
        """
        return self.alive

    def check_exists(self) -> bool:
        """
        Check if the snake exists.

        :return: True if the snake exists, False otherwise.
        """
        return self.exists

    def __str__(self) -> str:
        """
        Return a string representation of the Snake.

        :return: A string representing the Snake.
        """
        return f"Snake(body={self.body}, alive={self.alive}, ate={self.ate}, exists={self.exists})"

    def __repr__(self) -> str:
        """
        Return a string representation of the Snake.

        :return: A string representing the Snake.
        """
        return self.__str__()

