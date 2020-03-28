from source.utils.tetrominoe import Tetrominoe

# A sidebar for menu and next pieces
class Sidebar:

    def __init__(self):
        self.isMenu = False
        self.upNext = self.generateUpNext()

    def generateUpNext(self):
        upNext = []
        for num in range(3):
            upNext.append(Tetrominoe().getRandomTetromino())
        return upNext


