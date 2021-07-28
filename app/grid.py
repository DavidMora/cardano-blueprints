from app.rover import Rover

class Grid:
    '''
    The Grid class is a container to describe the model for the grid. In a real world application
    it would have a link to the db and allow an object representation via SQLAlchemy or
    DJango's ORM or any other? 
    '''
    def __init__(self, dimensions: tuple):
        self.dimensions = dimensions
        self.rovers = []
    
    def appendRover(self, rover: Rover):
        if (self.validateRoverPosition(rover, rover.position)):
            self.rovers.append(rover)
            return True
        return False

    def validateRoverPosition(self, rover: Rover, position: tuple):
        if (position[0] >= self.dimensions[0] or
           position[0] < 0 or
           position[1] >= self.dimensions[1] or
           position[1] < 0):
               return False
        if len([fRover for fRover in self.rovers if fRover.position == position and fRover.id != rover.id ]) > 0:
            return False
        return True
    
    def updateRoverPosition(self, rover: Rover, position: tuple):
        refRover = next((fRover for fRover in self.rovers if fRover.id == rover.id), None)
        if isinstance(refRover, Rover):
                refRover.position = position
                return True
        return False

    def updateRoverAngle(self, rover: Rover, angle: int):
        refRover = next((fRover for fRover in self.rovers if fRover.id == rover.id), None)
        if isinstance(refRover, Rover):
            refRover.angle = angle
            return True
        return False

    def getRoversStatus(self):
        roverList = []
        for rover in self.rovers:
            roverList.append(
                        {
                            'id': rover.id,
                            'position': rover.position,
                            'angle': rover.angle
                        }
                    )
        return roverList
