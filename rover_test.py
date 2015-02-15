import rover
import unittest

class RoverTests(unittest.TestCase):

#rover has a default x, y and origination upon initiation
    def test_new_rover_default_coordinates(self):
        r = rover.Rover()
        self.assertEqual(0, r.x)
        self.assertEqual(0, r.y)

#rover can be given coords upon initiation
    def test_rover_given_coordinates(self):
        r = rover.Rover(12, 10)
        self.assertEqual(12, r.x)
        self.assertEqual(10, r.y)


if __name__ == '__main__':
    unittest.main()

