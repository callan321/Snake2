# Direction Constants
RIGHT = "R"
LEFT = "L"
DOWN = "D"
UP = "U"

# Direction mappings
DIRECTIONS = {UP: (0, -1), DOWN: (0, 1), LEFT: (-1, 0), RIGHT: (1, 0)}

class Controller:
    """
    Base class for all controllers.

    Attributes:
        direction (tuple[int, int]): The current direction of movement.
    """

    def __init__(self):
        """
        Initialize the Controller with a default direction of DOWN.
        """
        self.direction = DIRECTIONS[DOWN]

    def get_direction(self) -> tuple[int, int]:
        """
        Return the current direction.

        Returns:
            tuple[int, int]: The current direction as (x, y) coordinates.
        """
        return self.direction

    @staticmethod
    def select(controller_type: str) -> "Controller":
        """
        Select and return the appropriate controller based on type.

        Args:
            controller_type (str): The type of controller to select.

        Returns:
            Controller: An instance of the selected controller type.

        Raises:
            ValueError: If the controller type is unknown.
        """
        if controller_type == "AI":
            from logic.controller.bfs_controller import BFSController
            return BFSController()
        elif controller_type == "Arrow":
            from logic.controller.human_controllers import ArrowKeyController
            return ArrowKeyController()
        elif controller_type == "WASD":
            from logic.controller.human_controllers import WASDController
            return WASDController()
        elif controller_type == "Human":
            from logic.controller.human_controllers import CombinedController
            return CombinedController()
        else:
            raise ValueError(f"Unknown controller type: {controller_type}")


class AIController(Controller):
    """
    Base class for AI-controlled controllers.
    """


