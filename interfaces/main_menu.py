import pygame
import sys
from ui.menu_button import MenuButton
from config.config import GameConfig
from typing import List


class MainMenu:
    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        self.screen = screen
        self.config = config
        self.title_font = pygame.font.Font(None, self.config.TITLE_FONT_SIZE)
        self.title_text = self.title_font.render(self.config.GAME_TITLE, True, self.config.TEXT_COLOR)
        self.button_labels = [config.PLAY, config.PLAY2, config.OPTIONS, config.REPLAY, config.QUIT]
        self.buttons: List[MenuButton] = []

        self.update_positions()
        self.create_buttons()

    def update_positions(self) -> None:
        self.screen_width, self.screen_height = self.screen.get_size()
        self.center_w = self.screen_width // 2
        self.center_h = self.screen_height // 2
        self.title_rect = self.title_text.get_rect(center=(self.center_w, self.center_h - self.config.TITLE_Y_OFFSET_MULTIPLIER * self.config.MB_HEIGHT))

    def create_buttons(self) -> None:
        for i, label in enumerate(self.button_labels):
            button = MenuButton(label, (self.center_w - self.config.MB_WIDTH // 2, self.center_h + i * self.config.MB_HEIGHT - 2 * self.config.MB_HEIGHT), self.config)
            self.buttons.append(button)

    def update_button_positions(self) -> None:
        self.update_positions()
        for i, button in enumerate(self.buttons):
            button.update_button_size()
            button.update((self.center_w - self.config.MB_WIDTH // 2, self.center_h + i * self.config.MB_HEIGHT - 2 * self.config.MB_HEIGHT))

    def display_menu(self) -> None:
        self.screen.fill(self.config.BACKGROUND_COLOR)
        self.screen.blit(self.title_text, self.title_rect)
        for button in self.buttons:
            button.show(self.screen)
        pygame.display.flip()

    def run(self) -> None:
        clock = pygame.time.Clock()
        running = True
        while running:
            self.update_button_positions()
            self.display_menu()
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
                    self.update_positions()
                else:
                    for button in self.buttons:
                        if button.click(event):
                            if button.text_string.lower() == "quit":
                                running = False
                            else:
                                return button.text_string.lower()

            clock.tick(self.config.FPS)
