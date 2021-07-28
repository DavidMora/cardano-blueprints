import math
import re
from app.rover import Rover


def parseInitGrid(cmdLine: str):
    data = cmdLine.split()
    dimensions = None
    if len(data) != 2:
        raise Exception(
                'WRONG INIT GRID COMMAND - INVALID NUMBER OF ATTRIBUTES'
                )
    try:
        dimensions = (
                    int(data[0]),
                    int(data[1])
             )
    except ValueError:
        raise ValueError('ATTRIBUTES MUST BE NUMERIC')
    return dimensions


def parseInitRover(cmdLine: str):
    data = cmdLine.split()
    position = None
    if len(data) != 3:
        raise Exception(
                'WRONG INIT ROVER COMMAND - INVALID NUMBER OF ATTRIBUTES'
                )
    try:
        position = (
                    int(data[0]),
                    int(data[1])
             )
    except ValueError:
        raise ValueError('POSITION ATTRIBUTES MUST BE NUMERIC')
    return Rover(position, cardinalToAngle(data[2]))


def validateDimensions(dimensions: str):
    if dimensions[0] > 0 and dimensions[1] > 0:
        return True
    return False


def validateCommand(cmdLine: str):
    search=re.compile(r'[^LMR.]').search
    return not bool(search(cmdLine))


def cardinalToAngle(cardinal: str):
    cardinal_to_angle = {'E': 0, 'N': math.pi/2, 'W': math.pi, 'S': 3*math.pi/2}
    angle = cardinal_to_angle.get(cardinal)
    if angle == None:
        raise Exception('VALID CARDINAL DIRECTIONS ARE: E, N, W, S')
    return angle
