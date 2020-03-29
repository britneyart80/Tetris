import pygame
pygame.init()
from source.utils.variables import UIVariables, Configs
# a view for the game
class GameView:

    # initializes the game view
    def __init__(self, name, gameboard, sidebar, columns, rows):
        self.gameboard = gameboard
        self.sidebar = sidebar
        self.title = name + "'s Tetris Game"
        self.displayWidth = Configs.gameboardWidth + Configs.sidebarWidth + 4
        self.displayHeight = rows * Configs.blockSize + 4
        # starting x coordinate for the sidebar
        self.sidebar_dx = self.displayWidth - Configs.sidebarWidth
        self.gameDisplay = pygame.display.set_mode((self.displayWidth, self.displayHeight))
        self.gameDisplay.fill((0,0,0))
        pygame.display.set_caption(self.title)
        self.columns = columns
        self.rows = rows

    # clears the gameboard
    def clear(self):
        display = pygame.display.get_surface()
        display.fill((0, 0, 0))

    # draws the tetromino in the appropriate upNext slot
    def drawSidebarTetromino(self, index, tetromino):
            for r in range(4):
                for c in range(4):
                    dx = self.sidebar_dx + Configs.blockSize + (c * Configs.sidebarBlockSize)
                    dy = (index * Configs.sidebarBlockSize * 4.5) + (r * Configs.sidebarBlockSize) + (Configs.blockSize * 3.5)
                    if tetromino[r][c] != 0:
                        pygame.draw.rect(
                            self.gameDisplay,
                            UIVariables.tetrominoColors[tetromino[r][c] - 1],
                            (dx + 1, dy + 1, Configs.sidebarBlockSize - 2, Configs.sidebarBlockSize - 2)
                        )

    # draw the tetromino given
    def drawTetromino(self, tetromino, coord):
        for r in range(4):
            for c in range(4):
                dx = coord[0] * Configs.blockSize + (c * Configs.blockSize) + 2
                dy = coord[1] * Configs.blockSize + (r * Configs.blockSize) + 2
                if tetromino[r][c] != 0:
                    pygame.draw.rect(
                            self.gameDisplay,
                            UIVariables.tetrominoColors[tetromino[r][c] - 1],
                            (dx + 2, dy + 2, Configs.blockSize - 4, Configs.blockSize - 4)
                    )

    # draw the current active piece on the board
    def drawCurrentPiece(self):
        position = self.gameboard.getActiveCoord()
        activePiece = self.gameboard.getActivePiece()
        self.drawTetromino(activePiece, position)

    # draws sidebar
    def drawSidebar(self):
        # sidebar background
        pygame.draw.rect(
            self.gameDisplay,
            UIVariables.sidebarColor,
            (self.sidebar_dx, 0, Configs.sidebarWidth, self.displayHeight)
        )

        # draw up next pieces
        upNext = self.sidebar.upNext
        for i in range(3):
            tetromino = upNext[i]
            self.drawSidebarTetromino(i, tetromino)

        # SIDEBAR TEXT --------------------
        # TETRIS title
        title = UIVariables.fontTitle.render("TETRIS", 1, UIVariables.tetrominoColors[6])
        self.gameDisplay.blit(title, (self.sidebar_dx + Configs.sidebarBlockSize, Configs.sidebarBlockSize * 1))
        # up next text
        upNextText = UIVariables.fontReg.render("UP NEXT", 1, UIVariables.gray)
        self.gameDisplay.blit(upNextText,
                              (self.sidebar_dx + (Configs.sidebarBlockSize * 1.5), Configs.sidebarBlockSize * 4))

        # draw held piece
        holdText = UIVariables.fontReg.render("HOLD", 1, UIVariables.gray)
        self.gameDisplay.blit(holdText,
                              (self.sidebar_dx + (Configs.sidebarBlockSize * 2), Configs.sidebarBlockSize * 21))
        pygame.draw.rect(
            self.gameDisplay,
            UIVariables.gray,
            (self.sidebar_dx + Configs.sidebarBlockSize / 2,
             Configs.sidebarBlockSize * 23,
             Configs.sidebarBlockSize * 6,
             Configs.sidebarBlockSize * 6)
        )
        if self.gameboard.getHold():
            held = self.gameboard.getHold()
            for r in range(4):
                for c in range(4):
                    dx = self.sidebar_dx + Configs.blockSize + (c * Configs.sidebarBlockSize)
                    dy = (Configs.sidebarBlockSize * 24) + (r * Configs.sidebarBlockSize)
                    if held[r][c] != 0:
                        pygame.draw.rect(
                            self.gameDisplay,
                            UIVariables.tetrominoColors[held[r][c] - 1],
                            (dx + 1, dy + 1, Configs.sidebarBlockSize - 2, Configs.sidebarBlockSize - 2)
                        )

        # Score text
        scoreText = UIVariables.fontReg.render("SCORE", 1, UIVariables.gray)
        scoreNum = self.gameboard.getScore()
        scoreNumText = UIVariables.fontTitle.render(str(scoreNum), 1, UIVariables.lightGray)
        self.gameDisplay.blit(scoreText,
                              (self.sidebar_dx + (Configs.sidebarBlockSize * 2), Configs.sidebarBlockSize * 30))
        self.gameDisplay.blit(scoreNumText,
                              (self.sidebar_dx + (Configs.sidebarBlockSize * 3), Configs.sidebarBlockSize * 31.5))



    # draws the game board with tiles
    def drawGameboard(self):
        for c in range(self.columns):
            for r in range(self.rows):
                dx = c * Configs.blockSize + 2
                dy = r * Configs.blockSize + 2
                pygame.draw.rect(
                    self.gameDisplay,
                    UIVariables.gray,
                    (dx + 2, dy + 2, Configs.blockSize - 4, Configs.blockSize - 4))

    # renders everything on the game board
    def renderTetris(self):
        if self.gameboard.paused:
            self.drawSidebar()
            self.drawGameboard()
            pauseText = UIVariables.fontPause.render("PAUSED", 1, (0, 0, 0))
            pauseScreen = pygame.Surface((Configs.gameboardWidth + 4, self.displayHeight)).convert_alpha()
            pauseScreen.fill((255, 255, 255, 230))
            self.gameDisplay.blit(pauseScreen, (0, 0))
            self.gameDisplay.blit(pauseText, (Configs.blockSize * 2.2, self.displayHeight / 2.3))
        else:
            self.clear()
            self.drawSidebar()
            self.drawGameboard()
            self.drawCurrentPiece()
        pygame.display.update()

