import random
from source.model.tetrominoe import Tetrominoe
from source.utils.variables import Configs

# a class containing methods used across the game
class GameUtils:

    # gets the tetromino matrix at type and rotation
    def getTetromino(self, type, rotation):
        return Configs.tetrominoes[type][rotation]

    # generates a random tetromino
    def getRandomTetromino(self):
        type = random.randint(0, 6)
        orientation = random.randint(0, 3)
        return Tetrominoe(type, orientation)

    # generates a new row of appropriate size
    def newRow(self):
        row = []
        for c in range(Configs.columns):
            row.append(0)
        return row