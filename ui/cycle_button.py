import pygame
from abc import abstractmethod
from config.config import GameConfig
from ui.standard_button import StandardButton

class CycleButton(StandardButton):
    def __init__(self, config: GameConfig) -> None:
        """Initialize a speed button with text, position, and configuration."""
        super().__init__('', config)
        self.change_text(self.get_text(self.get_attr()))
        self.idx = self.get_options().index(self.get_attr())
        
    @abstractmethod
    def get_options(self):
        pass
    
    @abstractmethod
    def get_attr(self):
        pass
    
    @abstractmethod
    def get_id(self):
        pass
    
    @abstractmethod
    def get_text(self):
        pass
    

    def handle_click(self):
        """Handle the click event for the controller button."""
        options = self.get_options()
        id = self.get_id()
        return self.cycle_options(id, options)
    
    def cycle_options(self, attribute_name: str, options: list) -> bool:
        """
        Generic function to handle click events for various buttons that cycle through options.

        Args:
            attribute_name (str): The name of the attribute to update.
            options (list): The list of options to cycle through.

        Returns:
            bool: Always returns True.
        """
        self.idx = (self.idx + 1) % len(options)
        new_value = options[self.idx]
        self.change_text(self.get_text(new_value))
        self.config.set_attribute(attribute_name, new_value)
        return True