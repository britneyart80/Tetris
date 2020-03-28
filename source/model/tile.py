
# a game board tile
class Tile:

    # initializes a tile
    # @param column: the column position of this tile
    # @param row: the row position of this tile
    # @param isEmpty: whether the tile has been filled by a piece
    def __init__(self, column, row):
        self.column = column
        self.row = row
        self.isEmpty = False


