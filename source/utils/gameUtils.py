import random
from source.model.tetrominoe import Tetrominoe


# a class containing methods used across the game
class GameUtils:

    def getRandomTetromino(self):
        type = random.randint(0, 6)
        orientation = random.randint(0, 3)
        return Tetrominoe(type, orientation)