import pygame
from main_menu import MainMenu
from play_game import PlayGame
from settings import Settings
import globals as g

def calculate_grid_dimensions(number_of_cells):
    cell_size = g.GAME_WIDTH // number_of_cells
    width = g.GAME_WIDTH // cell_size
    height = g.GAME_HEIGHT // cell_size
    return width, height, cell_size

def main():
    pygame.init()
    pygame.mixer.init()
    screen_info = pygame.display.Info()
    width, height = screen_info.current_w, screen_info.current_h
    screen = pygame.display.set_mode((width, height - g.TASKBAR_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption(g.GAME_TITLE)
    number_of_cells = 25

    main_menu = MainMenu(screen)
    while True:
        choice = main_menu.run()
        if choice == 'play':
            grid_width, grid_height, cell_size = calculate_grid_dimensions(number_of_cells)
            game = PlayGame(screen, grid_width, grid_height, cell_size)
            if game.run() == 'menu':
                continue
        elif choice == '2 player':
            # Handle 2 player mode
            pass
        elif choice == 'settings':
            settings = Settings(screen)
            if settings.run() == 'menu':
                continue
        elif choice == 'replay':
            # Handle replay mode
            pass
        else:
            break

if __name__ == "__main__":
    main()
