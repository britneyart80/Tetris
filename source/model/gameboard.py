from source.utils.enums.difficulty import Difficulty
from source.utils.tetrominoe import Tetrominoe
from source.model.tile import Tile

# model for Tetris game board
class Gameboard:

    # initializes the game board
    # @param gameMode: the difficulty of the game of type DIFFICULTY (enum)
    # @param columns: number of cols in the game
    # @param rows: number of rows in the game
    # gameTiles: the game tiles on the board
    # score: current score of the game
    # isGameOver: boolean to check game over
    def __init__(self, gameMode, columns, rows):
        self.gameMode = gameMode
        self.columns = columns
        self.rows = rows
        self.gameTiles = self.generateTiles(columns, rows)
        self.score = 0
        self.gameover = False
        self.currentPiece = Tetrominoe().getRandomTetromino()
        self.paused = False
        self.hold = None

    # generates the tiles on the board
    # @param columns: number of cols to generate tiles for
    # @param rows: number of rows to generate tiles for
    def generateTiles(self, columns, rows):
        tiles = []
        for c in range(columns):
            column = []
            for r in range(rows):
                column.append(Tile(c, r))
            tiles.append(column)
        return tiles

    # pause the game
    def pause(self):
        self.paused = not self.paused

    # returns if the game is over
    def isGameOver(self):
        return self.gameover

    # gets the current score of the game
    def getScore(self):
        return self.score

    # updates the current hold
    def updateHold(self, replace=False):
        # if specified replace hold, replace hold with that
        if replace:
            self.hold = replace
            print("replace")
        # otherwise swap the current hold with the current piece
        else:
            print("swap")
            print(self.currentPiece)
            temp = self.hold
            self.hold = self.currentPiece
            self.currentPiece = temp


    # gets the current hold
    def getHold(self):
        return self.hold











