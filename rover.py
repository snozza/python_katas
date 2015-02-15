class Rover:
    
    def __init__(self, position, direction='south'):
        self.position = position
        self.direction = direction

    def move(self, commands=()):
        for cmd in commands:
            if cmd == 'f' and self.direction == 'south':
                self.position.down()
            if cmd == 'b' and self.direction == 'south':
                self.position.up()
            if cmd == 'f' and self.direction == 'north':
                self.position.up()
            if cmd == 'b' and self.direction == 'north':
                self.position.down()
            if cmd == 'f' and self.direction == 'east':
                self.position.right()
            if cmd == 'b' and self.direction == 'east':
                self.position.left()
            if cmd == 'f' and self.direction == 'west':
                self.position.left()
            if cmd == 'b' and self.direction == 'west':
                self.position.right()

    def get_position(self):
        return self.position.get_position()

class Position:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def down(self):
        self.x -= 1

    def up(self):
        self.x += 1

    def right(self):
        self.y += 1

    def left(self):
        self.y -= 1

    def get_position(self):
        return (self.x, self.y)

