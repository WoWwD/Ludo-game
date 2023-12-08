from board import Board
from const import Const
from game import Game, launch
from boardnavigation import BoardNavigation, Direction
from player import Player

sizeBoard = launch()
boardNavigation = BoardNavigation(sizeBoard)

players = [
    Player(
        name=Const.player1Name,
        figure='A',
        direction=Direction.DOWN,
        navigation=boardNavigation
    ),
    Player(
        name=Const.player2Name,
        figure='B',
        direction=Direction.UP,
        navigation=boardNavigation
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

# Setting starting positions for players
players[0].setPosition(game.player1Base)
players[1].setPosition(game.player2Base)


def movePlayer(currentPlayer):
    for _ in range(currentPlayer.currentRoll):
        if game.isFinish(currentPlayer):
            break
        # Handling steps when the player is on the final road
        if game.isOnTheFinalRoad(currentPlayer):
            if game.reachesCenterThisTurn(player) or game.canMoveToCenterWithoutOvershooting(player):
                currentPlayer.move()
        else:
            currentPlayer.move()


while True:
    board.getBoard()

    for player in players:
        player.rollDice()
        movePlayer(player)
    if game.isVictory():
        break
    else:
        game.getPlayersInfo()
