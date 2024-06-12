from typing import Tuple, Optional

class Food:
    """
    A class to manage the food item in the game, including its position and state.
    """

    def __init__(self) -> None:
        """
        Initialize the Food object with no position.
        """
        self.pos: Optional[Tuple[int, int]] = None

    def respawn(self, pos: Optional[Tuple[int, int]]) -> None:
        """
        Respawn the food at the given position.

        :param pos: The position to respawn the food. If None, the food is not placed.
        """
        self.pos = pos

    def get_position(self) -> Optional[Tuple[int, int]]:
        """
        Get the current position of the food.

        :return: The current position of the food, or None if it does not exist.
        """
        return self.pos

    def remove(self) -> None:
        """
        Remove the food from the game, setting its position to None.
        """
        self.pos = None

    def exists(self) -> bool:
        """
        Check if the food currently exists in the game.

        :return: True if the food exists, False otherwise.
        """
        return self.pos is not None
