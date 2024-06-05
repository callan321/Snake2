# food.py
import random
class AvailablePositions:
    def __init__(self) -> None:
        pass
    
class Food:
    def __init__(self, positions):
        self.pos = None
        self.positions = positions

    def update(self, snake):
        if self.pos == snake.get_head():
            self.pos = None
        elif self.pos is None:
            self.respawn(snake)

    def respawn(self, snake):
        snake_body_set = set(snake.get_body())
        available_positions = self.positions - snake_body_set
        self.pos = random.choice(list(available_positions)) if available_positions else None

    def get_position(self):
        return self.pos
