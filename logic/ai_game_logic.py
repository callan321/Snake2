from logic.game_objects.snake import Snake
from logic.game_objects.food import Food
from logic.game_objects.spawn_generator import SpawnGenerator
from logic.controller.controller import Controller, AIController
from typing import Tuple, Dict
import numpy as np
from collections import deque

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
        reward (float): The cumulative reward for the current game state.
        step_count (int): The number of steps taken in the current game.
        just_ate (bool): Flag indicating if the snake just ate food.
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
        self.reward = 0
        self.step_count = 0
        self.just_ate = False

    def update(self) -> bool:
        """
        Update the game state for the next frame.

        Returns:
            bool: True if the game continues, False if there's a collision.
        """
        self.reward = 0
        self.just_ate = False
        self.update_snake()
        self.update_spawns()
        self.check_food_collision()
        self.update_food()
        self.step_count += 1
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

        # Reward for surviving
        self.reward += 1

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
            self.just_ate = True
            self.reward += 100

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
        if self.snake.check_collision(self.width, self.height):
            self.reward -= 200
            return True
        return False

    def get_game_state(self) -> np.ndarray:
        """
        Get the current state of the game.

        Returns:
            np.ndarray: The game state as a flattened array.
        """
        snake_body = np.array(self.snake.get_body())
        food_position = self.food.get_position()
        head_position = self.snake.get_head()
        
        # Calculate distances to walls
        distance_to_walls = [
            head_position[0],  # Distance to left wall
            self.width - head_position[0] - 1,  # Distance to right wall
            head_position[1],  # Distance to top wall
            self.height - head_position[1] - 1  
        ]
        
        # Calculate distance to food
        distance_to_food = [
            food_position[0] - head_position[0], 
            food_position[1] - head_position[1]   
        ]
        
       
        direction_indicators = [
            1 if self.last_direction == (0, -1) else 0,  
            1 if self.last_direction == (0, 1) else 0,   
            1 if self.last_direction == (-1, 0) else 0,  
            1 if self.last_direction == (1, 0) else 0    
        ]
        
        
        state = np.concatenate((
            snake_body.flatten(),
            np.array(food_position),         
            np.array(distance_to_walls),     
            np.array(distance_to_food),     
            np.array(direction_indicators),  
            np.array([self.width, self.height])  
        ))
        
        return state


    def get_reward(self) -> float:
        """
        Get the current reward for the game state.

        Returns:
            float: The current reward.
        """
        return self.reward

    def is_game_over(self) -> bool:
        """
        Check if the game is over.

        Returns:
            bool: True if the game is over, False otherwise.
        """
        return self.check_collisions()

    def get_just_ate(self) -> bool:
        """
        Check if the snake just ate food.

        Returns:
            bool: True if the snake just ate food, False otherwise.
        """
        return self.just_ate

    def get_snake_head(self) -> Tuple[int, int]:
        """
        Get the position of the snake's head.

        Returns:
            Tuple[int, int]: The position of the snake's head.
        """
        return self.snake.get_head()

    def get_snake_body(self) -> deque:
        """
        Get the positions of the snake's body.

        Returns:
            deque: The positions of the snake's body.
        """
        return self.snake.get_body()
