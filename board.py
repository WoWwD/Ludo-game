class Board:
    def __init__(self, sizeBoard, players):
        self.sizeBoard = sizeBoard
        self.players = players
        self.middleBoard = sizeBoard // 2

    def getBoard(self):
        for i in range(self.sizeBoard + 1):
            for j in range(self.sizeBoard + 1):
                if i == 0 and j == 0:
                    print(' ', end=' ')
                # Drawing coordinates on the top
                elif i == 0:
                    print((j - 1) % 10, end=' ')
                # Drawing coordinates on the down
                elif j == 0:
                    print((i - 1) % 10, end=' ')
                else:
                    playersOnCell = self.isPlayersOnCell(i - 1, j - 1)
                    if playersOnCell:
                        print(playersOnCell, end=' ')
                    elif self.isCenter(i - 1, j - 1):
                        print('X', end=' ')
                    elif self.isRoad(i - 1, j - 1):
                        print('*', end=' ')
                    elif self.isFinishRoad(i - 1, j - 1):
                        print('D', end=' ')
                    else:
                        print(' ', end=' ')
            print()

    def isRoad(self, i, j):
        mainRoad = (j in [self.middleBoard - 1, self.middleBoard + 1] or
                    i in [self.middleBoard - 1, self.middleBoard + 1])

        axis = ((i == self.middleBoard and j in [0, self.sizeBoard - 1]) or
                (j == self.middleBoard and i in [0, self.sizeBoard - 1]))

        notSpecialCells = not (i, j) in [
            (self.middleBoard + 1, self.middleBoard),
            (self.middleBoard - 1, self.middleBoard),
            (self.middleBoard, self.middleBoard + 1),
            (self.middleBoard, self.middleBoard - 1)
        ]

        return (mainRoad or axis) and notSpecialCells

    def isFinishRoad(self, i, j):
        return j == self.middleBoard or i == self.middleBoard

    def isCenter(self, i, j):
        return j == self.middleBoard and i == self.middleBoard

    def isPlayer(self, i, j, t):
        return i == self.players[t].x and j == self.players[t].y

    def isPlayersOnCell(self, i, j):
        figures = ''
        for t in range(len(self.players)):
            if self.isPlayer(i, j, t):
                figures += self.players[t].figure
        return figures
