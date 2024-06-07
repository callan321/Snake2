import pygame
import sys
from ui.menu_button import MenuButton
from ui.game_size_button import GameSizeButton
from config.config import GameConfig

class Options:
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
        button_data = self.config.GAME_SIZE_BUTTONS
        for i, (label, values) in enumerate(button_data.items()):
            button = GameSizeButton(label, (self.center_w + (i - 2) * (self.config.GAME_SIZE_BUTTON_WIDTH + 20), self.center_h), self.config)
            button.number_of_cells = values['number_of_cells']
            button.snake_size = values['snake_size']
            self.buttons.append(button)
        back_button = MenuButton('Back', (self.center_w, self.center_h + 2 * self.config.BUTTON_Y_OFFSET), self.config)
        self.buttons.append(back_button)

    def update_dimensions(self):
        self.screen_width, self.screen_height = self.screen.get_size()
        self.center_w = self.screen_width // 2
        self.center_h = self.screen_height // 2

    def update_button_positions(self):
        self.update_dimensions()
        self.title_rect = self.title_text.get_rect(center=(self.center_w, self.center_h - 5 * self.config.BUTTON_Y_OFFSET))

        for i, button in enumerate(self.buttons[:-1]):  # Update cell selection buttons
            button.x = self.center_w + (i - 2) * (self.config.GAME_SIZE_BUTTON_WIDTH + 20) - button.width // 2
            button.y = self.center_h
            button.rect.topleft = (button.x, button.y)
            button.update_surface()

        # Update position of the 'Back' button
        back_button = self.buttons[-1]
        back_button.x = self.center_w - back_button.width // 2
        back_button.y = self.center_h + 2 * self.config.BUTTON_Y_OFFSET
        back_button.rect.topleft = (back_button.x, back_button.y)
        back_button.update_surface()

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
                        else:
                            self.config.settings['game_settings']['number_of_cells'] = button.number_of_cells
                            self.config.settings['game_settings']['snake_size'] = button.snake_size
                            self.config.save_settings()
                            self.config.number_of_cells = button.number_of_cells
                            self.config.snake_size = button.snake_size
