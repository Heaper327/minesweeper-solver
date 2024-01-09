from game import Game

"""
Command line interface of the game, used for testing purposes
"""
def main():
    game = Game(20, 30, 60)
    printBoard(game)

    while not (game.hasWon() or game.hasLost()):
        inputStr = input("To open a tile, input 'o row col', to flag a tile, input 'f row col': ")
        
        tokens = inputStr.split(' ')
        if len(tokens) != 3:
            print("Malformed input, please try again")
            continue
        action = tokens[0]
        try:
            row = int(tokens[1]) - 1 # Convert from 1-indexed to 0-indexed
            col = int(tokens[2]) - 1
        except ValueError:
            print("Row or column index cannot be parsed, please try again.")
            continue

        if action == 'f':
            game.flag(row, col)
        elif action == 'o':
            game.open(row, col)
        else:
            print("Action cannot be recognized, make sure it is either r or o")

        printBoard(game)

    if game.hasWon():
        print("You won!")
    else:
        print("Game over, you lost!")

def printBoard(game: Game):
    board = game.getBoardPretty()
    # Tick every 5 tiles
    xRuler = "         " + "         ".join(['X' for i in range(int(game.numCols / 5))])
    yRuler = ['X' if i % 5 == 4 else ' ' for i in range(game.numRows)]

    rows = [yRuler[row] + "".join(board[row]) for row in range(game.numRows)]
    rows.insert(0, xRuler)

    print("\n".join(rows))
    

if __name__ == '__main__':
    main()