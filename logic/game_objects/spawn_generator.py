from typing import Tuple, List, Dict, Optional
from random import choice


class SpawnGenerator:
    """
    A class to manage the generation and removal of spawn points on a game board.
    """

    def __init__(self, width: int, height: int, start_pos: Tuple[int, int]) -> None:
        """
        Initialize the spawn generator with a board of given width and height,
        and remove the starting position from the available spawn points.

        :param width: The width of the game board.
        :param height: The height of the game board.
        :param start_pos: The starting position to be removed from spawn points.
        """
        self.list: List[Tuple[int, int]] = []
        self.map: Dict[Tuple[int, int], int] = {}
        self.init_board(width, height)
        self.remove(start_pos)

    def insert(self, coord: Tuple[int, int]) -> bool:
        """
        Insert a coordinate into the available spawn points.

        :param coord: The coordinate to insert.
        :return: True if the coordinate was inserted, False if it was already present.
        """
        if coord is None or coord in self.map:
            return False
        self.map[coord] = len(self.list)
        self.list.append(coord)
        return True

    def remove(self, coord: Tuple[int, int]) -> bool:
        """
        Remove a coordinate from the available spawn points.

        :param coord: The coordinate to remove.
        :return: True if the coordinate was removed, False if it was not present.
        """
        if coord not in self.map:
            return False
        idx = self.map[coord]
        last_element = self.list[-1]
        self.list[idx] = last_element
        self.map[last_element] = idx
        self.list.pop()
        del self.map[coord]
        return True

    def init_board(self, width: int, height: int) -> None:
        """
        Initialize the game board with all possible spawn points.

        :param width: The width of the game board.
        :param height: The height of the game board.
        """
        coords = [(x, y) for x in range(width) for y in range(height)]
        self.list.extend(coords)
        self.map.update({coord: idx for idx, coord in enumerate(coords)})

    def get_random(self) -> Optional[Tuple[int, int]]:
        """
        Get a random coordinate from the available spawn points.

        :return: A random coordinate, or None if no spawn points are available.
        """
        if not self.list:
            return None
        return choice(self.list)
