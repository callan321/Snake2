import json
import os

class GameConfig:
    def __init__(self, screen_width, screen_height, settings_file='config/settings.json'):
        self.settings_file = settings_file
        self.settings = self.load_settings(settings_file)
        self.BASE_SCREEN_WIDTH = self.settings['base_sacles']['SCREEN_WIDTH']
        self.BASE_SCREEN_HEIGHT = self.settings['base_sacles']['SCREEN_HEIGHT']
        self.load_attributes()
        self.load_options()
        self.load_constants()
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

    def load_attributes(self):
        self.number_of_cells = self.settings['attributes']["number_of_cells"]
        self.snake_size = self.settings['attributes']["snake_size"]
        self.game_speed = self.settings['attributes']["game_speed"]
        self.game_speed_mult = self.settings['attributes']["game_speed_mult"]
        self.p1 = self.settings['attributes']["p1"]
        
    def load_options(self):
        self.GSPEEDS =  self.settings["GSPEEDS"]
        self.CONTROLLER_TYPES = self.settings["CONTROLLER_TYPES"]
        self.GAME_SPEED_MULT_OPT = self.settings["GAME_SPEED_MULT_OPT"]
        self.GAME_SIZE_BUTTONS = self.settings['MAPS']
    
    def set_attribute(self, attribute_name, new_value):
        getattr(self, attribute_name)
        self.settings['attributes'][attribute_name] = new_value
        self.save_settings()
        setattr(self, attribute_name, new_value)
 
    def scale_value(self, base_value):
        width_scale = self.new_screen_width / self.BASE_SCREEN_WIDTH
        height_scale = self.new_screen_height / self.BASE_SCREEN_HEIGHT
        
        min_scale = min(width_scale, height_scale)
        
        scaled_value = base_value * min_scale
        return int(scaled_value)
    
    def update_config(self, screen_width, screen_height):
        self.new_screen_width = screen_width
        self.new_screen_height = screen_height
        
        # GAME SCALE CONFIG
        game_scales = self.settings['game_scales']
        self.BORDER_THICKNESS = self.scale_value(game_scales['BORDER_THICKNESS'])
        self.GAME_WIDTH = self.scale_value(game_scales['GAME_WIDTH'])
        self.GAME_HEIGHT = self.scale_value(game_scales['GAME_HEIGHT'])
        
        # buttons
        button_scales = self.settings['buttons']
        self.std_width = self.scale_value(button_scales['STD_WIDTH'])
        self.std_height = self.scale_value(button_scales['STD_HEIGHT'])
        self.std_br = self.scale_value(button_scales['STD_BR'])
        self.sm_width = self.scale_value(button_scales['SM_WIDTH'])
        self.sm_br = self.scale_value(button_scales['SM_BR'])
        self.lg_width = self.scale_value(button_scales['LG_WIDTH'])
        
        # MENU SCALES
        other = self.settings['other']
        self.std_f_size = other['STD_F_SIZE']
        self.tital_f_size = self.scale_value(other['TITLE_F_SIZE'])
     
        self.calculate_grid_dimensions()

              
    def calculate_grid_dimensions(self):
        self.cell_size = min(self.GAME_WIDTH, self.GAME_HEIGHT) // self.number_of_cells
        self.game_width = self.GAME_WIDTH // self.cell_size
        self.game_height = self.GAME_HEIGHT // self.cell_size
        
    def load_constants(self):  
        
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
        menu_text = self.settings['text']
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
        
        #sounds
        sounds = self.settings['sounds']
        self.HOVER_SOUND = sounds['HOVER_SOUND']
        self.CLICK_SOUND = sounds['CLICK_SOUND']