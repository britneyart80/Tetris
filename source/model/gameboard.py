from source.utils.gameUtils import GameUtils
import random

# model for Tetris game board
class Gameboard:

    # initializes the game board
    # @param gameMode: the difficulty of the game of type DIFFICULTY (enum)
    # @param columns: number of cols in the game
    # @param rows: number of rows in the game
    # score: current score of the game
    # isGameOver: boolean to check game over
    def __init__(self, gameMode, columns, rows):
        self.gameMode = gameMode
        self.columns = columns
        self.rows = rows
        self.score = 0
        self.gameover = False
        self.active = GameUtils().getRandomTetromino()
        self.activeCoord = [4, 0]
        self.paused = False
        self.hold = None

    def moveInDirection(self, direction):
        if (direction == "left"):
            self.activeCoord = [self.activeCoord[0] - 1, self.activeCoord[1]]
        if (direction == "right"):
            self.activeCoord = [self.activeCoord[0] + 1, self.activeCoord[1]]
        if (direction == "down"):
            self.activeCoord = [self.activeCoord[0], self.activeCoord[1] + 1]

    def rotateActive(self, direction):
        typeIndex = self.active.getType()
        rotationIndex = self.active.getRotation()
        if direction == "right":
            self.active = self.active.transformTetromino(typeIndex, (rotationIndex + 1) % 4)
        if direction == "left":
            self.active = self.active.transformTetromino(typeIndex, (rotationIndex - 1) % 4)

    # moves all movable blocks down on clock tick
    def moveDown(self):
        self.activeCoord = [self.activeCoord[0], self.activeCoord[1] + 1]

    # retrieves the current position of the active piece
    def getActiveCoord(self):
        return self.activeCoord

    # retrieves the current active piece
    def getActivePieceMatrix(self):
        return self.active.getMatrix()

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
    def updateHold(self, firstSwap=False):
        # if it is the first swap, put active in hold and take from up next
        if firstSwap:
            self.hold = self.active
            self.active = firstSwap
        # otherwise swap the current hold with the current piece
        else:
            temp = self.hold
            self.hold = self.active
            self.active = temp

    # gets the current hold
    def getHold(self):
        return self.hold











