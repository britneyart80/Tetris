import pygame
pygame.init()

# controller for a game of Tetris
class GameController:

    def __init__(self, gameboard, view, sidebar, columns, rows):
        self.gameboard = gameboard
        self.view = view
        self.sidebar = sidebar
        self.gameOver = False

    def playGame(self):
        while not self.gameboard.isGameOver():
            paused = False
            if not paused:
                self.view.renderTetris()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        # pause the game on escape
                        if event.key == pygame.K_ESCAPE:
                            self.sidebar.update()
                            self.gameboard.pause()
                            paused = True
                            # if key pressed to swap hold
                        if event.key == pygame.K_f:
                            if self.gameboard.getHold():
                                print("first")
                                self.gameboard.updateHold()
                            else:
                                print("Second")
                                newhold = self.sidebar.update()
                                self.gameboard.updateHold(newhold)
                        self.view.renderTetris()

            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        # pause the game on escape
                        if event.key == pygame.K_ESCAPE:
                            self.sidebar.update()
                            self.gameboard.pause()
                            paused = False
                        self.view.renderTetris()

                self.view.renderTetris()
