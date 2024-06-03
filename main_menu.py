import pygame
import sys
from ui.button import Button

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.play_button = Button('Play', (350, 250), 74, "blue")
        self.quit_button = Button('Quit', (350, 350), 74, "red")

    def display_menu(self):
        self.screen.fill((0, 0, 0))
        self.play_button.show(self.screen)
        self.quit_button.show(self.screen)
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            self.display_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif self.play_button.click(event):
                    return 'play'
                elif self.quit_button.click(event):
                    pygame.quit()
                    sys.exit()
