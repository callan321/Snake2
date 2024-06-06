from typing import Deque, Dict, Any, Optional
from collections import deque

class HashQueue:
    def __init__(self):
        self.data: Deque[Any] = deque()
        self.hash_map: Dict[Any, int] = {}

    def add_front(self, element: Any) -> None:
        self.data.appendleft(element)
        self.hash_map[element] = self.hash_map.get(element, 0) + 1

    def add_back(self, element: Any) -> None:
        self.data.append(element)
        self.hash_map[element] = self.hash_map.get(element, 0) + 1

    def pop_back(self) -> Optional[Any]:
        if not self.data:
            return None
        element = self.data.pop()
        self.hash_map[element] -= 1
        if self.hash_map[element] == 0:
            del self.hash_map[element]
        return element

    def peak_front(self) -> Any:
        return self.data[0]

    def peak_back(self) -> Any:
        return self.data[-1]

    def check1(self, element: Any) -> bool:
        return self.hash_map.get(element, 0) > 1

    def check0(self, element: Any) -> bool:
        return self.hash_map.get(element, 0) > 0

    def get_data(self) -> Deque[Any]:
        return self.data

    def get_length(self) -> int:
        return len(self.data)
