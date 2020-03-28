from source.utils.enums.difficulty import Difficulty
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

    def isGameOver(self):
        return self.gameover









