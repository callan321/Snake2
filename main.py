import pygame
from interfaces.main_menu import MainMenu
from interfaces.play_game import PlayGame
from interfaces.options import Options
from config.config import GameConfig

### bugs ###
# spawn generator goes outside area like due to snake death un expected behaviour 
### update ###
# make better system for handling button clicks
# better system for handling hovers

# wall
# esp

### optional ###
# arrows
# enter select 

# fullscreenmode
# cheatmode
# wall
# metronome
# add hold button
# hold ff
# pause overlay
# syn time with bpm
# metronome 

# scores
# ai vs

# replay
# go thorugh files
# save files
# delete files
# replay interface
# file manager 

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
        main_menu.reset()
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
