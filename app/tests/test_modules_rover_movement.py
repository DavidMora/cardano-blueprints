import unittest
import math

from app.modules.rover_movement import rotate, move


class ModulesRoverTestCase(unittest.TestCase):
    def test_rover_rotate_left(self):
        self.assertEqual(rotate(0, 'L'), math.pi/2)

    def test_rover_rotate_right(self):
        self.assertEqual(rotate(0, 'R'), -math.pi/2)

    def test_rover_rotate_wrong(self):
        self.assertEqual(rotate(0, 'ANY OTHER THING'), 0)
        self.assertEqual(rotate(math.pi/2, 'ANY OTHER THING'), math.pi/2)

    def test_rover_move(self):
        self.assertEqual(move((0, 1), 0), (1, 1))
        self.assertEqual(move((2, 1), 0), (3, 1))
        self.assertEqual(move((0, 1), math.pi/2), (0, 2))
        self.assertEqual(move((1, 1), math.pi), (0, 1))
        self.assertEqual(move((0, 1), 3*math.pi/2), (0, 0))
