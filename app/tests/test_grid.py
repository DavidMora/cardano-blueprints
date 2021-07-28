import unittest
import math
from app.grid import Grid
from app.rover import Rover


class GridTestCase(unittest.TestCase):
    def test_grid_is_created(self):
        grid = Grid((9, 9))
        self.assertEqual(grid.rovers, [])

    def test_appendRoverToGrid(self):
        grid = Grid((5, 5))
        rover = Rover((0, 0), 0)
        result = grid.appendRover(rover)
        self.assertTrue(result)
        self.assertEqual(len(grid.rovers), 1)

    def test_validateMultipleRovers(self):
        grid = Grid((5, 5))
        rover1 = Rover((0, 0), 0)
        grid.appendRover(rover1)
        rover2 = Rover((0, 1), 0)
        grid.appendRover(rover2)
        self.assertEqual(len(grid.rovers), 2)

    def test_validateRoverCantBeAppendedOverExistingRover(self):
        grid = Grid((5, 5))
        rover1 = Rover((0, 0), 0)
        grid.appendRover(rover1)
        rover2 = Rover((0, 0), 0)
        result = grid.appendRover(rover2)
        self.assertFalse(result)

    def test_gridValidatePositionFails(self):
        grid = Grid((5, 5))
        rover1 = Rover((0, 0), 0)
        grid.appendRover(rover1)
        rover2 = Rover((0, 1), 0)
        grid.appendRover(rover2)
        self.assertFalse(grid.validateRoverPosition(rover2, (-1, 0)))
        self.assertFalse(grid.validateRoverPosition(rover2, (0, -1)))
        self.assertFalse(grid.validateRoverPosition(rover2, (6, 0)))
        self.assertFalse(grid.validateRoverPosition(rover2, (0, 5)))
        self.assertFalse(grid.validateRoverPosition(rover2, (0, 0)))

    def test_gridValidatePositionSucceeds(self):
        grid = Grid((5, 5))
        rover1 = Rover((0, 0), 0)
        grid.appendRover(rover1)
        rover2 = Rover((0, 1), 0)
        grid.appendRover(rover2)
        self.assertTrue(grid.validateRoverPosition(rover2, (0, 1)))

    def test_updatePositionFails(self):
        grid = Grid((5, 5))
        rover1 = Rover((0, 0), 0)
        rover2 = Rover((0, 0), 0)
        grid.appendRover(rover1)
        grid.updateRoverPosition(rover1, (2, 2))
        self.assertFalse(grid.updateRoverPosition(rover2, (2, 2)))

    def test_updatePositionSucceeds(self):
        grid = Grid((5, 5))
        rover1 = Rover((0, 0), 0)
        grid.appendRover(rover1)
        grid.updateRoverPosition(rover1, (2, 2))
        self.assertEqual(grid.rovers[0].position, (2, 2))

    def test_updateAngleFails(self):
        grid = Grid((5, 5))
        rover1 = Rover((0, 0), 0)
        rover2 = Rover((0, 0), 0)
        grid.appendRover(rover1)
        self.assertFalse(grid.updateRoverAngle(rover2, 0))

    def test_updateAngleSucceeds(self):
        grid = Grid((5, 5))
        rover1 = Rover((0, 0), 0)
        grid.appendRover(rover1)
        grid.updateRoverAngle(rover1, math.pi/2)
        self.assertEqual(grid.rovers[0].angle, math.pi/2)

    def test_validateRoverPositionWithMultipleRovers(self):
        grid = Grid((5, 5))
        rover1 = Rover((0, 0), 0)
        grid.appendRover(rover1)
        rover2 = Rover((1, 0), 0)
        grid.appendRover(rover2)
        rover3 = Rover((2, 0), 0)
        grid.appendRover(rover3)
        result = grid.validateRoverPosition(rover1, (4, 4))
        self.assertTrue(result)

    def test_RoversStatus(self):
        grid = Grid((5, 5))
        rover1 = Rover((0, 0), 0)
        grid.appendRover(rover1)
        rover2 = Rover((1, 0), 0)
        grid.appendRover(rover2)
        rover3 = Rover((2, 0), 0)
        grid.appendRover(rover3)
        status = grid.getRoversStatus()
        self.assertEqual(len(status), 3)

    def test_RoversStatusReturnsEmpty(self):
        grid = Grid((5, 5))
        status = grid.getRoversStatus()
        self.assertEqual(len(status), 0)
