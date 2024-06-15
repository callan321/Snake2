import unittest
from collections import deque
import timeit
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logic.game_objects.hash_queue import HashQueue


class TestHashQueue(unittest.TestCase):

    def setUp(self):
        self.hash_queue = HashQueue()

    # Functional Tests
    def test_initialization(self):
        """Test if the HashQueue is initialized correctly."""
        self.assertEqual(len(self.hash_queue.get_data()), 0)
        self.assertEqual(self.hash_queue.get_length(), 0)

    def test_add_front(self):
        """Test adding elements to the front of the queue."""
        self.hash_queue.add_front(1)
        self.assertEqual(self.hash_queue.peak_front(), 1)
        self.hash_queue.add_front(2)
        self.assertEqual(self.hash_queue.peak_front(), 2)
        self.assertEqual(self.hash_queue.get_length(), 2)

    def test_add_back(self):
        """Test adding elements to the back of the queue."""
        self.hash_queue.add_back(1)
        self.assertEqual(self.hash_queue.peak_back(), 1)
        self.hash_queue.add_back(2)
        self.assertEqual(self.hash_queue.peak_back(), 2)
        self.assertEqual(self.hash_queue.get_length(), 2)

    def test_pop_back(self):
        """Test removing elements from the back of the queue."""
        self.hash_queue.add_back(1)
        self.hash_queue.add_back(2)
        self.assertEqual(self.hash_queue.pop_back(), 2)
        self.assertEqual(self.hash_queue.peak_back(), 1)
        self.assertEqual(self.hash_queue.get_length(), 1)
        self.assertEqual(self.hash_queue.pop_back(), 1)
        self.assertIsNone(self.hash_queue.pop_back())

    def test_peak_front(self):
        """Test peeking at the front element."""
        self.hash_queue.add_front(1)
        self.hash_queue.add_back(2)
        self.assertEqual(self.hash_queue.peak_front(), 1)

    def test_peak_back(self):
        """Test peeking at the back element."""
        self.hash_queue.add_front(1)
        self.hash_queue.add_back(2)
        self.assertEqual(self.hash_queue.peak_back(), 2)

    def test_check1(self):
        """Test checking if an element appears more than once."""
        self.hash_queue.add_back(1)
        self.hash_queue.add_back(1)
        self.assertTrue(self.hash_queue.has_multi(1))
        self.assertFalse(self.hash_queue.has_multi(2))

    def test_check0(self):
        """Test checking if an element appears at least once."""
        self.hash_queue.add_back(1)
        self.assertTrue(self.hash_queue.has_one(1))
        self.assertFalse(self.hash_queue.has_one(2))

    def test_get_data(self):
        """Test getting the underlying deque data."""
        self.hash_queue.add_back(1)
        self.hash_queue.add_back(2)
        self.assertEqual(self.hash_queue.get_data(), deque([1, 2]))

    def test_get_length(self):
        """Test getting the length of the queue."""
        self.hash_queue.add_back(1)
        self.hash_queue.add_back(2)
        self.assertEqual(self.hash_queue.get_length(), 2)

    def test_combined_check1_check0(self):
        """Test combining check1 and check0 with add and remove operations."""
        # Add the element 1 twice
        self.hash_queue.add_back(1)
        self.hash_queue.add_back(1)
        
        # Check if check1 and check0 return correct values
        self.assertTrue(self.hash_queue.has_multi(1))
        self.assertTrue(self.hash_queue.has_one(1))

        # Remove one occurrence of 1
        self.hash_queue.pop_back()

        # Check if check1 and check0 return correct values after removal
        self.assertFalse(self.hash_queue.has_multi(1))
        self.assertTrue(self.hash_queue.has_one(1))

        # Remove the remaining occurrence of 1
        self.hash_queue.pop_back()

        # Check if check1 and check0 return correct values after complete removal
        self.assertFalse(self.hash_queue.has_multi(1))
        self.assertFalse(self.hash_queue.has_one(1))

    """
    Performance Tests
    """

    def measure_time(self, method, *args, number=10000):
        """
        Measure the execution time of a method.

        :param method: The method to measure.
        :param args: The arguments to pass to the method.
        :param number: The number of executions.
        :return: The average execution time per call.
        """
        timer = timeit.Timer(lambda: method(*args))
        return timer.timeit(number=number) / number

    def test_add_front_performance(self):
        """Test the performance of adding elements to the front."""
        for i in range(1, 10000, 1000):
            self.hash_queue = HashQueue()  # Reset the queue
            time = self.measure_time(self.hash_queue.add_front, i)
            print(f"Add front with element {i}: {time:.10f} seconds")

    def test_add_back_performance(self):
        """Test the performance of adding elements to the back."""
        for i in range(1, 10000, 1000):
            self.hash_queue = HashQueue()  # Reset the queue
            time = self.measure_time(self.hash_queue.add_back, i)
            print(f"Add back with element {i}: {time:.10f} seconds")

    def test_pop_back_performance(self):
        """Test the performance of popping elements from the back."""
        for i in range(1, 10000, 1000):
            self.hash_queue = HashQueue()  # Reset the queue
            for j in range(i):
                self.hash_queue.add_back(j)
            time = self.measure_time(self.hash_queue.pop_back)
            print(f"Pop back with {i} elements: {time:.10f} seconds")

    def test_check1_performance(self):
        """Test the performance of checking if an element appears more than once."""
        self.hash_queue = HashQueue()
        for i in range(10000):
            self.hash_queue.add_back(i)
        time = self.measure_time(self.hash_queue.has_multi, 5000)
        print(f"Check1 with element appearing once: {time:.10f} seconds")
        self.hash_queue.add_back(5000)
        time = self.measure_time(self.hash_queue.has_multi, 5000)
        print(f"Check1 with element appearing twice: {time:.10f} seconds")

    def test_has_one_performance(self):
        """Test the performance of checking if an element appears at least once."""
        self.hash_queue = HashQueue()
        for i in range(10000):
            self.hash_queue.add_back(i)
        time = self.measure_time(self.hash_queue.has_one, 5000)
        print(f"Check0 with element present: {time:.10f} seconds")
        time = self.measure_time(self.hash_queue.has_one, 10000)
        print(f"Check0 with element not present: {time:.10f} seconds")


if __name__ == "__main__":
    unittest.main()
