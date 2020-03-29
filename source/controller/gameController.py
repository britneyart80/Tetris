import pygame
pygame.init()
from source.utils.variables import Configs

# controller for a game of Tetris
class GameController:

    def __init__(self, gameboard, view, sidebar, columns, rows):
        self.gameboard = gameboard
        self.view = view
        self.sidebar = sidebar
        self.gameOver = False
        self.paused = False
        self.fps = Configs.fps

    def playGame(self):

        moveDown = pygame.USEREVENT + 1
        pygame.time.set_timer(moveDown, 1000)
        # while the game is not over yet
        while not self.gameboard.isGameOver():
            if not self.paused:
                for event in pygame.event.get():
                    if event.type == moveDown:
                        self.gameboard.moveDown()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        # pause the game on escape
                        if event.key == pygame.K_ESCAPE:
                            self.gameboard.pause()
                            self.paused = True
                        # if key pressed, swap hold with active piece
                        if event.key == pygame.K_f:
                            if self.gameboard.getHold():
                                self.gameboard.updateHold()
                            else:
                                firstSwap = self.sidebar.update()
                                self.gameboard.updateHold(firstSwap)
                        # directional
                        if event.key == pygame.K_LEFT:
                            self.gameboard.moveInDirection("left")
                        if event.key == pygame.K_RIGHT:
                            self.gameboard.moveInDirection("right")
                        if event.key == pygame.K_DOWN:
                            self.gameboard.moveInDirection("down")
                        if event.key == pygame.K_a:
                            self.gameboard.rotateActive("left")
                        if event.key == pygame.K_d:
                            self.gameboard.rotateActive("right")
                self.view.renderTetris()

            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        # pause the game on escape
                        if event.key == pygame.K_ESCAPE:
                            self.gameboard.pause()
                            self.paused = False
                        self.view.renderTetris()

                self.view.renderTetris()
