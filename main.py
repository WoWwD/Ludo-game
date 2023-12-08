from board import Board
from const import Const
from game import Game, launch
from boardnavigation import BoardNavigation, Direction
from player import Player


sizeBoard = launch()
direction = BoardNavigation(sizeBoard)

players = [
    Player(
        name=Const.player1Name,
        figure='A',
        direction=Direction.DOWN,
        movement=direction
    ),
    Player(
        name=Const.player2Name,
        figure='B',
        direction=Direction.UP,
        movement=direction
    )
]

board = Board(
    sizeBoard=sizeBoard,
    players=players
)

game = Game(
    board=board,
    players=players
)

players[0].setPosition(game.player1Base)
players[1].setPosition(game.player2Base)


def isVictory():
    for i in range(len(players)):
        if players[i].countFinishedFigures == game.countFigures:
            print(f'{players[i].name} won')
            return True


while True:
    if isVictory():
        break

    board.getBoard()
    print('------------------------------')
    for player in players:
        player.rollDice()
        for _ in range(player.currentRoll):
            if game.isFinish(player):
                break
            if game.isRoadToCenter(player):
                if ((player.x + player.currentRoll == board.middleBoard) or
                        (player.x - player.currentRoll == board.middleBoard)):
                    player.move()
                if ((player.currentRoll <= board.middleBoard - player.x) or
                        (player.currentRoll <= player.x - board.middleBoard)):
                    player.move()
            else:
                player.move()
        player.getInfo()
