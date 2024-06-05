import pygame
import sys
from button import MenuButton
import globals as g

class Settings:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = screen.get_size()
        self.center_w = self.screen_width // 2
        self.center_h = self.screen_height // 2
        self.title_font = pygame.font.Font(None, g.TITAL_FONT_SIZE)
        self.title_text = self.title_font.render("Settings", True, g.TITLE_COLOR)
        self.title_rect = self.title_text.get_rect(center=(self.center_w, self.center_h - 5 * g.BUTTON_Y_OFFSET))

        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        button_labels = ['Back']
        for i, label in enumerate(button_labels):
            button = MenuButton(label, (self.center_w, self.center_h + i * 2 * g.BUTTON_Y_OFFSET))
            self.buttons.append(button)

    def update_button_positions(self):
        self.screen_width, self.screen_height = self.screen.get_size()
        self.center_w = self.screen_width // 2
        self.center_h = self.screen_height // 2
        self.title_rect = self.title_text.get_rect(center=(self.center_w, self.center_h - 5 * g.BUTTON_Y_OFFSET))
        
        for i, button in enumerate(self.buttons):
            button.x = self.center_w - button.width // 2
            button.y = self.center_h + i * 2 * g.BUTTON_Y_OFFSET
            button.rect.topleft = (button.x, button.y)

    def display_settings(self):
        self.screen.fill(g.BACKGROUND_COLOR)  # Use the global background color
        self.screen.blit(self.title_text, self.title_rect)
        for button in self.buttons:
            button.show(self.screen)
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            self.update_button_positions()
            self.display_settings()
            mouse_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                button.update_highlight(mouse_pos)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                for button in self.buttons:
                    if button.click(event):
                        if button.text_string == 'Back':
                            return 'menu'


