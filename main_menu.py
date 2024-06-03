import pygame
import sys
from button import MenuButton
import globals as g

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        self.center_w = self.screen_width // 2
        self.center_h = self.screen_height // 2
        self.title_font = pygame.font.Font(None, g.TITAL_FONT_SIZE)  # Choose a font and size for the title
        self.title_text = self.title_font.render(g.GAME_TITLE, True, g.TITLE_COLOR)
        self.title_rect = self.title_text.get_rect(center=(self.center_w, self.center_h - 2 * g.BUTTON_Y_OFFSET))
        self.play_button = MenuButton('Play', (self.center_w, self.center_h - g.BUTTON_Y_OFFSET))
        self.quit_button = MenuButton('Quit', (self.center_w, self.center_h + g.BUTTON_Y_OFFSET))
        

    def update_button_positions(self):
        self.screen_width, self.screen_height = self.screen.get_size()
        self.center_w = self.screen_width // 2
        self.center_h = self.screen_height // 2
        self.title_rect = self.title_text.get_rect(center=(self.center_w, self.center_h - 3 * g.BUTTON_Y_OFFSET))
        
        self.play_button.x = self.center_w - self.play_button.width // 2
        self.play_button.y = self.center_h - g.BUTTON_Y_OFFSET
        self.play_button.rect.topleft = (self.play_button.x, self.play_button.y)

        self.quit_button.x = self.center_w - self.quit_button.width // 2
        self.quit_button.y = self.center_h + g.BUTTON_Y_OFFSET
        self.quit_button.rect.topleft = (self.quit_button.x, self.quit_button.y)

    def display_menu(self):
        self.screen.fill(g.BACKGROUND_COLOR)  # Use the global background color
        self.screen.blit(self.title_text, self.title_rect)
        self.play_button.show(self.screen)
        self.quit_button.show(self.screen)
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            self.update_button_positions()
            self.display_menu()
            mouse_pos = pygame.mouse.get_pos()
            self.play_button.update_highlight(mouse_pos)
            self.quit_button.update_highlight(mouse_pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                elif self.play_button.click(event):
                    return 'play'
                elif self.quit_button.click(event):
                    pygame.quit()
                    sys.exit()
