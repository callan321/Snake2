class GameConfig:
    def __init__(self, base_width=1920, base_height=1080):
        self.base_width = base_width
        self.base_height = base_height
        self.update_config(base_width, base_height)

    def scale_value(self, base_value, base_screen_size, current_screen_size):
        return int(base_value * current_screen_size / base_screen_size)

    def update_config(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        # WINDOW SCALE CONFIG
        self.TASKBAR_HEIGHT = self.scale_value(72, self.base_height, self.screen_height)

        # GAME SCALE CONFIG
        self.BORDER_THICKNESS = self.scale_value(5, self.base_width, self.screen_width)
        self.GAME_WIDTH = self.scale_value(800, self.base_width, self.screen_width)
        self.GAME_HEIGHT = self.scale_value(600, self.base_height, self.screen_height)

        # MENU SCALES
        self.TITLE_Y_OFFSET_MULTIPLIER = 5
        self.BUTTON_Y_OFFSET_MULTIPLIER = 2
        self.BUTTON_Y_OFFSET_SHIFT = 3

        # UI SCALES
        self.SPEED_BUTTON_WIDTH = self.scale_value(150, self.base_width, self.screen_width)
        self.SPEED_BUTTON_PADDING_TOP = self.scale_value(10, self.base_height, self.screen_height)

        # MENU BUTTON SCALE SETTINGS
        self.MB_HEIGHT = self.scale_value(96, self.base_height, self.screen_height)
        self.MB_WIDTH = self.scale_value(440, self.base_width, self.screen_width)  
        self.MB_BORDER_RADIUS = self.scale_value(12, self.base_width, self.screen_width)
        self.BUTTON_Y_OFFSET = self.scale_value(48, self.base_height, self.screen_height)
        self.BUTTON_FONT_SIZE = self.scale_value(72, self.base_height, self.screen_height)
        self.BUTTON_PADDING = self.scale_value(10, self.base_width, self.screen_width)

        # Add other config as necessary
        self.GAME_TITLE = "Snake AI 2"
        self.TITLE_FONT_SIZE = self.scale_value(144, self.base_height, self.screen_height)
        self.TEXT_COLOR = (24, 30, 40)
        self.BACKGROUND_COLOR = (136, 175, 146)

        # Colors and other static configs
        self.BACKGROUND_GREEN = (136, 175, 146)
        self.GREEN_BLACK = (24, 30, 40)
        self.DARK_GREEN = (8, 71, 57)
        self.RED = (191, 47, 55)
        self.GRID_COLOR = self.GREEN_BLACK
        self.GREEN_SNAKE = self.DARK_GREEN
        self.SNAKE_TRANS = 200
        self.FOOD_COLOR = self.RED
        self.BORDER_COLOR = self.GREEN_BLACK
        self.HOVER_SOUND = 'sounds/hover_sound.wav'
        self.CLICK_SOUND = 'sounds/click_sound.wav'
