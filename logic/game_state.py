import numpy as np
from typing import Tuple, Any
from collections import deque

class GameState:
    """
    Manages the state of the game, including rewards, step count, food consumption status,
    and assembling the game state for AI training.
    """

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.reward: float = 0
        self.step_count: int = 0
        self.just_ate: bool = False

    def reset(self) -> None:
        """Reset the game state."""
        self.reward = 0
        self.just_ate = False

    def increment_step(self) -> None:
        """Increment the step count."""
        self.step_count += 1

    def update_reward(self, value: float) -> None:
        """Update the reward value."""
        self.reward += value

    def set_just_ate(self, value: bool) -> None:
        """Set the just_ate flag."""
        self.just_ate = value

    def get_reward(self) -> float:
        """Get the current reward."""
        return self.reward

    def get_just_ate(self) -> bool:
        """Check if the snake just ate food."""
        return self.just_ate

    def assemble_game_state(self, snake_body: deque, food_position: Tuple[int, int], 
                            last_direction: Tuple[int, int], opposite_direction: Tuple[int, int]) -> np.ndarray:
        """
        Get the current state of the game.

        Returns:
            np.ndarray: The game state as a flattened array.
        """
        snake_body = np.array(snake_body)
        food_position = np.array(food_position)
        head_position = snake_body[0]

        # Calculate distance to food
        distance_to_food = [
            food_position[0] - head_position[0],
            food_position[1] - head_position[1],
        ]

        direction_indicators = [
            1 if last_direction == (0, -1) else 0,
            1 if last_direction == (0, 1) else 0,
            1 if last_direction == (-1, 0) else 0,
            1 if last_direction == (1, 0) else 0,
        ]

        opposite_direction_indicators = [
            1 if opposite_direction == (0, -1) else 0,
            1 if opposite_direction == (0, 1) else 0,
            1 if opposite_direction == (-1, 0) else 0,
            1 if opposite_direction == (1, 0) else 0,
        ]

        state = np.concatenate(
            (
                snake_body.flatten(),
                food_position,
                np.array(distance_to_food),
                np.array(direction_indicators),
                np.array(opposite_direction_indicators),
                np.array([self.width, self.height]),
            )
        )

        return state
