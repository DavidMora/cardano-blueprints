import math


def rotate(currentAngle: float, direction: str):
    angle = currentAngle
    if direction == 'L':
        angle = angle + math.pi/2
    elif direction == 'R':
        angle = angle - math.pi/2
    return angle


def move(currentPosition: tuple, currentAngle: float):
    return (
                currentPosition[0] + round(math.cos(currentAngle)),
                currentPosition[1] + round(math.sin(currentAngle))
            )
