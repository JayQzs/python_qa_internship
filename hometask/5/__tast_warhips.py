# Write a warships game with field 5x5
import random
board = []

for x in range(0, 5):
    board.append(['0'] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))


def random_row(board):
    return random.randint(0, len(board))

def random_col(board):
    return random.randint(0, len(board))

ship_row = random_row(board)
ship_col = random_col(board)

print('Welcome to the game!')
print_board(board)

turns = 3
while turns > 0:
    guess_row = int(input('Guess the Row: '))
    guess_col = int(input('Guess the Column: '))

    if guess_row == ship_row and guess_col == ship_col:
        print('You won the game! You sank that warship!')
        break

    elif guess_row > 4 or guess_col > 4:
        turns -= 1
        print('That\'s not in the ocean')
        print('Turns left', str(turns))
    elif board[guess_row][guess_col] == 'X':
        turns -= 1
        print('You guessed that one already')
        print('Turns left', str(turns))
    elif turns == 0:
        print('The game is over')
    else:
        turns -= 1
        print('You missed the warship')
        print('Turns left', str(turns))
        board[guess_row][guess_col] = 'X'
        print_board(board)
