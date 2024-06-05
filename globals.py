# 9, 10, 11, 12, 13, 14, 18, 24, 36, 48, 64, 72, 96, 144, 288
# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TASKBAR_HEIGHT = 72  # Height of the taskbar

# common factors 1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 200
NUMBER_OF_CELLS = 50

CELLSIZE = 40
CELLSIZE = min(SCREEN_WIDTH, SCREEN_HEIGHT) // NUMBER_OF_CELLS
BOARD_WIDTH = SCREEN_WIDTH // CELLSIZE
BOARD_HEIGHT = SCREEN_HEIGHT // CELLSIZE
SNAKE_BORDER_RADIUS = CELLSIZE // 3
# Game settings
GAME_TITLE = 'Snake 2'


# Main Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


BACKGROUND_COLOR = (136, 175, 146)
GREEN_BLACK = (24, 30, 40) 
TRANSPARENT = (0, 0, 0, 0)
GRID_COLOR = GREEN_BLACK

# Inhereted Colors
GREEN_SNAKE = (8, 71, 57)

TITLE_COLOR = GREEN_BLACK
BORDER_COLOR = GREEN_BLACK  
FOOD_COLOR = (191, 47, 55)

MB_BG_COLOR = BACKGROUND_COLOR
MB_T_COLOR = GREEN_BLACK
MB_HBG_COLOR = GREEN_BLACK
MB_HT_COLOR = BACKGROUND_COLOR

MB_HEIGHT = 72
MB_WIDTH = 244
MB_BORDER_RADIUS = 12

FOOD_BORDER_RADIUS = 12
FOOD_SIZE = CELLSIZE // 6
TITAL_FONT_SIZE =  144


# Button settings
BUTTON_Y_OFFSET = 48
BUTTON_FONT_SIZE = 72
BUTTON_PADDING = 10

# Border settings
BORDER_THICKNESS = 5
BORDER_RECT_WIDTH = 800
BORDER_RECT_HEIGHT = 600

# Direction mappings
directions = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0)
}
