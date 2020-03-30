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
        self.gameTiles = self.generateTiles()
        self.active = GameUtils().getRandomTetromino()
        self.activeCoord = [3, 0]
        self.paused = False
        self.hold = None

    #generates the game board tiles
    def generateTiles(self):
        gameboard = []
        for r in range(self.rows):
            row = []
            for c in range(self.columns):
                row.append(0)
            gameboard.append(row)
        return gameboard

    # gets the current game board block
    def getBlock(self, row, column):
        return self.gameTiles[row][column]

    # returns if the game board needs a new active tetromino
    def needsTetromino(self):
        return self.active is None

    # replaces the current active piece
    def setActive(self, tetromino):
        print("Active set to:")
        print(tetromino)
        self.active = tetromino

    # places the Tetromino onto the gameboard
    def placeTetromino(self):
        active = self.active.getMatrix()
        for r in range(4):
            for c in range(4):
                curr = active[r][c]
                if curr != 0:
                    row = self.gameTiles[r + self.activeCoord[1]]
                    row[c + self.activeCoord[0]] = curr
        self.activeCoord = [3, 0]
        self.active = None

    # determines if the current piece can move in the given direction
    def canMove(self, direction):
        active = self.active.getMatrix()
        for r in range(4):
            for c in range(4):
                curr = active[r][c]
                if direction == "right":
                    if curr != 0 and (
                            (c + self.activeCoord[0] >= 9) or
                            (curr + self.gameTiles[r + self.activeCoord[1]][c + self.activeCoord[0] + 1] > curr)):
                        return False
                elif direction == "left":
                    if curr != 0 and (
                            (c + self.activeCoord[0] - 1 < 0) or
                            (curr + self.gameTiles[r + self.activeCoord[1]][c + self.activeCoord[0] - 1] > curr)):
                        return False
                elif direction == "down":
                    if curr != 0 and (
                            (r + self.activeCoord[1] >= 19) or
                            (curr + self.gameTiles[r + self.activeCoord[1] + 1][c + self.activeCoord[0]] > curr)):
                        self.placeTetromino()
                        return False

        return True

    # move current piece in the direction given
    def moveInDirection(self, direction):
        if self.canMove(direction):
            if (direction == "left"):
                self.activeCoord = [self.activeCoord[0] - 1, self.activeCoord[1]]
            if (direction == "right"):
                self.activeCoord = [self.activeCoord[0] + 1, self.activeCoord[1]]
            if (direction == "down"):
                self.activeCoord = [self.activeCoord[0], self.activeCoord[1] + 1]

    # rotate the active piece in direction given
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
    def updateHold(self):
            temp = self.hold
            self.hold = self.active
            self.active = temp

    # gets the current hold
    def getHold(self):
        return self.hold











