import rover
import unittest

class RoverTests(unittest.TestCase):

#rover has a x, y and origination upon initiation
    def test_access_rover_variables(self):
        r = rover.Rover(10, 12, 'N')
        self.assertEqual(10, r.x)
        self.assertEqual(12, r.y)
        self.assertEqual('N', r.orientation)

#implement commands to move rover forwards and backwards
    def test_rover_receives_forward_command(self):
        r = rover.Rover(5, 10, 'N')
        r.executeCommands(['f'])
        self.assertEqual(5, r.x)
        self.assertEqual(11, r.y)


if __name__ == '__main__':
    unittest.main()

