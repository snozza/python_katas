from rover import Rover
import unittest

class RoverTests(unittest.TestCase):

#rover has a default x, y and direction upon instantiation
    def test_new_rover_default_coordinates(self):
        rover = Rover()
        self.assertEqual(0, rover.x)
        self.assertEqual(0, rover.y)

#rover can be given coords upon instantiation
    def test_rover_given_coordinates(self):
        rover = Rover(12, 10)
        self.assertEqual(12, rover.x)
        self.assertEqual(10, rover.y)

    def test_move_one_forward(self):
        rover = Rover(0, 0, 'south')
        rover.move(('f'))
        self.assertEqual((-1, 0), rover.get_position())

    def test_move_three_forward(self):
        rover = Rover(0, 0, 'south')
        rover.move(('f', 'f', 'f'))
        self.assertEqual((-3, 0), rover.get_position())

    def test_move_two_forward_one_backwards(self):
        rover = Rover(0, 0, 'south')
        rover.move(('f', 'f', 'b'))
        self.assertEqual((-1, 0), rover.get_position())

if __name__ == '__main__':
    unittest.main()

