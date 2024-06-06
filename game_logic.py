
from game_objects.snake import Snake
from game_objects.food import Food
from game_objects.spawn_generator import SpawnGenerator
from controller import Controller, AIController


class GameLogic:
    def __init__(self, width, height, controller_type='Combined', snake_size=3):
        adjust_start_x = lambda x: x - 1 if width % 2 == 0 else x
        start_x = adjust_start_x(width // 2)
        start_pos = (start_x, 0)
        self.width, self.height = width, height

        self.snake = Snake(start_pos, snake_size)
        self.spawn_generator = SpawnGenerator(self.width, self.height, start_pos)
        self.food = Food()
        self.controller = Controller.select(controller_type)
        self.running = True

    def update(self):
        if isinstance(self.controller, AIController):
            direction = self.controller.get_direction(self.snake.get_head(), self.food.get_position())
        else:
            direction = self.controller.get_direction()

        self.snake.update(direction, self.food.get_position())
        head_pos = self.snake.get_head()
        tail_pos = self.snake.get_last_tail()

        self.spawn_generator.insert(tail_pos)
        self.spawn_generator.remove(head_pos)

        if self.snake.check_ate():
            self.food.remove()

        if self.food.check_if_despawned():
            self.food.update(self.spawn_generator.get_random())

        if self.snake.check_collision(self.width, self.height):
            self.running = False
