import pygame
import sys
from ui.menu_button import MenuButton
from config.config import GameConfig
from typing import List

'''
    "menu_scales": {
        "TITLE_Y_OFFSET_MULTIPLIER": 5,
        "TITLE_FONT_SIZE": 144,
        "menu_button": {
            "MB_BORDER_RADIUS": 12,
            "MB_FONT_SIZE": 72
        },
'''

class MainMenu:
    def __init__(self, screen, config: GameConfig):
        self.screen = screen
        self.config = config
        self.update_positions()
        self.title_font = pygame.font.Font(None, self.config.TITLE_FONT_SIZE)
        self.title_text = self.title_font.render(self.config.GAME_TITLE, True, self.config.TEXT_COLOR)
        self.title_rect = self.title_text.get_rect(center=(self.center_w, self.center_h - self.config.TITLE_Y_OFFSET_MULTIPLIER * self.config.MB_HEIGHT))

        button_labels = ["Play", "2 Player", "Settings", "Replay", "Quit"]
        self.buttons: List[MenuButton] = []  # Type hinting for self.buttons
        for i, label in enumerate(button_labels):
            button = MenuButton(label, (self.center_w - self.config.MB_WIDTH // 2, self.center_h + i * self.config.MB_HEIGHT - 2 * self.config.MB_HEIGHT), config)
            self.buttons.append(button)

    def update_positions(self):
        self.screen_width, self.screen_height = self.screen.get_size()
        self.center_w = self.screen_width // 2
        self.center_h = self.screen_height // 2

    def update_button_positions(self):
        self.update_positions()
        self.title_rect = self.title_text.get_rect(center=(self.center_w, self.center_h - self.config.TITLE_Y_OFFSET_MULTIPLIER * self.config.MB_HEIGHT))
        for i, button in enumerate(self.buttons):
            button.update_button_size()
            button.rect.topleft = (self.center_w - self.config.MB_WIDTH // 2, self.center_h + i * self.config.MB_HEIGHT - 2 * self.config.MB_HEIGHT)

    def display_menu(self):
        self.screen.fill(self.config.BACKGROUND_COLOR)
        self.screen.blit(self.title_text, self.title_rect)
        for button in self.buttons:
            button.show(self.screen)
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            self.update_button_positions()
            self.display_menu()
            mouse_pos = pygame.mouse.get_pos()
        
            for button in self.buttons:
                if button.rect.collidepoint(mouse_pos):
                    if not button.highlighted:
                        button.update_highlight(mouse_pos)
                else:
                    if button.highlighted:
                        button.highlighted = False
                        button.update_surface()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.config.update_config(event.w, event.h)
                    self.update_positions()
                else:
                    for button in self.buttons:
                        if button.click(event):
                            if button.text_string.lower() == "quit":
                                running = False
                            else:
                                return button.text_string.lower()


