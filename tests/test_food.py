import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logic.game_objects.food import Food
from typing import Tuple, Optional

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food = Food()

    def test_initialization(self):
        """Test if the food is initialized with no position."""
        self.assertIsNone(self.food.get_position())

    def test_respawn(self):
        """Test respawning the food at a given position."""
        position = (3, 3)
        self.food.respawn(position)
        self.assertEqual(self.food.get_position(), position)

        # Test respawning the food with None
        self.food.respawn(None)
        self.assertIsNone(self.food.get_position())

    def test_remove(self):
        """Test removing the food."""
        self.food.remove()
        self.assertIsNone(self.food.get_position())

    def test_exists(self):
        """Test if the existence check works correctly."""
        self.assertFalse(self.food.exists())
        position = (5, 0)
        self.food.respawn(position)
        self.assertTrue(self.food.exists())
        self.food.remove()
        self.assertFalse(self.food.exists())

if __name__ == "__main__":
    unittest.main()
