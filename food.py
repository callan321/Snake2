from typing import Tuple, Dict, List, Optional
from spawn_generator import SpawnGenerator


class Food:
    def __init__(self) -> None:
        self.pos: Tuple[int, int] = None

    def update(self, snake_pos: Tuple[int, int], generator: SpawnGenerator) -> None:
        if self.pos == snake_pos:
            self.pos = None
        if self.pos is None:
            self.respawn(generator.get_random())

    def respawn(self, pos: Tuple[int, int]) -> None:
        self.pos = pos

    def get_position(self) -> Tuple[int, int]:
        return self.pos
