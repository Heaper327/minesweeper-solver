from dataclasses import dataclass
import random

@dataclass
class Tile:
    # Whether this tile has been mined
    mined: bool
    # Whether this tile has been opened
    opened: bool
    # Whether this tile has been flagged
    flagged: bool
    # Number of adjacent mines, excluding this tile itself
    adjacentMines: int
    """
    Returns what the tile looks like 
    where a flagged unopened tile is 'X', an unflagged unopened tile is '?',
    a mined opened tile is '!', and an unmined opened tile is '0-9'
    """
    def toString(self) -> str:
        if self.opened:
            if self.mined:
                return '!'
            else:
                return str(self.adjacentMines)
        else:
            if self.flagged:
                return 'X'
            else:
                return '?'

# A minesweeper board
class Board:

    """
    Internal game board that keeps track of each tile's mined, opened, and flagged status
    """
    board: list[list[Tile]]
    """
    Number of rows and columns respectively.
    """
    numRows: int
    numCols: int
    """
    Status of the game, 0 represents in progress, 1 means won, and 2 means lost
    """
    status: int

    """
    Create an n-by-m game of minesweeper, with randomly placed mines using the given seed.
    n       -- The number of rows of the board
    m       -- The number of columns of the board
    numMines-- The number of mines on the board
    seed    -- Random seed used to place mines, same seed guarantees same placement of mines
    """
    def __init__(self, n: int, m: int, numMines: int, seed=None) -> None:
        self.board = [[Tile(False, False, False, 0) for col in range(m)] for row in range(n)]
        self.numRows = n
        self.numCols = m
        self.status = 0
        # populate board with mines randomly, and calculate each tile's number of adjacent mines
        random.seed(seed)
        indices = [i for i in range(n * m)]
        for index in random.sample(indices, numMines):
            row, col = int(index / m), index % m
            self.board[row][col].mined = True
            for i, j in self.__getNeighbors(row, col):
                    self.board[i][j].adjacentMines += 1

    """
    Return the current state of the board as an n-by-m array of characters, 
    where '?' represents an unopened tile, '0-8' represents an opened tile with no mine,
    '!' represents an opened tile with mine, and 'X' represents a flagged tile.
    """
    def toChars(self) -> list[list[str]]:
        return [[tile.toString() for tile in row] for row in self.board] 

    """
    Return a prettier version of the board as an n-by-m array of unicode characters
    """
    def toCharsPretty(self) -> list[list[str]]:
        pretty = {
            '!': '💥',
            'X': '🎌',
            '?': '🟦',
            '0': '⬜',
            '1': '1️⃣ ', # vscode treats keycap emojis as half-width characters, needs to pad with a space
            '2': '2️⃣ ',
            '3': '3️⃣ ',
            '4': '4️⃣ ',
            '5': '5️⃣ ',
            '6': '6️⃣ ',
            '7': '7️⃣ ',
            '8': '8️⃣ ',
        }
        chars = self.toChars()
        return [[pretty[char] for char in row] for row in chars]

    """
    Open the tile at row, col if it is unopened, and possibly open its adjacent non-mine tiles.
    Does nothing if row, col is out of bound or the tile is already opened
    row     -- The row of the tile to be opened
    col     -- The column of the tile to be opened
    """
    def open(self, row: int, col: int) -> None:
        if not self.__isValid(row, col):
            return
        
        tile = self.board[row][col]
        # do nothing if already opened, this prevents infinite loops
        if tile.opened:
            return
        tile.opened = True

        # if tile is mined, game over - open all tiles
        if tile.mined:
            self.status = 2
            for row in self.board:
                for tile in row:
                    tile.opened = True
            return
        
        # if its neighbors are all unmined, recursively reveal its neighbors
        if tile.adjacentMines == 0:
            for i, j in self.__getNeighbors(row, col):
                self.open(i, j)
    

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
    def hasWon(self) -> bool:
        return self.status == 1

    """
    Return whether the game has been lost, aka a mined tile has been opened. 
    """
    def hasLost(self) -> bool:
        return self.status == 2

    """
    Return a list of tiles adjacent to (row, col), including diagonal tiles
    """
    def __getNeighbors(self, row, col) -> list[int, int]:
        return [[i, j]
                for i in range(row - 1, row + 2) 
                for j in range(col - 1, col + 2)
                if self.__isValid(i, j) and (i, j) != (row, col)]

    """
    Return whether (row, col) is a valid coordinate (not out of bounds)
    """
    def __isValid(self, row, col) -> bool:
        return row >= 0 and row < self.numRows and col >= 0 and col < self.numCols
        