import pygame

# controller for a game of Tetris
class GameController:

    def __init__(self, gameboard, view, columns, rows):
        self.gameboard = gameboard
        self.view = view
        self.gameOver = False

    def playGame(self):
        while not self.gameboard.isGameOver():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.view.renderTetris()
