import unittest
from app.rover import Rover


class RoverTestCase(unittest.TestCase):
    def setUp(self):
        self.rover = Rover(position=(0, 0), angle=0)

    def test_rover_saves_position(self):
        self.assertEqual(self.rover.position, (0, 0))

    def test_rover_saves_angle(self):
        self.assertEqual(self.rover.position, (0, 0))

    def test_rover_has_incrementing_id(self):
        currentId = Rover.currentId
        rover = Rover(position=(0,0), angle=0)
        self.assertEqual(rover.id, currentId)
        self.assertEqual(Rover.currentId, currentId + 1)
