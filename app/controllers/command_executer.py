import io
from ..grid import Grid
from ..rover import Rover
from ..modules.rover_movement import rotate, move
from ..modules.command_protocol import CommandProtocol
from ..modules.command_parser import (
        parseInitGrid,
        parseInitRover,
        validateDimensions,
        validateCommand
        )


def execute(commands):
    failedResponse = {'status': 'Failed'}
    protocol = CommandProtocol()
    buf = io.StringIO(commands)
    command = None
    command = buf.readline()
    if command == '':
        return failedResponse
    grid = initGrid(command)
    if grid == None:
        return failedResponse
    
    # BEGIN THE COMMAND LOOP
    coordinates = []
    currentRover = None
    coordinates.append(grid.getRoversStatus())
    while command != '':

        command = buf.readline().strip()
        if protocol.next() == 'rover_init':
            currentRover = initRover(command)
            if currentRover == None or not grid.appendRover(currentRover):
                return coordinates
            coordinates.append(grid.getRoversStatus())
        elif protocol.next() == 'rover_move':
            if not validateCommand(command):
                return coordinates
            coordinates = coordinates + moveRover(command, grid, currentRover)
            protocol.abortMovement()
    return coordinates
            


def initGrid(command):
    dimensions = None
    grid = None
    try:
        dimensions = parseInitGrid(command)
    except:
        pass
    if dimensions != None and validateDimensions(dimensions):
        grid = Grid(dimensions)
    return grid


def initRover(command):
   rover = None
   try:
       rover = parseInitRover(command)
   except:
       pass
   return rover

def moveRover(command, grid, rover):
    coordinates = []
    commandList = [c for c in command]
    for cmd in commandList:
        if cmd == 'M':
            newPosition = move(rover.position, rover.angle)
            if grid.validateRoverPosition(rover, newPosition):
                rover.position = newPosition
                grid.updateRoverPosition(rover, newPosition)
            else:
                return coordinates
        else:
            rover.angle = rotate(rover.angle, cmd) 
            grid.updateRoverAngle(rover, rover.angle)
        coordinates.append(grid.getRoversStatus())
    return coordinates
