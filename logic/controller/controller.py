from typing import Tuple
from abc import abstractclassmethod
class Controller:
    """
    Base class for all controllers.

    Attributes:
        direction (Tuple[int, int]): The current direction of movement.
        opposite_direction (Tuple[int, int]): The opposite direction of the last movement.
    """

    # Direction constants
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    # Directions as tuples
    DIRECTIONS = [
        (0, -1),  # UP
        (0, 1),   # DOWN
        (-1, 0),  # LEFT
        (1, 0)    # RIGHT
    ]

    def __init__(self, starting_direction) -> None:
        """
        Initialize the Controller with a default direction.

        Args:
            starting_direction (Tuple[int, int]): The initial direction of the controller.
        """
        self.direction = starting_direction
        self.opposite_direction = self.get_opposite_direction(starting_direction)

   
    def get_direction(self) -> Tuple[int, int]:
        """
        Return the current direction.

        Returns:
            Tuple[int, int]: The current direction as (x, y) coordinates.
        """
        raise NotImplementedError("This method must be implemented") 
        
    
    def get_current_direction(self):
        return self.direction
        

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

    @staticmethod
    def select(controller_type: str, starting_direction) -> "Controller":
        """
        Select and return the appropriate controller based on type.

        Args:
            controller_type (str): The type of controller to select.

        Returns:
            Controller: An instance of the selected controller type.

        Raises:
            ValueError: If the controller type is unknown.
        """
        if controller_type == "Greedy":
            from logic.controller.greedy_controller import GreedyController
            return GreedyController(starting_direction)
        elif controller_type == "Arrow":
            from logic.controller.human_controllers import ArrowKeyController
            return ArrowKeyController(starting_direction)
        elif controller_type == "WASD":
            from logic.controller.human_controllers import WASDController
            return WASDController(starting_direction)
        elif controller_type == "Human":
            from logic.controller.human_controllers import CombinedController
            return CombinedController(starting_direction)
        else:
            raise ValueError(f"Unknown controller type: {controller_type}")
