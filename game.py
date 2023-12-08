from const import Const
from boardnavigation import Direction


def launch():
    print(Const.notification)
    print()
    while True:
        return int(input("Enter board size: "))


class Game:
    def __init__(self, board, players):
        self.players = players
        self.board = board
        self.countFigures = (board.sizeBoard - 3) // 2
        self.player1Base = [0, board.middleBoard + 1]
        self.player2Base = [board.sizeBoard - 1, board.middleBoard - 1]

    # After each move, the function checks for each player the number of figures, that reached the center
    def isVictory(self):
        for i in range(len(self.players)):
            if self.players[i].countFinishedFigures == self.countFigures:
                print(f'{self.players[i].name} won')
                return True

    # Checking for players in the center and returning them to base
    def isFinish(self, player):
        if [player.x, player.y] == [self.board.middleBoard, self.board.middleBoard]:
            player.finish()
            if player.name == Const.player1Name:
                player.setPosition(self.player1Base)
            if player.name == Const.player2Name:
                player.setPosition(self.player2Base)

    def isRoadToCenter(self, player):
        if player.name == Const.player1Name:
            result = player.x <= self.board.middleBoard and player.y == self.board.middleBoard
            if result:
                if player.direction != Direction.DOWN:
                    player.direction = Direction.DOWN
            return result
        if player.name == Const.player2Name:
            result = player.x >= self.board.middleBoard and player.y == self.board.middleBoard
            if result:
                if player.direction != Direction.UP:
                    player.direction = Direction.UP
            return result
