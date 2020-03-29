from source.utils.tetrominoe import Tetrominoe

# A sidebar for menu and next pieces
class Sidebar:

    # initializes a sidebar or menu depending on current game state
    def __init__(self):
        self.isMenu = False
        self.upNext = self.generateUpNext()

    # randomly generates 3 tetrominoes that are coming up next
    def generateUpNext(self):
        upNext = []
        for num in range(3):
            upNext.append(Tetrominoe().getRandomTetromino())
        return upNext

    # removes first tetrominoe in the list and adds a new one
    def update(self):
        self.upNext.append(Tetrominoe().getRandomTetromino())
        return self.upNext.pop(0)



