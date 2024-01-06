from board import Board

board = Board(20, 30, 100)
boardChars = board.toCharsPretty()
print("\n".join(["".join(row) for row in boardChars]))