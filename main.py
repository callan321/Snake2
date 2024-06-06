import pygame
from main_menu import MainMenu
from play_game import PlayGame
from settings import Settings
import globals as g
from sounds.load_sounds import load_sounds

def main():
    pygame.init()
    screen_info = pygame.display.Info()
    width, height = screen_info.current_w, screen_info.current_h
    screen = pygame.display.set_mode((width, height - g.TASKBAR_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption(g.GAME_TITLE)
    
    # Load sounds
    sounds = load_sounds()
    
    main_menu = MainMenu(screen, sounds)
    while True:
        choice = main_menu.run()
        if choice == 'play':
            number_of_cells = 20
            cell_size = g.GAME_WIDTH // number_of_cells
            width = g.GAME_WIDTH // cell_size
            height = g.GAME_HEIGHT // cell_size
            game = PlayGame(screen, width, height, cell_size, sounds)
            if game.run() == 'menu':
                continue
        elif choice == '2player':
            # Handle 2 player mode
            game = PlayGame(screen)
            if game.run() == 'menu':
                continue
        elif choice == 'settings':
            settings = Settings(screen)
            if settings.run() == 'menu':
                continue
        elif choice == 'replay':
            # Handle replay functionality
            # Add your replay logic here
            pass
        else:
            break
    
if __name__ == "__main__":
    main()
