# A game of minesweeper
class Game:
    """
    Create an n-by-m game of minesweeper, with randomly placed mines using the given seed.
    n       -- The number of rows of the board
    m       -- The number of columns of the board
    numMines-- The number of mines on the board
    seed    -- Random seed used to place mines, same seed guarantees same placement of mines
    """
    def __init__(self, n, m, numMines, seed) -> None:
        pass

    """
    Return the current state of the board as an n-by-m array of strings, 
    where '?' represents an unopened tile, '0-8' represents an opened tile with no mine,
    '!' represents an opened tile with mine, and 'X' represents a flagged tile.
    """
    def getBoard() -> list[list[str]]:
        pass

    """
    Open the tile at row, col if it is unopened, and possibly open its adjacent non-mine tiles.
    row     -- The row of the tile to be opened
    col     -- The column of the tile to be opened
    """
    def open(row, col) -> None:
        pass

    """
    Flag the tile at row, col if it has not been flagged already
    row     -- The row of the tile to be flagged
    col     -- The column of the tile to be flagged
    """
    def flag(row, col) -> None:
        pass

    """
    Returns whether the game has been won, aka all non-mine tiles have been opened.
    """
    def hasWon() -> bool:
        pass

    """
    Return whether the game has been lost, aka a mined tile has been opened. 
    """
    def hasLost() -> bool:
        pass