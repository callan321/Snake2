import pygame
import globals as g
from collections import deque
import random
import sys

class HashQueue:
    def __init__(self, positions):
        self.data = deque()
        self.hash_map = {}
        for pos in positions:
            self.hash_map[pos] = 0
        
    def add_front(self, element): 
        self.data.appendleft(element) 
        if element in self.hash_map:
            self.hash_map[element] += 1
        
    def add_back(self, element):
        self.data.append(element)
        if element in self.hash_map:
            self.hash_map[element] += 1
        
    def pop_back(self): 
        element = self.data.pop()
        if element in self.hash_map:
            self.hash_map[element] -= 1
          
    def peak_front(self):
        return self.data[0]
    
    def peak_back(self):
        return self.data[-1]

    def check(self, element): 
        if self.hash_map[element] > 1:
            return True
    
    def get_data(self):
        return self.data
    
class Snake:
    def __init__(self, start_pos, positions, size = 3):
        self.body = HashQueue(positions)
        self.body.add_back(start_pos)
        for _ in range(size-1):
            self.grow()
     
    def update(self, direction, food):
        self.move(direction)  
        if self.check_food(food):  
            self.grow()  
              
    def grow(self):
        tail_x, tail_y = self.body.peak_back()
        self.body.add_back((tail_x, tail_y)) 

    def move(self, direction):
        x, y = g.directions[direction]
        head_x, head_y = self.get_head()
        new_head = (head_x + x, head_y + y)
        self.body.add_front(new_head) 
        self.body.pop_back()

    def get_body(self):
        return self.body.get_data()

    def get_head(self):
        return self.body.peak_front()

    def check_food(self, food):
        return self.get_head() == food.get_position() # Check if the head is at the food position
         
    
    def check_collision(self):
        x, y = self.get_head()

        if x < 0 or x >= g.BOARD_WIDTH or y < 0 or y >= g.BOARD_HEIGHT:
            print("wall")
            return True

        if self.body.check(self.get_head()):
            print("body self")
            return True
        
        return False

def get_board_positions(width, height):
    return {(x, y) for x in range(width) for y in range(height)}  

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
        if available_positions:
            self.pos = random.choice(list(available_positions))
        else:
            self.pos = None
    
    def get_position(self):
        return self.pos
    
    
# Draw snake on screen
def draw_snake(screen, snake):
    for pos in snake.get_body():
        position = (pos[0] * g.CELLSIZE, pos[1] * g.CELLSIZE)
        size = (g.CELLSIZE, g.CELLSIZE)          
        rect = pygame.Rect(position, size) 
        pygame.draw.rect(screen, g.BLACK, rect, border_radius=g.MB_BORDER_RADIUS)

def draw_food(screen, food):
    if not food.get_position():
        return
    x, y = food.get_position()
    position = (x * g.CELLSIZE, y * g.CELLSIZE)
    size = (g.CELLSIZE, g.CELLSIZE)          
    rect = pygame.Rect(position, size) 
    pygame.draw.rect(screen, g.GREEN, rect, border_radius=g.MB_BORDER_RADIUS)
    
# Draw grid on screen
def draw_grid(screen):
    for x in range(0, g.SCREEN_WIDTH, g.CELLSIZE):
        pygame.draw.line(screen, g.GRID_COLOR, (x, 0), (x, g.SCREEN_HEIGHT))      
    for y in range(0, g.SCREEN_HEIGHT, g.CELLSIZE):
        pygame.draw.line(screen, g.GRID_COLOR, (0, y), (g.SCREEN_WIDTH, y))


def get_player_input(last_move):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and last_move != 'D':
                return 'U'
            elif event.key == pygame.K_DOWN and last_move != 'U':
                return 'D'
            elif event.key == pygame.K_LEFT and last_move != 'R':
                return 'L'
            elif event.key == pygame.K_RIGHT and last_move != 'L':
                return 'R'
    
    return last_move

# Initialize Pygame
pygame.init()
game_window = pygame.display.set_mode((g.SCREEN_WIDTH, g.SCREEN_HEIGHT))

positions =  get_board_positions(g.BOARD_WIDTH, g.BOARD_HEIGHT)
last_move = "D"
snake = Snake((5, 5), positions)
food = Food(positions)


# Main game loop
running = True
while running:

    last_move = get_player_input(last_move)
    snake.update(last_move, food)
    food.update(snake)
    
    
    if snake.check_collision():
        sys.exit()
    
    game_window.fill((255, 255, 255)) 
    
    draw_grid(game_window)
    draw_snake(game_window, snake)
    draw_food(game_window, food)
    
    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    fps = pygame.time.Clock()
    fps.tick(5)

pygame.quit()
