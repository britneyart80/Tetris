import pygame

# controller for a game of Tetris
class GameController:

    def __init__(self, model, view, columns, rows):
        self.game = model
        self.view = view
        self.gameOver = False

    def playGame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            self.view.render()