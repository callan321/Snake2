from logic.game_objects.snake import Snake
from logic.game_objects.food import Food
from logic.game_objects.spawn_generator import SpawnGenerator
from logic.game_objects.snake_spawner import SnakeSpawner
from logic.controller.controller import Controller
from typing import Tuple, List, Deque

class GameLogic:
    """
    Manages the game logic for a snake game controlled by AI.

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
        self, width: int, height: int, controller_type: str = "Greedy", snake_size: int = 3, num_snakes: int = 12
    ) -> None:
        """
        Initialize the game logic with the given parameters.

        Args:
            width (int): The width of the game area.
            height (int): The height of the game area.
            controller_type (str): The type of controller (default is 'AI').
            snake_size (int): The initial size of the snake (default is 3).
            num_snakes (int): The number of snakes in the game (default is 1).
        """
        self.width = width
        self.height = height
        self.spawn_generator = SpawnGenerator(self.width, self.height)
        spawns = SnakeSpawner(width, height , num_snakes).get_spawns()
        self.snakes : List[Snake]= []
        self.controllers: List[Controller] = []

        for i, (start_pos, start_dir) in enumerate(spawns):
            self.snakes.append(Snake(start_pos, snake_size))
            self.spawn_generator.remove(start_pos)
            if i == 0:  # The first two snakes use Human controllers
                self.controllers.append(Controller.select('WASD', start_dir))
            elif i == 1:
                self.controllers.append(Controller.select('Arrow', start_dir))
            else:  # The rest use Greedy controllers
                self.controllers.append(Controller.select('Greedy', start_dir))
        
        
        self.running = True
        self.food = Food()
        self.step_count = 0


    def update(self) -> bool:
        """
        Update the game state for the next frame.

        Returns:
            bool: True if the game continues, False if there's a collision.
        """
        self.step_count += 1
        for snake in self.snakes:
            snake.ate = False  # Reset the just_ate flag for each snake
            
        i = 0
        while i < len(self.snakes):
            snake = self.snakes[i]
            self.update_snake(i, snake)

            self.update_spawns(snake)
            self.check_food_collision(snake)
            self.update_food()

            if not snake.check_exists():
                self.snakes.pop(i)
                self.controllers.pop(i)
            else:
                if snake.check_alive():
                    self.check_collisions(snake)
                i += 1

        return self.running

    def update_snake(self, snake_id: int, snake: 'Snake') -> None:
        """
        Update the snake's position based on the direction.
        """
        direction = self.controllers[snake_id].get_direction(
            snake, self.food.get_position(), self.width, self.height, self.snakes
        )
        snake.update(direction, self.food.get_position())



    def update_spawns(self, snake: Snake) -> None:
        """
        Update the spawn generator.
        """
        head_pos = snake.get_head()
        tail_pos = snake.get_last_tail()
        self.spawn_generator.update(head_pos, tail_pos)


    def check_food_collision(self, snake: Snake) -> None:
        """
        Check if the snake has eaten the food.
        """
        if snake.check_ate():
            self.food.remove()

    def update_food(self) -> None:
        """
        Update the food's position if it has been eaten or despawned.
        """
        if not self.food.exists():
            new_food_position = self.spawn_generator.get_random()
            self.food.respawn(new_food_position)

    def check_collisions(self, snake: Snake) -> bool:
        """
        Check for collisions with the walls or the snake itself.

        Returns:
            bool: True if there is a collision, False otherwise.
        """
        
             
        return snake.check_collision(self.width, self.height, self.snakes)

    def get_snake_just_ate(self) -> bool:
        """
        Check if any snake just ate food.

        Returns:
            bool: True if any snake just ate food, False otherwise.
        """
        return any(snake.check_ate() for snake in self.snakes)

    def get_step_count(self) -> int:
        """
        Get the number of steps taken in the current game.

        Returns:
            int: The number of steps taken.
        """
        return self.step_count

    def get_snake_head(self, snake_id: int) -> Tuple[int, int]:
        """
        Get the position of the snake's head.

        Args:
            snake_id (int): The ID of the snake.

        Returns:
            Tuple[int, int]: The position of the snake's head.
        """
        return self.snakes[snake_id].get_head()

    def get_snake_body(self, snake_id: int) -> Deque[Tuple[int, int]]:
        """
        Get the positions of the snake's body.

        Args:
            snake_id (int): The ID of the snake.

        Returns:
            Deque[Tuple[int, int]]: The positions of the snake's body.
        """
        return self.snakes[snake_id].get_body()

    def get_food_position(self) -> Tuple[int, int]:
        """
        Get the position of the food.

        Returns:
            Tuple[int, int]: The position of the food.
        """
        return self.food.get_position()

    def get_snake_body_and_direction(self, snake_id: int) -> Tuple[Deque[Tuple[int, int]], Tuple[int, int]]:
        """
        Get the body and the direction of the snake controlled by the specified controller.

        Args:
            snake_id (int): The ID of the snake.

        Returns:
            Tuple[Deque[Tuple[int, int]], Tuple[int, int]]: The body of the snake and the direction of the controller.
        """
        snake_body = self.get_snake_body(snake_id)
        snake_direction = self.controllers[snake_id].get_current_direction()
        return snake_body, snake_direction

    def get_controller(self, snake_id: int) -> Controller:
        """
        Get the controller for the specified snake.

        Args:
            snake_id (int): The ID of the snake.

        Returns:
            Controller: The controller for the specified snake.
        """
        if snake_id < 0 or snake_id >= len(self.controllers):
            self.running = False
            return
        return self.controllers[snake_id]

    def get_snake_count(self) -> int:
        """
        Get the number of snakes in the game.

        Returns:
            int: The number of snakes.
        """
        return len(self.snakes)
