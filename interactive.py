from board import Game

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
        row, col = int(tokens[0]), int(tokens[1])
        game.open(row, col)
        printBoard(game)

def printBoard(game):
    board = game.toCharsPretty()
    print("\n".join(["".join(row) for row in board]))
    print("")
    

if __name__ == '__main__':
    main()