import pygame
import sys
from ui.menu_button import MenuButton
from config.config import GameConfig

class Settings:
    def __init__(self, screen, config: GameConfig):
        self.screen = screen
        self.config = config
        self.update_dimensions()
        self.title_font = pygame.font.Font(None, self.config.TITLE_FONT_SIZE)
        self.title_text = self.title_font.render("Settings", True, self.config.TEXT_COLOR)
        self.title_rect = self.title_text.get_rect(center=(self.center_w, self.center_h - 5 * self.config.BUTTON_Y_OFFSET))

        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        button_labels = ['Back']
        for i, label in enumerate(button_labels):
            button = MenuButton(label, (self.center_w, self.center_h + i * 2 * self.config.BUTTON_Y_OFFSET), self.config)
            self.buttons.append(button)

    def update_dimensions(self):
        self.screen_width, self.screen_height = self.screen.get_size()
        self.center_w = self.screen_width // 2
        self.center_h = self.screen_height // 2

    def update_button_positions(self):
        self.update_dimensions()
        self.title_rect = self.title_text.get_rect(center=(self.center_w, self.center_h - 5 * self.config.BUTTON_Y_OFFSET))

        for i, button in enumerate(self.buttons):
            button.x = self.center_w - button.width // 2
            button.y = self.center_h + i * 2 * self.config.BUTTON_Y_OFFSET
            button.rect.topleft = (button.x, button.y)
            button.update_surface()

    def display_settings(self):
        self.screen.fill(self.config.BACKGROUND_COLOR)
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
                    self.config.update_config(event.w, event.h)
                    self.update_button_positions()
                for button in self.buttons:
                    if button.click(event):
                        if button.text_string == 'Back':
                            return 'menu'
