from const import Const
from boardnavigation import Direction


def launch():
    print(Const.notification)
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
                print(f'{self.players[i].name} has {self.players[i].countFinishedFigures} finished figures')
                return True

    # Checking for players in the center and returning them to base
    def isFinish(self, player):
        if [player.x, player.y] == [self.board.middleBoard, self.board.middleBoard]:
            player.finish()
            if player.name == Const.player1Name:
                player.setPosition(self.player1Base)
            if player.name == Const.player2Name:
                player.setPosition(self.player2Base)

    # Logic for the behavior of the figures when they reach the final road
    def isOnTheFinalRoad(self, player):
        # Way for the first player only
        if player.name == Const.player1Name:
            isOnTheFinalRoad = player.x <= self.board.middleBoard and player.y == self.board.middleBoard
            if isOnTheFinalRoad:
                if player.direction != Direction.DOWN:
                    player.direction = Direction.DOWN
            return isOnTheFinalRoad
        # Way for the second player only
        if player.name == Const.player2Name:
            isOnTheFinalRoad = player.x >= self.board.middleBoard and player.y == self.board.middleBoard
            if isOnTheFinalRoad:
                if player.direction != Direction.UP:
                    player.direction = Direction.UP
            return isOnTheFinalRoad

    def getPlayersInfo(self):
        for player in self.players:
            print('')
            print(f'{player.name}: {player.getCurrentPosition()}')
            print(f'Roll: {player.currentRoll}')
            print(f'Count finished figures: {player.countFinishedFigures}')
            print('')

    # The function determines whether the first or second player will reach the center on the current dice roll
    def reachesCenterThisTurn(self, player):
        firstPlayer = player.x + player.currentRoll == self.board.middleBoard
        secondPlayer = player.x - player.currentRoll == self.board.middleBoard
        if firstPlayer or secondPlayer:
            return True

    # The function determines whether the first or second player will overshoot the center on the current dice roll
    def canMoveToCenterWithoutOvershooting(self, player):
        firstPlayer = player.currentRoll <= self.board.middleBoard - player.x
        secondPlayer = player.currentRoll <= player.x - self.board.middleBoard
        if firstPlayer or secondPlayer:
            return True
