from source.utils.gameUtils import GameUtils
from source.utils.variables import Configs
# model for Tetris game board
class Gameboard:

    # initializes the game board
    # @param gameMode: the difficulty of the game of type DIFFICULTY (enum)
    # @param columns: number of cols in the game
    # @param rows: number of rows in the game
    # score: current score of the game
    # isGameOver: boolean to check game over
    def __init__(self, gameMode, columns, rows):
        self.level = 1
        self.gameMode = gameMode
        self.columns = columns
        self.rows = rows
        self.score = 0
        self.gameOver = False
        self.gameTiles = self.generateTiles()
        self.active = GameUtils().getRandomTetromino()
        self.activeCoord = [3, -1]
        self.paused = False
        self.usedHold = False;
        self.hold = None
        self.lastMove = 0

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
        self.active = tetromino

    # calculates the score added
    def updateScore(self, rowCount):
        self.score += rowCount * 100 * self.level

    # checks which parts of the board can be cleared
    def checkCleared(self):
        fullRow = []
        for r in range(self.rows):
            isFull = True
            for c in range(self.columns):
                if self.gameTiles[r][c] == 0:
                    isFull = False
                    break;
            if isFull:
                fullRow.append(True)
            else:
                fullRow.append(False)

        rowCount = 0
        for i in range(len(fullRow)):
            isFullRow = fullRow[i]
            if isFullRow:
                rowCount += 1
                self.gameTiles.pop(i)
                self.gameTiles.insert(0, GameUtils().newRow())
        self.updateScore(rowCount)



    # places the Tetromino onto the gameboard
    def placeTetromino(self):
        active = self.active.getMatrix()
        for r in range(4):
            for c in range(4):
                curr = active[r][c]
                if curr != 0:
                    row = self.gameTiles[r + self.activeCoord[1]]
                    row[c + self.activeCoord[0]] = curr
        self.activeCoord = [3, -1]
        self.active = None
        self.usedHold = False;
        self.score += self.level
        self.checkCleared()

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

    # determines if the piece can be rotated
    def canRotate(self, direction):
        for r in range(4):
            for c in range(4):
                if direction == "right":
                    nextRotation = GameUtils().getTetromino(self.active.getType(), (self.active.getRotation() + 1) % 4)
                if direction == "left":
                    nextRotation = GameUtils().getTetromino(self.active.getType(), (self.active.getRotation() - 1) % 4)

                curr = nextRotation[r][c]
                if curr != 0 and (
                        (c + self.activeCoord[0] > 9) or (c + self.activeCoord[0] < 0) or
                        (curr + self.gameTiles[r + self.activeCoord[1]][c + self.activeCoord[0]] > curr)):
                    return False
        return True

    # rotate the active piece in direction given
    def rotateActive(self, direction):
        typeIndex = self.active.getType()
        rotationIndex = self.active.getRotation()
        if direction == "right" and self.canRotate("right"):
            self.active = self.active.transformTetromino(typeIndex, (rotationIndex + 1) % 4)
        if direction == "left" and self.canRotate("left"):
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
        for c in range(4):
            if self.gameTiles[0][c + 3] != 0:
                self.gameOver = True
                return True
        return False

    # refreshes the gameboard
    def newGame(self):
        self.score = 0
        self.gameOver = False
        self.gameTiles = self.generateTiles()
        self.active = GameUtils().getRandomTetromino()
        self.activeCoord = [3, -1]
        self.paused = False
        self.usedHold = False;
        self.hold = None

    # gets the current score of the game
    def getScore(self):
        return self.score

    # updates the current hold
    def updateHold(self):
        if not self.usedHold:
            temp = self.hold
            self.hold = self.active
            self.active = temp
            self.activeCoord = [3, -1]
        self.usedHold = True;

    # gets the current hold
    def getHold(self):
        return self.hold











