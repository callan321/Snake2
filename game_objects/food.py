from typing import Tuple, Optional

class Food:
    def __init__(self) -> None:
        self.pos: Optional[Tuple[int, int]] = None

    def update(self, pos) -> None:
        if self.pos is None:
            self.respawn(pos)

    def respawn(self, pos: Optional[Tuple[int, int]]) -> None:
        self.pos = pos

    def get_position(self) -> Optional[Tuple[int, int]]:
        return self.pos

    def remove(self) -> None:
        self.pos = None

    def check_if_despawned(self) -> bool:
        return self.pos is None
