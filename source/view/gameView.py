import pygame
from source.utils.variables import UIVariables, Configs
# a view for the game
class GameView:

    # initializes the game view
    def __init__(self, name, gameboard, columns, rows):
        self.gameboard = gameboard
        self.title = name + "'s Tetris Game"
        self.displayWidth = (columns * Configs.blockSize) + Configs.sidebarWidth
        self.displayHeight = rows * Configs.blockSize
        self.gameDisplay = pygame.display.set_mode((self.displayWidth, self.displayHeight))
        self.gameDisplay.fill((0,0,0))
        pygame.display.set_caption(self.title)
        self.columns = columns
        self.rows = rows

    # draws sidebar
    def drawSidebar(self):
        pygame.draw.rect(
            self.gameDisplay,
            UIVariables.sidebarColor,
            (self.displayWidth - Configs.sidebarWidth, 0, Configs.sidebarWidth, self.displayHeight)
        )

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

