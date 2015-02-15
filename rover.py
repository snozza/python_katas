class Rover():

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move(self, commands):
        for cmd in commands:
            if cmd == 'f' and self.direction == Direction.S:
                self.direction.forward(self.position)
            elif cmd == 'b' and self.direction == Direction.S:
                self.direction.backward(self.position)
            elif cmd == 'f' and self.direction == Direction.N:
                self.position.up() 
            elif cmd == 'b' and self.direction == Direction.N:
                self.position.down()

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

class SouthDirection():

    def forward(self, position):
        return position.down()

    def backward(self, position):
        return position.up()

class Direction():
    S = SouthDirection()
    N = 'north'
