class SnakeSpawner:
    def __init__(self, width: int, height: int, nspawns: int) -> None:
        self.width = width
        self.height = height
        self.direction_down = (0, 1)
        self.direction_up = (0, -1)
        self.direction_left = (-1, 0)
        self.direction_right = (1, 0)
        self.spawns = self.calc_spawns(nspawns)

    def get_spawns(self):
        return self.spawns
    
    def calc_spawns(self, nspawns: int):
        if nspawns == 1:
            return [self.top_mid()]

        spawn_points_8_to_12 = [
            self.top_left(),
            self.top_right(),
            self.bottom_left(),
            self.bottom_right(),
            self.left_top(),
            self.left_bottom(),
            self.right_top(),
            self.right_bottom(),
            self.bottom_mid(),
            self.left_mid(),
            self.right_mid(),
            self.top_mid(),
        ]
        
        spawn_points_even = [
            self.top_left(),
            self.top_right(),
            self.bottom_left(),
            self.bottom_right(),
            self.left_mid(),
            self.right_mid(),
        ]

        spawn_points_odd = [
            self.top_left(),
            self.top_right(),
            self.bottom_mid(),
            self.left_mid(),
            self.right_mid(),
            self.bottom_left(),
            self.bottom_right(),
        ]

        if nspawns > 12:
            return spawn_points_8_to_12
        elif 8 <= nspawns <= 12:
            return spawn_points_8_to_12[:nspawns]
        elif nspawns % 2 == 0:
            return spawn_points_even[:nspawns]
        else:
            return spawn_points_odd[:nspawns]
    
    def top_left(self):
        y = 0
        x = self.width // 3
        return (x, y), self.direction_down

    def top_mid(self):
        y = 0
        x = self.width // 2
        return (x, y), self.direction_down

    def top_right(self):
        y = 0
        x = (2 * self.width) // 3
        return (x, y), self.direction_down

    def bottom_left(self):
        y = self.height
        x = self.width // 3
        return (x, y), self.direction_up

    def bottom_mid(self):
        y = self.height
        x = self.width // 2
        return (x, y), self.direction_up

    def bottom_right(self):
        y = self.height
        x = (2 * self.width) // 3
        return (x, y), self.direction_up

    def left_top(self):
        x = 0
        y = self.height // 3
        return (x, y), self.direction_right

    def left_mid(self):
        x = 0
        y = self.height // 2
        return (x, y), self.direction_right

    def left_bottom(self):
        x = 0
        y = (2 * self.height) // 3
        return (x, y), self.direction_right

    def right_top(self):
        x = self.width
        y = self.height // 3
        return (x, y), self.direction_left

    def right_mid(self):
        x = self.width
        y = self.height // 2
        return (x, y), self.direction_left

    def right_bottom(self):
        x = self.width
        y = (2 * self.height) // 3
        return (x, y), self.direction_left
