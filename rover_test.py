from rover import Rover, Position
import unittest

class RoverTests(unittest.TestCase):

#position has a default x, y
    def test_position_default_coordinates(self):
        position = Position()
        self.assertEqual(0, position.x)
        self.assertEqual(0, position.y)

#rover can be given coords upon instantiation
    def test_rover_given_coordinates(self):
        rover = Rover(Position(12, 10), 'south')
        self.assertEqual((12, 10), rover.get_position())

    def test_move_one_forward(self):
        rover = Rover(Position(0, 0), 'south')
        rover.move(('f'))
        self.assertEqual((-1, 0), rover.get_position())

    def test_move_three_forward(self):
        rover = Rover(Position(0, 0), 'south')
        rover.move(('f', 'f', 'f'))
        self.assertEqual((-3, 0), rover.get_position())

    def test_move_two_forward_one_backwards(self):
        rover = Rover(Position(0, 0), 'south')
        rover.move(('f', 'f', 'b'))
        self.assertEqual((-1, 0), rover.get_position())

    def test_move_three_forward_four_backwards_north(self):
        rover = Rover(Position(0, 0), 'north')
        rover.move(('f', 'f', 'f', 'b', 'b', 'b', 'b'))
        self.assertEqual((-1, 0), rover.get_position())

    def test_move_five_forward_east(self):
        rover = Rover(Position(0, 0), 'east')
        rover.move(('f', 'f', 'f', 'f', 'f'))
        self.assertEqual((0, 5), rover.get_position())

    def test_move_two_backwards_west(self):
        rover = Rover(Position(0, 0), 'west')
        rover.move(('b', 'b'))
        self.assertEqual((0, 2), rover.get_position())

if __name__ == '__main__':
    unittest.main()

