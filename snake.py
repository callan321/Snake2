from collections import deque

class HashQueue:
    def __init__(self):
        self.data = deque()
        self.hash_map = {}

    def add_front(self, element):
        self.data.appendleft(element)
        if element in self.hash_map:
            self.hash_map[element] += 1
        else:
            self.hash_map[element] = 1

    def add_back(self, element):
        self.data.append(element)
        if element in self.hash_map:
            self.hash_map[element] += 1
        else:
            self.hash_map[element] = 1

    def pop_back(self):
        element = self.data.pop()
        if element in self.hash_map:
            self.hash_map[element] -= 1
            if self.hash_map[element] == 0:
                del self.hash_map[element]

    def peak_front(self):
        return self.data[0]

    def peak_back(self):
        return self.data[-1]

    def check(self, element):
        return self.hash_map.get(element, 0) > 1

    def get_data(self):
        return self.data
    
    def get_length(self):
        return len(self.data)
        

class Snake:
    def __init__(self, start_pos, size=3):
        self.body = HashQueue()
        self.body.add_back(start_pos)
        for _ in range(size - 1):
            self.grow_initial()

    def update(self, direction, food_pos):
        self.move(direction)
        if self.check_food(food_pos):
            self.grow()

    def grow_initial(self):
        tail_x, tail_y = self.body.peak_back()
        new_tail = (tail_x - 1, tail_y)
        self.body.add_back(new_tail)

    def grow(self):
        tail_x, tail_y = self.body.peak_back()
        self.body.add_back((tail_x, tail_y))

    def move(self, direction):
        x, y = direction
        head_x, head_y = self.get_head()
        new_head = (head_x + x, head_y + y)
        self.body.add_front(new_head)
        self.body.pop_back()

    def get_body(self):
        return self.body.get_data()

    def get_head(self):
        return self.body.peak_front()

    def check_food(self, food_pos):
        return self.get_head() == food_pos

    def get_size(self):
        return self.body.get_length()
    
    def check_collision(self, width, height):
        x, y = self.get_head()

        if x < 0 or x >= width or y < 0 or y >= height:
            return True

        if self.get_size() > 4 :
            return self.body.check(self.get_head())
             
        return False
