import pygame
import sys
from ui.menu_button import MenuButton
from ui.game_size_button import GameSizeButton
from config.config import GameConfig
from typing import List

class Options:
    def __init__(self, screen: pygame.Surface, config: GameConfig) -> None:
        """Initialize the options menu with screen and configuration."""
        self.screen = screen
        self.config = config
        self.title_font = pygame.font.Font(None, self.config.TITLE_FONT_SIZE)
        self.title_text = self.title_font.render("Settings", True, self.config.TEXT_COLOR)
        self.buttons: List[MenuButton] = []

        self.update_positions()
        self.create_buttons()

    def update_positions(self) -> None:
        """Update positions of the title and buttons based on screen size."""
        self.screen_width, self.screen_height = self.screen.get_size()
        self.center_w = self.screen_width // 2
        self.center_h = self.screen_height // 2
        self.title_rect = self.title_text.get_rect(
            center=(self.center_w, self.center_h - 5 * self.config.MB_HEIGHT)
        )

    def create_buttons(self) -> None:
        """Create buttons for the options menu."""
        button_data = self.config.GAME_SIZE_BUTTONS
        for i, (label, values) in enumerate(button_data.items()):
            button = GameSizeButton(
                label,
                (self.center_w + (i - 2) * (self.config.GS_BUTTON_WIDTH), self.center_h),
                self.config
            )
            button.number_of_cells = values['number_of_cells']
            button.snake_size = values['snake_size']
            self.buttons.append(button)
        back_button = MenuButton('Back', (self.center_w, self.center_h + 2 * self.config.MB_HEIGHT), self.config)
        self.buttons.append(back_button)

    def update_button_positions(self) -> None:
        """Update button positions when the screen is resized."""
        self.update_positions()
        for i, button in enumerate(self.buttons[:-1]):  # Update cell selection buttons
            button.update((self.center_w + (i - 2) * (self.config.GS_BUTTON_WIDTH), self.center_h))
        # Update position of the 'Back' button
        back_button = self.buttons[-1]
        back_button.update((self.center_w, self.center_h + 2 * self.config.MB_HEIGHT))

    def display_menu(self) -> None:
        """Display the options menu with the title and buttons."""
        self.screen.fill(self.config.BACKGROUND_COLOR)
        self.screen.blit(self.title_text, self.title_rect)
        for button in self.buttons:
            button.show(self.screen)
        pygame.display.flip()

    def run(self) -> str:
        """Run the options menu loop to handle events and button clicks."""
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
                            if button.text_string == 'Back':
                                return 'menu'
                            else:
                                self.config.settings['game_settings']['number_of_cells'] = button.number_of_cells
                                self.config.settings['game_settings']['snake_size'] = button.snake_size
                                self.config.save_settings()
                                self.config.number_of_cells = button.number_of_cells
                                self.config.snake_size = button.snake_size

            clock.tick(self.config.FPS)
