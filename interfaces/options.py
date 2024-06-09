import pygame
import sys
from ui.menu_button import MenuButton
from ui.back_button import BackButton
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
            center=(self.center_w, self.center_h - 3 * self.config.GS_BUTTON_HEIGHT)
        )

    def create_buttons(self) -> None:
        """Create buttons for the options menu."""
        button_data = self.config.GAME_SIZE_BUTTONS
        for label, values in button_data.items():
            button = GameSizeButton(
                label,
                self.config
            )
            button.number_of_cells = values['number_of_cells']
            button.snake_size = values['snake_size']
            self.buttons.append(button)

        self.back_button = BackButton(self.config.BACK, self.config)

    def update_button_positions(self) -> None:
        """Update button positions when the screen is resized."""
        self.update_positions()
        button_width = self.config.GS_BUTTON_WIDTH
        total_width = len(self.config.GAME_SIZE_BUTTONS) * button_width
        start_x = self.center_w - (total_width // 2) + (button_width // 2)

        for i, button in enumerate(self.buttons):  # Update cell selection buttons
            button.update((start_x + i * button_width - button_width // 2, self.center_h))

        self.back_button.update((self.center_w - self.config.MB_WIDTH // 2, self.center_h + 2 * self.config.GS_BUTTON_HEIGHT))

    def display_menu(self) -> None:
        """Display the options menu with the title and buttons."""
        self.screen.fill(self.config.BACKGROUND_COLOR)
        self.screen.blit(self.title_text, self.title_rect)
        for button in self.buttons:
            button.draw(self.screen)
        self.back_button.draw(self.screen)  # Ensure back button is displayed
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
            self.back_button.update_highlight(mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif self.back_button.click(event):
                    if self.back_button.handle_click():
                        return self.config.MENU
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.config.update_config(event.w, event.h)
                    self.update_positions()
                else:
                    for button in self.buttons:
                        if button.click(event):
                            button.handle_click()

            clock.tick(self.config.FPS)
