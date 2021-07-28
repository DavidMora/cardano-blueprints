class Rover:
    currentId = 0
    '''
    The Rover class is a container to describe the model. In a real world application
    it would have a link to the db and allow an object representation via SQLAlchemy or
    DJango's ORM or any other? 
    '''
    def __init__(self, position: tuple, angle: float):
        self.position = position
        self.angle = angle
        self.id = Rover.currentId
        Rover.currentId += 1
