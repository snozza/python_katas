class Rover():

    def __init__(self, position, direction, grid_size=(-1, -1)):
        self.position = position
        self.position.set_grid_size(grid_size)
        self.direction = direction

    def move(self, commands):
        for cmd in commands:
            if cmd == 'f':
                self.direction.forward(self.position)
            elif cmd == 'b':
                self.direction.backward(self.position)
            elif cmd == 'l':
                self.direction = self.direction.turn_left()
            elif cmd == 'r':
                self.direction = self.direction.turn_right()

    def get_position(self):
        return self.position

class Position():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_grid_size(self, grid_size):
        self.grid_size = grid_size

    def is_finite_grid(self):
        return self.grid_size != (-1, -1)

    def __repr__(self):
        return "<Position x=%r, y=%r>" % (self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.x == self.x and other.y == self.y
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return other.x != self.x
        else:
            return True

    def down(self):
        if self.is_finite_grid() and self.x-1 < self.grid_size[0] * -1:
            self.x = self.grid_size[0]
        else:
            self.x -= 1

    def up(self):
        if self.is_finite_grid() and self.x+1 > self.grid_size[0]:
            self.x = 0-self.grid_size[0]
        else:
            self.x += 1

    def left(self):
        if self.is_finite_grid() and self.y-1 < self.grid_size[1] * -1:
            self.y = self.grid_size[1]
        else:
            self.y -= 1

    def right(self):
        if self.is_finite_grid() and self.y+1 > self.grid_size[1]:
            self.y = 0-self.grid_size[1]
        else: 
            self.y += 1

class NorthDirection():

    def forward(self, position):
        return position.up()

    def backward(self, position):
        return position.down()

    def turn_left(self):
        return Direction.W

    def turn_right(self):
        return Direction.E

class WestDirection():

    def forward(self, position):
        return position.left()

    def backward(self, position):
        return position.right()

    def turn_right(self):
        return Direction.N

    def turn_left(self):
        return Direction.S

class EastDirection():

    def forward(self, position):
        return position.right()

    def backward(self, position):
        return position.left()

    def turn_right(self):
        return Direction.S

    def turn_left(self):
        return Direction.N

class SouthDirection():

    def forward(self, position):
        return position.down()

    def backward(self, position):
        return position.up()

    def turn_right(self):
        return Direction.W

    def turn_left(self):
        return Direction.E

class Direction():
    S = SouthDirection()
    N = NorthDirection()
    W = WestDirection()
    E = EastDirection()
