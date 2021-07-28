import math
import unittest

from app.modules.command_parser import (
    parseInitGrid,
    parseInitRover,
    validateCommand, 
    validateDimensions,
    cardinalToAngle
)

class ModulesRoverTestCase(unittest.TestCase):
    def test_parseInitGridCommandLenght(self):
        with self.assertRaises(Exception):
            parseInitGrid('COMMAND SIZE DOESNT MATCH')
        with self.assertRaises(Exception):
            parseInitGrid('SIZE DOESNT MATCH')
        with self.assertRaises(Exception):
            parseInitGrid('MATCH')
    
    def test_parseInitGridCommandIsNumeric(self):
        with self.assertRaises(ValueError):
            parseInitGrid('M M')
        with self.assertRaises(ValueError):
            parseInitGrid('M 5')

    def test_parseInitGridReturnsTuple(self):
        dimensions = parseInitGrid('5 5')
        self.assertIsInstance(dimensions, tuple)

    def test_parseInitGridReturnsNumbers(self):
        dimensions = parseInitGrid('5 6')
        self.assertEqual(dimensions[0], 5)
        self.assertEqual(dimensions[1], 6)

    def test_validateDimensionsIsFalse(self):
        self.assertFalse(validateDimensions((0,1)))
        self.assertFalse(validateDimensions((-1,1)))
        self.assertFalse(validateDimensions((1,0)))
        self.assertFalse(validateDimensions((1,-1)))

    def test_validateDimensionsIsTrue(self):
        self.assertTrue(validateDimensions((1,1)))

    def test_cadinalToAngleRaises(self):
        with self.assertRaises(Exception):
            cadinalToAngle('NE')
            cadinalToAngle('ANY OTHER THING')

    def test_cadinalToAngleIsValidAngle(self):
        self.assertEqual(cardinalToAngle('E'), 0)
        self.assertEqual(cardinalToAngle('N'), math.pi/2)
        self.assertEqual(cardinalToAngle('W'), math.pi)
        self.assertEqual(cardinalToAngle('S'), 3*math.pi/2)

    def test_parseInitRover(self):
        self.assertEqual(parseInitRover('0 1 E').position, (0,1))
        self.assertEqual(parseInitRover('0 1 E').angle, 0)

    def test_parseInitRoverRaisesException(self):
        with self.assertRaises(Exception):
            parseInitRover('COMMAND SIZE DOESNT MATCH')
        with self.assertRaises(Exception):
            parseInitRover('DOESNT MATCH')
        with self.assertRaises(Exception):
            parseInitRover('MATCH')

    def test_parseInitRoverRaisesValueError(self):
        with self.assertRaises(ValueError):
            parseInitRover('M M E')
        with self.assertRaises(ValueError):
            parseInitRover('M 5 E')

    def test_parseInitRoverRaisesException2(self):
        with self.assertRaises(Exception):
            parseInitRover('1 1 J')

    def test_validateCommand(self):
        self.assertTrue(validateCommand('MMLLRRLLMMMM'))
        self.assertFalse(validateCommand(' MMLLRRLLMMMMQWERTY'))
        self.assertTrue(validateCommand(''))
