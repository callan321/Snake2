import pygame
import sys
from main_menu import MainMenu
from play_game import PlayGame
from settings import Settings
import globals as g

def main():
    pygame.init()
    screen_info = pygame.display.Info()
    width, height = screen_info.current_w, screen_info.current_h
    screen = pygame.display.set_mode((width, height - g.TASKBAR_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption(g.GAME_TITLE)
    
    main_menu = MainMenu(screen)
    while True:
        choice = main_menu.run()
        if choice == 'play':
            game = PlayGame(screen)
            if game.run() == 'menu':
                continue
        elif choice == '2player':
            # Handle 2 player mode
            game = PlayGame(screen, mode='2player')
            if game.run() == 'menu':
                continue
        elif choice == 'settings':
            settings = Settings(screen)
            if settings.run() == 'menu':
                continue
        else:
            break

if __name__ == "__main__":
    main()
