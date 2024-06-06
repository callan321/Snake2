from typing import Tuple, Optional
from game_objects.hash_queue import HashQueue

class Snake:
    def __init__(self, start_pos: Tuple[int, int], size: int = 3):
        self.body: HashQueue[Tuple[int, int]] = HashQueue()
        self.body.add_back(start_pos)
        for _ in range(size - 1):
            self.grow()
        self.last_tail: Optional[Tuple[int, int]] = None
        self.ate = False

    def update(self, direction: Tuple[int, int], food_pos: Tuple[int, int]) -> None:
        self.ate = False
        self.move(direction)
        if self.check_food(food_pos):
            self.grow()
            self.ate = True

    def grow(self) -> None:
        tail_x, tail_y = self.body.peak_back()
        self.body.add_back((tail_x, tail_y))

    def move(self, direction: Tuple[int, int]) -> None:
        x, y = direction
        head_x, head_y = self.get_head()
        new_head: Tuple[int, int] = (head_x + x, head_y + y)
        self.body.add_front(new_head)
        self.last_tail = self.body.pop_back()

    def get_body(self) -> HashQueue:
        return self.body.get_data()

    def get_head(self) -> Tuple[int, int]:
        return self.body.peak_front()

    def check_food(self, food_pos: Tuple[int, int]) -> bool:
        return self.get_head() == food_pos

    def get_size(self) -> int:
        return self.body.get_length()

    def get_last_tail(self) -> Optional[Tuple[int, int]]:
        return self.last_tail

    def check_collision(self, width: int, height: int) -> bool:
        x, y = self.get_head()

        if x < 0 or x >= width or y < 0 or y >= height:
            return True

        if self.get_size() > 4:
            return self.check_self()

        return False

    def check_self(self) -> bool:
        return self.body.check1(self.get_head())

    def check_other(self, pos: Tuple[int, int]) -> bool:
        return self.body.check0(pos)

    def check_ate(self) -> bool:
        return self.ate
