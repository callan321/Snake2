import pygame
from main_menu import MainMenu
from play_game import PlayGame
from settings import Settings
import config as g
from config import GameConfig

def calculate_grid_dimensions(number_of_cells: int, config: GameConfig):
    cell_size = min(config.GAME_WIDTH, config.GAME_HEIGHT) // number_of_cells
    width = config.GAME_WIDTH // cell_size
    height = config.GAME_HEIGHT // cell_size
    return width, height, cell_size

def main():
    pygame.init()
    pygame.mixer.init()
    screen_info = pygame.display.Info()
    width, height = screen_info.current_w, screen_info.current_h*14/15
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    config = GameConfig(screen.get_width(), screen.get_height())
    
    
    number_of_cells = 25

    main_menu = MainMenu(screen, config)
    while True:
        choice = main_menu.run()
        if choice == 'play':
            grid_width, grid_height, cell_size = calculate_grid_dimensions(number_of_cells, config)
            game = PlayGame(screen, grid_width, grid_height, cell_size, config)
            if game.run() == 'menu':
                continue
        elif choice == '2 player':
            # Handle 2 player mode
            pass
        elif choice == 'settings':
            settings = Settings(screen, config)
            if settings.run() == 'menu':
                continue
        elif choice == 'replay':
            # Handle replay mode
            pass
        else:
            break

if __name__ == "__main__":
    main()
