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

    def pop_front(self) -> Optional[Any]:
        """
        Remove and return the element from the front of the queue.

        :return: The element from the front of the queue, or None if the queue is empty.
        """
        if not self.data:
            return None
        element = self.data.popleft()
        self.hash_map[element] -= 1
        if self.hash_map[element] == 0:
            del self.hash_map[element]
        return element

    def peak_front(self) -> Optional[Any]:
        """
        Return the element at the front of the queue without removing it.

        :return: The element at the front of the queue, or None if the queue is empty.
        """
        if not self.data:
            return None
        return self.data[0]

    def peak_back(self) -> Optional[Any]:
        """
        Return the element at the back of the queue without removing it.

        :return: The element at the back of the queue, or None if the queue is empty.
        """
        if not self.data:
            return None
        return self.data[-1]

    def has_multi(self, element: Any) -> bool:
        """
        Check if the element appears more than once in the queue.

        :param element: The element to check.
        :return: True if the element appears more than once, False otherwise.
        """
        return self.hash_map.get(element, 0) > 1

    def has_one(self, element: Any) -> bool:
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

    def __str__(self) -> str:
        """
        Return a string representation of the HashQueue.

        :return: A string representing the HashQueue.
        """
        return f"HashQueue(data={list(self.data)}, hash_map={self.hash_map})"

    def __repr__(self) -> str:
        """
        Return a string representation of the HashQueue.

        :return: A string representing the HashQueue.
        """
        return self.__str__()
