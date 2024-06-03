import pygame
import sys
from main_menu import MainMenu
from play_game import PlayGame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Snake 2')

    main_menu = MainMenu(screen)
    while True:
        choice = main_menu.run()
        if choice == 'play':
            game = PlayGame(screen)
            game.run()
        else:
            break

if __name__ == "__main__":
    main()
