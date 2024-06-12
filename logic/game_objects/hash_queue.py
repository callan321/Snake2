from typing import Deque, Dict, Any, Optional
from collections import deque

class HashQueue:
    """
    A queue-like data structure that also keeps track of the number of occurrences
    of each element using a dictionary for O(1) worst-case time complexity.
    """

    def __init__(self) -> None:
        """
        Initialize an empty HashQueue.
        """
        self.data: Deque[Any] = deque()
        self.hash_map: Dict[Any, int] = {}

    def add_front(self, element: Any) -> None:
        """
        Add an element to the front of the queue.

        :param element: The element to add to the front.
        """
        self.data.appendleft(element)
        self.hash_map[element] = self.hash_map.get(element, 0) + 1

    def add_back(self, element: Any) -> None:
        """
        Add an element to the back of the queue.

        :param element: The element to add to the back.
        """
        self.data.append(element)
        self.hash_map[element] = self.hash_map.get(element, 0) + 1

    def pop_back(self) -> Optional[Any]:
        """
        Remove and return the element from the back of the queue.

        :return: The element from the back of the queue, or None if the queue is empty.
        """
        if not self.data:
            return None
        element = self.data.pop()
        self.hash_map[element] -= 1
        if self.hash_map[element] == 0:
            del self.hash_map[element]
        return element

    def peak_front(self) -> Any:
        """
        Return the element at the front of the queue without removing it.

        :return: The element at the front of the queue.
        """
        return self.data[0]

    def peak_back(self) -> Any:
        """
        Return the element at the back of the queue without removing it.

        :return: The element at the back of the queue.
        """
        return self.data[-1]

    def check1(self, element: Any) -> bool:
        """
        Check if the element appears more than once in the queue.

        :param element: The element to check.
        :return: True if the element appears more than once, False otherwise.
        """
        return self.hash_map.get(element, 0) > 1

    def check0(self, element: Any) -> bool:
        """
        Check if the element appears at least once in the queue.

        :param element: The element to check.
        :return: True if the element appears at least once, False otherwise.
        """
        return self.hash_map.get(element, 0) > 0

    def get_data(self) -> Deque[Any]:
        """
        Get the underlying deque data.

        :return: The deque data.
        """
        return self.data

    def get_length(self) -> int:
        """
        Get the number of elements in the queue.

        :return: The length of the queue.
        """
        return len(self.data)
