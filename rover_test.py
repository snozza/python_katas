from rover import Rover, Position, Direction
import unittest

class RoverTests(unittest.TestCase):

    def test_move_one_forward(self):
        self._move_and_test_rover(Position(0, 0),
                Direction.S,
                ('f',),
                Position(-1, 0))

    def test_move_one_forward_one_backward(self):
        self._move_and_test_rover(Position(0, 0),
                Direction.S,
                ('f', 'b'),
                Position(0, 0))

    def test_move_one_forward_two_backward_north(self):
        self._move_and_test_rover(Position(0, 0),
                Direction.N,
                ('f', 'b', 'b'),
                Position(-1, 0))

    def test_move_one_forward_two_backward_turn_left_north(self):
        self._move_and_test_rover(Position(0, 0),
                Direction.N,
                ('f', 'b', 'b', 'l', 'f'),
                Position(-1, -1))

    def test_move_one_forward_two_backward_turn_right_south(self):
        self._move_and_test_rover(Position(0, 0),
                Direction.S,
                ('f', 'b', 'b', 'r', 'f'),
                Position(1, -1))

    def test_move_one_forward_two_backward_turn_left_south(self):
        self._move_and_test_rover(Position(0,0),
                Direction.S,
                ('f', 'b', 'b', 'l', 'f', 'f'),
                Position(1, 2))

    def test_move_one_forward_two_backward_turn_right_west(self):
        self._move_and_test_rover(Position(0,0),
                Direction.S,
                ('f', 'b', 'b', 'r', 'f', 'f'),
                Position(1, -2))

    def test_move_one_forward_two_backward_turn_left_twice_east(self):
        self._move_and_test_rover(Position(0, 0),
                Direction.S,
                ('f', 'b', 'b', 'l', 'l', 'f', 'f'),
                Position(3, 0))

    def test_move_west_on_finite_grid(self):
        rover = Rover(Position(10, 10), Direction.W, (20, 20))
        rover.move(('f', 'f'))
        self.assertEqual(Position(10, 8), rover.get_position())

    def test_move_east_on_finite_grid_with_wrapping(self):
        rover = Rover(Position(10, 10), Direction.E, (10, 10))
        rover.move(('f', 'f', 'f'))
        self.assertEqual(Position(10, -8), rover.get_position())

    def _move_and_test_rover(self, position, direction, movement, expected_position):
        rover = Rover(position, direction)
        rover.move(movement)
        self.assertEqual(expected_position, rover.get_position())

if __name__ == '__main__':
    unittest.main()

