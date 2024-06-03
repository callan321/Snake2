import pygame
import sys
from main_menu import MainMenu
from play_game import PlayGame
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
        else:
            break

if __name__ == "__main__":
    main()
