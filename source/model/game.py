from source.model.gameboard import Gameboard

# a game of Tetris
class Game:

    # initializing a game
    # @param difficulty: difficulty of the game (enum)
    def __init__(self, difficulty, columns, rows):
        self.difficulty = difficulty
        self.gameOver = False
        self.gameBoard = Gameboard(difficulty, columns, rows)

    def isGameOver(self):
        return self.gameOver

