import pygame
import globals as g


class Controller:
    def __init__(self):
        self.current_move = "D"
        self.direction = g.directions[self.current_move]
        
    def handle_keydown(self, event):
        raise NotImplementedError("This method should be overridden by subclasses")

    def get_direction(self):
        return self.direction

    @staticmethod
    def select(controller_type):
        if controller_type == "AI":
            return TESTController()
        elif controller_type == "Arrow":
            return ArrowKeyController()
        elif controller_type == "WASD":
            return WASDController()
        elif controller_type == "Combined":
            return CombinedController()
        else:
            raise ValueError(f"Unknown controller type: {controller_type}")


class HumanController(Controller):
    def __init__(self):
        super().__init__()
        self.changed_direction = False
        
    def get_direction(self):
        self.changed_direction = False
        return self.direction


class AIController(Controller):
    def handle_keydown(self, event):
        pass


class ArrowKeyController(HumanController):
    def handle_keydown(self, event):
        new_direction = None
        if self.changed_direction == False:
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


class WASDController(HumanController):
    def handle_keydown(self, event):
        new_direction = None
        if self.changed_direction == False:
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


class CombinedController(HumanController):
    def handle_keydown(self, event):
        new_direction = None
        if self.changed_direction == False:
            if (
                event.key == pygame.K_RIGHT or event.key == pygame.K_d
            ) and self.current_move != "L":
                new_direction = "R"
            elif (
                event.key == pygame.K_LEFT or event.key == pygame.K_a
            ) and self.current_move != "R":
                new_direction = "L"
            elif (
                event.key == pygame.K_DOWN or event.key == pygame.K_s
            ) and self.current_move != "U":
                new_direction = "D"
            elif (
                event.key == pygame.K_UP or event.key == pygame.K_w
            ) and self.current_move != "D":
                new_direction = "U"

        if new_direction:
            self.current_move = new_direction
            self.direction = g.directions[self.current_move]
            self.changed_direction = True


class TESTController(AIController):
    def __init__(self):
        super().__init__()
        self.current_move = "D"  # Initial direction

    def get_direction(self, snake_head, food_pos):  
        head_x, head_y = snake_head
        
        if food_pos is None:
            self.current_move = "D"
            self.direction = g.directions[self.current_move]
            return self.direction
            
    
        food_x, food_y = food_pos

        
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

   
        self.current_move = new_direction
        self.direction = g.directions.get(self.current_move, (0, 1))  # Default to moving down if direction not found
        return self.direction
