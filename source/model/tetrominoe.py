from source.utils.variables import Configs
# class for a Tetromino
class Tetrominoe:

    # creates a new tetromino with the given type and rotation as well as the appropriate matrix
    def __init__(self, type, rotation):
        self.tetromino = Configs.tetrominoes[type][rotation]
        self.type = type
        self.rotation = rotation

    # returns the tetromino matrix
    def getMatrix(self):
        return self.tetromino

    # gets the type of this tetromino
    def getType(self):
        return self.type

    # gets the current rotation of this tetromino
    def getRotation(self):
        return self.rotation

    # transforms the tetromino to the new type and rotation
    def transformTetromino(self, type, rotation):
        self.tetromino = Configs.tetrominoes[type][rotation]
        self.type = type
        self.rotation = rotation
        return self
