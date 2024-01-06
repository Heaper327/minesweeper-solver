from board import Board

def printBoard(board):
    boardChars = board.toCharsPretty()
    print("\n".join(["".join(row) for row in boardChars]))
    print("")

def main():
    board = Board(20, 30, 60)
    printBoard(board)

    while not (board.hasWon() or board.hasLost()):
        inputStr = input("To open a tile, input 'row col': ")
        tokens = inputStr.split(' ')
        if len(tokens) != 2:
            print("Input cannot be parsed, please try again.")
            continue
        row, col = int(tokens[0]), int(tokens[1])
        board.open(row, col)
        printBoard(board)
    

if __name__ == '__main__':
    main()