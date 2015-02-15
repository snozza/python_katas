from rover import Rover, Position
import unittest

class RoverTests(unittest.TestCase):

#position has a default x, y
    def test_position_default_coordinates(self):

#rover can be given coords upon instantiation
    def test_rover_given_coordinates(self):

    def test_move_one_forward(self):

if __name__ == '__main__':
    unittest.main()

