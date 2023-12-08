from enum import Enum


# The file contains the functions necessary to determine the rotation on the board
# It also contains logic, that sets directions depending on coordinates

class Direction(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    UP = "UP"
    DOWN = "DOWN"


class BoardNavigation:
    def __init__(self, sizeBoard):
        self.sizeBoard = sizeBoard
        self.middleBoard = sizeBoard // 2

    # If there isn't turn, then current direction will be returned
    def isTurn(self, position, currentDirection):
        if self.isTurnRight(position):
            return Direction.RIGHT
        if self.isTurnLeft(position):
            return Direction.LEFT
        if self.isTurnUp(position):
            return Direction.UP
        if self.isTurnDown(position):
            return Direction.DOWN
        return currentDirection

    def isTurnDown(self, position):
        return position in [
            [0, self.middleBoard + 1],
            [self.middleBoard - 1, self.sizeBoard - 1],
            [self.middleBoard + 1, self.middleBoard + 1]
        ]

    def isTurnUp(self, position):
        return position in [
            [self.sizeBoard - 1, self.middleBoard - 1],
            [self.middleBoard + 1, 0],
            [self.middleBoard - 1, self.middleBoard - 1]
        ]

    def isTurnRight(self, position):
        return position in [
            [self.middleBoard - 1, self.middleBoard + 1],
            [self.middleBoard - 1, 0],
            [0, self.middleBoard - 1]
        ]

    def isTurnLeft(self, position):
        return position in [
            [self.middleBoard + 1, self.sizeBoard - 1],
            [self.sizeBoard - 1, self.middleBoard + 1],
            [self.middleBoard + 1, self.middleBoard - 1]
        ]
