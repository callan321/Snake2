import pygame
from interfaces.main_menu import MainMenu
from interfaces.play_game import PlayGame
from interfaces.options import Options
from config.config import GameConfig


# fix even handling for button clicks main menu
# make buttons more efficient 
  
# improve game logic
# fix bug where food can spawn under snake on first scale
# make so game only allows for valid moves
# return vales in logic
# add sound to game

def main() -> None:
    """Main function to initialize thex game and handle the main menu loop."""
    pygame.init()
    pygame.mixer.init()

    try:
        # Get screen dimensions and set up the display
        screen_info = pygame.display.Info()
        width, height = screen_info.current_w, int(screen_info.current_h * 14 / 15)
        screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        # Load game configuration
        config = GameConfig(
            screen.get_width(),
            screen.get_height(),
            settings_file="config/settings.json",
        )
    except FileNotFoundError as e:
        print(e)
        return

    # Create the main menu
    main_menu = MainMenu(screen, config)
    while True:
        main_menu.running = True
        main_menu.run()
        choice = main_menu.choice
        if choice == config.PLAY:
            # adjust grid depending on aspect ratio
            config.calculate_grid_dimensions()
            game = PlayGame(screen, config)
            game.run()
        elif choice == config.PLAY2:
            # Handle 2 player mode
            pass
        elif choice == config.OPTIONS:
            options = Options(screen, config)
            options.run()
        elif choice == config.REPLAY:
            # Handle replay mode
            pass
        else:
            break


if __name__ == "__main__":
    main()
