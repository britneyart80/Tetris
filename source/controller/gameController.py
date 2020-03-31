import pygame
pygame.init()

# controller for a game of Tetris
class GameController:

    # initialize the game controller
    def __init__(self, gameboard, view, sidebar, columns, rows):
        self.playing = True
        self.gameboard = gameboard
        self.view = view
        self.sidebar = sidebar
        self.gameOver = False
        self.paused = False
        self.lastMove = 0
        self.speed = 0

    # plays the game of tetris
    def playGame(self):
        moveDown = pygame.USEREVENT + 1
        # levelUp = pygame.USEREVENT + 2
        # pygame.time.set_timer(levelUp, 5000)
        pygame.time.set_timer(moveDown, 1000)

        while self.playing:
            if self.gameboard.isGameOver():
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.gameboard.newGame()
                self.view.renderTetris()
            elif not self.paused:
                for event in pygame.event.get():
                    if event.type == moveDown:
                        self.gameboard.moveInDirection("down")
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
                            self.gameboard.updateHold()
                        # rotations
                        if event.key == pygame.K_a:
                            self.gameboard.rotateActive("left")
                        if event.key == pygame.K_d:
                            self.gameboard.rotateActive("right")
                        # hard drop
                        if event.key == pygame.K_SPACE:
                            while self.gameboard.canMove("down"):
                                ms = pygame.time.get_ticks()
                                if ms > self.lastMove + 5:
                                    self.lastMove = ms
                                    self.gameboard.moveInDirection("down")
                                    self.view.renderTetris()
                # moving the tetris piece
                keys = pygame.key.get_pressed()
                ms = pygame.time.get_ticks()
                if ms > self.lastMove + 110:
                    if keys[pygame.K_LEFT]:
                        self.gameboard.moveInDirection("left")
                    if keys[pygame.K_RIGHT]:
                        self.gameboard.moveInDirection("right")
                    if keys[pygame.K_DOWN]:
                        self.gameboard.moveInDirection("down")
                    self.lastMove = ms

                if self.gameboard.needsTetromino():
                    next = self.sidebar.update()
                    self.gameboard.setActive(next)
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
