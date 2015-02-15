class Rover():

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move(self, commands):
        for cmd in commands:
            if cmd == 'f':
                self.position.down()
            else:
                self.position.up()

    def get_position(self):
        return self.position

class Position():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Position x=%s, y=%s>" % (self.x, self.y)

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

class Direction():
    S = 'south'
