class Rover:
    
    def __init__(self, x=0, y=0, direction='south'):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, commands=()):
        for cmd in commands:
            if cmd == 'f' and self.direction == 'south':
                self.x -= 1
            if cmd == 'b' and self.direction == 'south':
                self.x += 1

    def get_position(self):
        return (self.x, self.y)