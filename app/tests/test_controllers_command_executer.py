import unittest
import math
from app.grid import Grid
from app.rover import Rover
from app.controllers.command_executer import (
            execute,
            initGrid,
            initRover,
            moveRover
        )


class CommandExecuterTestCase(unittest.TestCase):
    def test_initGridSucceeds(self):
        grid = initGrid('4 4')
        self.assertIsInstance(grid, Grid)

    def test_initGridFails(self):
        grid = initGrid('K 4')
        self.assertIsNone(grid)
        grid = initGrid('0 0')
        self.assertIsNone(grid)

    def test_initRoverSucceeds(self):
        rover = initRover('1 2 N')
        self.assertIsInstance(rover, Rover)

    def test_initRoverFails(self):
        rover = initRover('K 2 N')
        self.assertIsNone(rover)

    def test_moveRoverNoEdges(self):
        grid = Grid((5, 5))
        rover = Rover((0, 0), 0)
        grid.appendRover(rover)
        coordinates = moveRover('LRMLMM', grid, rover)
        self.assertEqual(coordinates[0][0]['angle'], math.pi/2)
        self.assertEqual(coordinates[1][0]['angle'], 0)
        self.assertEqual(coordinates[2][0]['position'], (1, 0))
        self.assertEqual(coordinates[5][0]['position'], (1, 2))
        self.assertEqual(len(coordinates), 6)

    def test_moveRoverNoMovementBecauseOfEdges(self):
        grid = Grid((5, 5))
        rover = Rover((0, 0), 0)
        grid.appendRover(rover)
        coordinates = moveRover('LLMMMMMMMMMRRRMMRLLLLRM', grid, rover)
        self.assertEqual(coordinates[1][0]['angle'], math.pi)
        self.assertEqual(len(coordinates), 2)
        grid = Grid((2, 2))
        rover = Rover((0, 0), 0)
        grid.appendRover(rover)
        coordinates = moveRover('LMM', grid, rover)
        self.assertEqual(len(coordinates), 2)
        grid = Grid((2, 2))
        rover = Rover((0, 0), 0)
        grid.appendRover(rover)
        coordinates = moveRover('MM', grid, rover)
        self.assertEqual(len(coordinates), 1)
        grid = Grid((2, 2))
        rover = Rover((0, 0), 0)
        grid.appendRover(rover)
        coordinates = moveRover('RRM', grid, rover)
        self.assertEqual(len(coordinates), 2)

    def test_moveRoverColission(self):
        grid = Grid((5, 5))
        rover1 = Rover((0, 0), 0)
        grid.appendRover(rover1)
        rover2 = Rover((1, 1), 0)
        grid.appendRover(rover2)
        coordinates = moveRover('LMRMRMMMMM', grid, rover1)
        self.assertEqual(coordinates[1][0]['position'], (0, 1))
        self.assertEqual(len(coordinates), 3)

    def test_executeFailsBecauseNoCommands(self):
        failedResponse = {'status': 'Failed'}
        commands = ""
        self.assertEqual(execute(commands), failedResponse)

    def test_executeFailsBecauseBadGridCommand(self):
        failedResponse = {'status': 'Failed'}
        commands = "BAD GRID"
        self.assertEqual(execute(commands), failedResponse)

    def test_executeWithOneRoverNoMovements(self):
        commands = "5 5\n0 0 E"
        coordinates = execute(commands)
        self.assertEqual(len(coordinates), 2)

    def test_executeMultiRover(self):
        commands = "5 5\n0 0 E\nLM\n0 0 E\nMLMLM"
        coordinates = execute(commands)
        self.assertEqual(len(coordinates), 9)
        self.assertEqual(coordinates[3][0]['position'], (0, 1))
        self.assertEqual(coordinates[7][1]['position'], (1, 1))
        self.assertEqual(coordinates[8][1]['angle'], 2*math.pi/2)

    def test_executeMultiRoverFailsOnInvalidCommand(self):
        commands = "5 5\n0 0 E\nLX"
        coordinates = execute(commands)
        self.assertEqual(len(coordinates), 2)
