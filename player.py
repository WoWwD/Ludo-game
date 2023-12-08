import random
from boardnavigation import Direction


class Player:
    def __init__(self, name, figure, direction, movement):
        self.name = name
        self.figure = figure
        self.x = 0
        self.y = 0
        self.direction = direction
        self.countFinishedFigures = 0
        self.currentRoll = 0
        self.movement = movement

    # Function for movement, first the direction is determined and then a step is taken
    def move(self):
        self.direction = self.movement.isTurn([self.x, self.y], self.direction)
        if self.direction == Direction.DOWN:
            self.x += 1
        if self.direction == Direction.UP:
            self.x -= 1
        if self.direction == Direction.RIGHT:
            self.y += 1
        if self.direction == Direction.LEFT:
            self.y -= 1

    def getCurrentPosition(self):
        return [self.x, self.y]

    # It's called when the player reaches the center
    def finish(self):
        self.countFinishedFigures += 1

    def setPosition(self, position):
        self.x = position[0]
        self.y = position[1]

    def rollDice(self):
        self.currentRoll = random.randint(1, 6)

    def getInfo(self):
        print('')
        print(f'{self.name}: {self.getCurrentPosition()}')
        print(f'Roll: {self.currentRoll}')
        print(f'Count finished figures: {self.countFinishedFigures}')
        print('')
