from app.modules.command_parser import (
    parseInitGrid,
    parseInitRover,
    validateCommand, 
    validateDimensions,
    cardinalToAngle
)

class CommandProtocol:
    def __init__(self):
        self.current = 'grid_init'

    def next(self):
        if self.current == 'grid_init':
            self.current = 'rover_init'
        elif self.current == 'rover_init':
            self.current = 'rover_move'
        elif self.current == 'rover_move':
            self.current = 'rover_move'
        elif self.current == 'rover_move_end':
            self.current = 'rover_init'
        return self.current
    
    def abortMovement(self):
        self.current = 'rover_move_end'


