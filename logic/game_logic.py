from logic.controller.controller import AIController
from typing import Tuple
from logic.ai_game_logic import GameLogicAI


class GameLogic(GameLogicAI):

    def get_direction(self) -> Tuple[int, int]:
        if isinstance(self.controller, AIController):
            return self.controller.get_direction(
                self.snake, self.food.get_position(), self.width, self.height
            )
        return self.controller.get_direction()
