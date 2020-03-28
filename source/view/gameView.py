import pygame
from source.utils.variables import UIVariables, Configs
# a view for the game
class GameView:

    # initializes the game view
    def __init__(self, name, gameboard, sidebar, columns, rows):
        self.gameboard = gameboard
        self.sidebar = sidebar
        self.title = name + "'s Tetris Game"
        self.displayWidth = (columns * Configs.blockSize) + Configs.sidebarWidth
        self.displayHeight = rows * Configs.blockSize
        # starting x coordinate for the sidebar
        self.sidebar_dx = self.displayWidth - Configs.sidebarWidth
        self.gameDisplay = pygame.display.set_mode((self.displayWidth, self.displayHeight))
        self.gameDisplay.fill((0,0,0))
        pygame.display.set_caption(self.title)
        self.columns = columns
        self.rows = rows


    # draws the tetromino in the appropriate upNext slot
    def drawTetromino(self, index, tetromino, isSidebar):
       if isSidebar:
            for r in range(4):
                row = tetromino[r]
                for c in range(4):
                    dx = self.sidebar_dx + Configs.blockSize + (c * Configs.sidebarBlockSize)
                    dy = (index * Configs.sidebarBlockSize * 4.5) + (r * Configs.sidebarBlockSize) + (Configs.blockSize * 3)
                    if tetromino[r][c] != 0:
                        pygame.draw.rect(
                            self.gameDisplay,
                            UIVariables.tetrominoColors[tetromino[r][c] - 1],
                            (dx + 1, dy + 1, Configs.sidebarBlockSize - 2, Configs.sidebarBlockSize - 2)
                        )






    # draws sidebar
    def drawSidebar(self):
        pygame.draw.rect(
            self.gameDisplay,
            UIVariables.sidebarColor,
            (self.sidebar_dx, 0, Configs.sidebarWidth, self.displayHeight)
        )

        # draw background for upNext pieces
        pygame.draw.rect(
            self.gameDisplay,
            UIVariables.gray,
            (self.sidebar_dx + (Configs.blockSize * 0.5),
             Configs.blockSize * 2.5,
             Configs.sidebarBlockSize * 5,
             Configs.sidebarBlockSize * 15)
        )
        upNext = self.sidebar.upNext
        for i in range(3):
            tetromino = upNext[i]
            self.drawTetromino(i, tetromino, True)



    # draws the game board with tiles
    def drawGameboard(self):
        for c in range(self.columns):
            for r in range(self.rows):
                dx = c * Configs.blockSize
                dy = r * Configs.blockSize
                pygame.draw.rect(
                    self.gameDisplay,
                    UIVariables.gray,
                    (dx + 2, dy + 2, Configs.blockSize - 4, Configs.blockSize - 4))


    # renders everything on the game board
    def renderTetris(self):
        self.drawSidebar()
        self.drawGameboard()
        pygame.display.update()

