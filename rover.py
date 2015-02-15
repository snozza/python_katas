class Rover():

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move(self, commands):
        for cmd in commands:
            if cmd == 'f':
                self.direction.forward(self.position)
            elif cmd == 'b':
                self.direction.backward(self.position)
            elif cmd == 'l':
                self.direction = self.direction.turn_left()

    def get_position(self):
        return self.position

class Position():

    def __init__(self, x, y):
        self.x = x
        self.y = y

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
        self.x -= 1

    def up(self):
        self.x += 1

    def left(self):
        self.y -= 1

    def right(self):
        self.y += 1

class NorthDirection():

    def forward(self, position):
        return position.up()

    def backward(self, position):
        return position.down()

    def turn_left(self):
        return Direction.W

class WestDirection():

    def forward(self, position):
        return position.left()

    def backward(self, position):
        return position.right()

class SouthDirection():

    def forward(self, position):
        return position.down()

    def backward(self, position):
        return position.up()

class Direction():
    S = SouthDirection()
    N = NorthDirection()
    W = WestDirection()
