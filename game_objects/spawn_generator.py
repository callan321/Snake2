from typing import Tuple, List, Dict, Optional
from random import choice


class SpawnGenerator:
    def __init__(self, width: int, height: int, start_pos: Tuple[int, int]) -> None:
        self.list: List[Tuple[int, int]] = []
        self.map: Dict[Tuple[int, int], int] = {}
        self.init_board(width, height)
        self.remove(start_pos)

    def insert(self, coord: Tuple[int, int]) -> bool:
        if coord is None or coord in self.map:
            return False
        self.map[coord] = len(self.list)
        self.list.append(coord)
        return True

    def remove(self, coord: Tuple[int, int]) -> bool:
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
        coords = [(x, y) for x in range(width) for y in range(height)]
        self.list.extend(coords)
        self.map.update({coord: idx for idx, coord in enumerate(coords)})

    def get_random(self) -> Optional[Tuple[int, int]]:
        if not self.list:
            return None
        return choice(self.list)
