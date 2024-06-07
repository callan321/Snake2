import json
import os

class GameConfig:
    def __init__(self, screen_width, screen_height, settings_file='config/settings.json'):
        self.settings = self.load_settings(settings_file)
        self.base_width = self.settings['base_width']
        self.base_height = self.settings['base_height']
        self.update_config(screen_width, screen_height)
        self.number_of_cells = self.settings.get("number_of_cells", 55)

    def load_settings(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Settings file '{file_path}' not found. Please ensure the settings file exists.")
        
        with open(file_path, 'r') as file:
            return json.load(file)

    def save_settings(self, file_path='config/settings.json'):
        with open(file_path, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def scale_value(self, base_value, base_screen_size, current_screen_size):
        return int(base_value * current_screen_size / base_screen_size)

    def update_config(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        # WINDOW SCALE CONFIG
        self.TASKBAR_HEIGHT = self.scale_value(self.settings['TASKBAR_HEIGHT'], self.base_height, self.screen_height)

        # GAME SCALE CONFIG
        self.BORDER_THICKNESS = self.scale_value(self.settings['BORDER_THICKNESS'], self.base_width, self.screen_width)
        self.GAME_WIDTH = self.scale_value(self.settings['GAME_WIDTH'], self.base_width, self.screen_width)
        self.GAME_HEIGHT = self.scale_value(self.settings['GAME_HEIGHT'], self.base_height, self.screen_height)

        # MENU SCALES
        self.TITLE_Y_OFFSET_MULTIPLIER = self.settings['TITLE_Y_OFFSET_MULTIPLIER']
        self.BUTTON_Y_OFFSET_MULTIPLIER = self.settings['BUTTON_Y_OFFSET_MULTIPLIER']
        self.BUTTON_Y_OFFSET_SHIFT = self.settings['BUTTON_Y_OFFSET_SHIFT']

        # UI SCALES
        self.SPEED_BUTTON_WIDTH = self.scale_value(self.settings['SPEED_BUTTON_WIDTH'], self.base_width, self.screen_width)
        self.SPEED_BUTTON_PADDING_TOP = self.scale_value(self.settings['SPEED_BUTTON_PADDING_TOP'], self.base_height, self.screen_height)

        # MENU BUTTON SCALE SETTINGS
        self.MB_HEIGHT = self.scale_value(self.settings['MB_HEIGHT'], self.base_height, self.screen_height)
        self.MB_WIDTH = self.scale_value(self.settings['MB_WIDTH'], self.base_width, self.screen_width)
        self.MB_BORDER_RADIUS = self.scale_value(self.settings['MB_BORDER_RADIUS'], self.base_width, self.screen_width)
        self.BUTTON_Y_OFFSET = self.scale_value(self.settings['BUTTON_Y_OFFSET'], self.base_height, self.screen_height)
        self.BUTTON_FONT_SIZE = self.scale_value(self.settings['BUTTON_FONT_SIZE'], self.base_height, self.screen_height)
        self.BUTTON_PADDING = self.scale_value(self.settings['BUTTON_PADDING'], self.base_width, self.screen_width)
        self.BUTTON_WIDTH = self.scale_value(self.settings['BUTTON_WIDTH'], self.base_width, self.screen_width)
        
        # Add other config as necessary
        self.GAME_TITLE = self.settings['GAME_TITLE']
        self.TITLE_FONT_SIZE = self.scale_value(self.settings['TITLE_FONT_SIZE'], self.base_height, self.screen_height)
        self.TEXT_COLOR = tuple(self.settings['TEXT_COLOR'])
        self.BACKGROUND_COLOR = tuple(self.settings['BACKGROUND_COLOR'])

        # Colors and other static configs
        self.BACKGROUND_GREEN = tuple(self.settings['BACKGROUND_GREEN'])
        self.GREEN_BLACK = tuple(self.settings['GREEN_BLACK'])
        self.DARK_GREEN = tuple(self.settings['DARK_GREEN'])
        self.RED = tuple(self.settings['RED'])
        self.GRID_COLOR = tuple(self.settings['GRID_COLOR'])
        self.GREEN_SNAKE = tuple(self.settings['GREEN_SNAKE'])
        self.SNAKE_TRANS = self.settings['SNAKE_TRANS']
        self.FOOD_COLOR = tuple(self.settings['FOOD_COLOR'])
        self.BORDER_COLOR = tuple(self.settings['BORDER_COLOR'])
        self.HOVER_SOUND = self.settings['HOVER_SOUND']
        self.CLICK_SOUND = self.settings['CLICK_SOUND']

    def calculate_grid_dimensions(self, number_of_cells):
        cell_size = min(self.GAME_WIDTH, self.GAME_HEIGHT) // number_of_cells
        width = self.GAME_WIDTH // cell_size
        height = self.GAME_HEIGHT // cell_size
        return width, height, cell_size
