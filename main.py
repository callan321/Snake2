import pygame
from interfaces.main_menu import MainMenu
from interfaces.play_game import PlayGame
from interfaces.options import Options
from config.config import GameConfig


def main():
    pygame.init()
    pygame.mixer.init()
    
    try:
        screen_info = pygame.display.Info()
        width, height = screen_info.current_w, int(screen_info.current_h * 14 / 15)
        screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        config = GameConfig(screen.get_width(), screen.get_height(), settings_file='config/settings.json')
    except FileNotFoundError as e:
        print(e)
        return

    main_menu = MainMenu(screen, config)
    while True:
        choice = main_menu.run()
        if choice == 'play':
            config.calculate_grid_dimensions()
            game = PlayGame(screen, config.game_width, config.game_height, config)
            if game.run() == 'menu':
                continue
        elif choice == '2 player':
            # Handle 2 player mode
            pass
        elif choice == 'option':
            settings = Options(screen, config)
            if settings.run() == 'menu':
                # Reload config to reflect changes in settings
                config = GameConfig(screen.get_width(), screen.get_height(), settings_file='config/settings.json')
                continue
        elif choice == 'replay':
            # Handle replay mode
            pass
        else:
            break

if __name__ == "__main__":
    main()
