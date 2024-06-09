import json
import os

class GameConfig:
    def __init__(self, screen_width, screen_height, settings_file='config/settings.json'):
        self.settings_file = settings_file
        self.settings = self.load_settings(settings_file)
        self.BASE_SCREEN_WIDTH = self.settings['base_sacles']['SCREEN_WIDTH']
        self.BASE_SCREEN_HEIGHT = self.settings['base_sacles']['SCREEN_HEIGHT']
        
        self.number_of_cells = self.settings['game_settings'].get("number_of_cells", 20)
        self.snake_size = self.settings['game_settings'].get("snake_size", 2)
        self.game_speed = self.settings['game_settings'].get("game_speed", 1)
        self.cell_size = 0
        
        self.update_config(screen_width, screen_height)

    def load_settings(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Settings file '{file_path}' not found. Please ensure the settings file exists.")
        
        with open(file_path, 'r') as file:
            return json.load(file)

    def update_speed(self):
        self.game_speed = self.settings['game_settings'].get("game_speed", 10)
        
    def save_settings(self):
        with open(self.settings_file, 'w') as file:
            json.dump(self.settings, file, indent=4)

    
    def scale_value(self, base_value, new_screen_width, new_screen_height):
        width_scale = new_screen_width / self.BASE_SCREEN_WIDTH
        height_scale = new_screen_height / self.BASE_SCREEN_HEIGHT
        
        min_scale = min(width_scale, height_scale)
        
        scaled_value = base_value * min_scale
        return int(scaled_value)
    
    def update_config(self, screen_width, screen_height):

        # GAME SCALE CONFIG
        game_scales = self.settings['game_scales']
        self.BORDER_THICKNESS = self.scale_value(game_scales['BORDER_THICKNESS'], screen_width, screen_height)
        self.GAME_WIDTH = self.scale_value(game_scales['GAME_WIDTH'], screen_width, screen_height)
        self.GAME_HEIGHT = self.scale_value(game_scales['GAME_HEIGHT'], screen_width, screen_height)
        
        # speed button
        speed_button = game_scales['speed_button']
        self.SB_WIDTH = self.scale_value(speed_button['SB_WIDTH'], screen_width, screen_height)
        self.SB_HEIGHT = self.scale_value(speed_button['SB_HEIGHT'], screen_width, screen_height)
        self.SB_BORDER_RADIUS = self.scale_value(speed_button['SB_BORDER_RADIUS'], screen_width, screen_height)
        self.SB_FONT_SIZE = self.scale_value(speed_button['SB_FONT_SIZE'], screen_width, screen_height)
        
        # MENU SCALES
        menu_scales = self.settings['menu_scales']
        self.TITLE_Y_OFFSET_MULTIPLIER = menu_scales['TITLE_Y_OFFSET_MULTIPLIER']
        self.TITLE_FONT_SIZE = self.scale_value(menu_scales['TITLE_FONT_SIZE'], screen_width, screen_height)
        self.MB_Y_OFFSET = self.scale_value(menu_scales['MB_Y_OFFSET'], screen_width, screen_height)
        
        # menu button
        menu_buttons = menu_scales['menu_button']
        self.MB_WIDTH = self.scale_value(menu_buttons['MB_WIDTH'], screen_width, screen_height)
        self.MB_HEIGHT = self.scale_value(menu_buttons['MB_HEIGHT'], screen_width, screen_height)
        self.MB_BORDER_RADIUS = self.scale_value(menu_buttons['MB_BORDER_RADIUS'], screen_width, screen_height)
        self.BUTTON_FONT_SIZE = self.scale_value(menu_buttons['MB_FONT_SIZE'], screen_width, screen_height)
        
        # game size buttons
        game_size_buttons = menu_scales['game_size_button']
        self.GS_FONT_SIZE = self.scale_value(game_size_buttons['GS_FONT_SIZE'], screen_width, screen_height)
        self.GS_BUTTON_HEIGHT = self.scale_value(game_size_buttons['GS_BUTTON_HEIGHT'], screen_width, screen_height)
        self.GS_BUTTON_WIDTH = self.scale_value(game_size_buttons['GS_BUTTON_WIDTH'], screen_width, screen_height)
        self.GS_BORDER_RADIUS = self.scale_value(game_size_buttons['GS_BORDER_RADIUS'], screen_width, screen_height)


        self.GAME_SIZE_BUTTONS = game_size_buttons['BUTTONS']

        # globals
        globals = self.settings['globals']
        self.MENU = globals['MENU']
        self.PLAY = globals['PLAY']
        self.PLAY2 = globals['PLAY2']
        self.OPTIONS = globals['OPTIONS']
        self.REPLAY = globals['REPLAY']
        self.QUIT = globals['QUIT']
        self.FPS = globals["FPS"]
        self.BACK = globals["BACK"]
        
        # menu 
        menu_text = self.settings['menu_text']
        self.GAME_TITLE = menu_text['GAME_TITLE']
    
        # colors
        colors = self.settings['colors']
        self.TEXT_COLOR = tuple(colors['TEXT_COLOR'])
        self.BACKGROUND_COLOR = tuple(colors['BACKGROUND_COLOR'])
        self.BACKGROUND_GREEN = tuple(colors['BACKGROUND_GREEN'])
        self.GREEN_BLACK = tuple(colors['GREEN_BLACK'])
        self.DARK_GREEN = tuple(colors['DARK_GREEN'])
        self.RED = tuple(colors['RED'])
        self.GRID_COLOR = tuple(colors['GRID_COLOR'])
        self.GREEN_SNAKE = tuple(colors['GREEN_SNAKE'])
        self.FOOD_COLOR = tuple(colors['FOOD_COLOR'])
        self.BORDER_COLOR = tuple(colors['BORDER_COLOR'])
        self.SNAKE_TRANS = colors['SNAKE_TRANS']
        
        sounds = self.settings['sounds']
        self.HOVER_SOUND = sounds['HOVER_SOUND']
        self.CLICK_SOUND = sounds['CLICK_SOUND']

        self.calculate_grid_dimensions()

        
        
    def calculate_grid_dimensions(self):
        self.cell_size = min(self.GAME_WIDTH, self.GAME_HEIGHT) // self.number_of_cells
        self.game_width = self.GAME_WIDTH // self.cell_size
        self.game_height = self.GAME_HEIGHT // self.cell_size
        