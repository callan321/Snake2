import pygame
import globals as g

class BaseController:
    def __init__(self):
        self.current_move = "D"
        self.direction = g.directions[self.current_move]
        self.changed_direction = False

    def handle_keydown(self, event):
        raise NotImplementedError("This method should be overridden by subclasses")

    def reset_changed_direction(self):
        self.changed_direction = False

class ArrowKeyController(BaseController):
    def handle_keydown(self, event):
        new_direction = None
        if event.key == pygame.K_RIGHT and self.current_move != "L":
            new_direction = "R"
        elif event.key == pygame.K_LEFT and self.current_move != "R":
            new_direction = "L"
        elif event.key == pygame.K_DOWN and self.current_move != "U":
            new_direction = "D"
        elif event.key == pygame.K_UP and self.current_move != "D":
            new_direction = "U"

        if new_direction:
            self.current_move = new_direction
            self.direction = g.directions[self.current_move]
            self.changed_direction = True

class WASDController(BaseController):
    def handle_keydown(self, event):
        new_direction = None
        if event.key == pygame.K_d and self.current_move != "L":
            new_direction = "R"
        elif event.key == pygame.K_a and self.current_move != "R":
            new_direction = "L"
        elif event.key == pygame.K_s and self.current_move != "U":
            new_direction = "D"
        elif event.key == pygame.K_w and self.current_move != "D":
            new_direction = "U"

        if new_direction:
            self.current_move = new_direction
            self.direction = g.directions[self.current_move]
            self.changed_direction = True

class CombinedController(BaseController):
    def handle_keydown(self, event):
        new_direction = None
        if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.current_move != "L":
            new_direction = "R"
        elif (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.current_move != "R":
            new_direction = "L"
        elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.current_move != "U":
            new_direction = "D"
        elif (event.key == pygame.K_UP or event.key == pygame.K_w) and self.current_move != "D":
            new_direction = "U"

        if new_direction:
            self.current_move = new_direction
            self.direction = g.directions[self.current_move]
            self.changed_direction = True


class AIController(BaseController):
    def __init__(self):
        super().__init__()

    def update_direction(self, snake_head, food_pos):
        head_x, head_y = snake_head
        if food_pos:
            food_x, food_y = food_pos
        
        else: 
            self.current_move = "D"
            return
        if head_x < food_x:
            new_direction = "R"
        elif head_x > food_x:
            new_direction = "L"
        elif head_y < food_y:
            new_direction = "D"
        elif head_y > food_y:
            new_direction = "U"
        else:
            new_direction = self.current_move

        if self.is_valid_move(new_direction):
            self.current_move = new_direction
            self.direction = g.directions[self.current_move]
            self.changed_direction = True

    def is_valid_move(self, new_direction):
        opposite_directions = {
            "U": "D",
            "D": "U",
            "L": "R",
            "R": "L"
        }
        return opposite_directions[self.current_move] != new_direction