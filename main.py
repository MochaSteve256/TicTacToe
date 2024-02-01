def check_win():
    global xb
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if xb[i][0] == xb[i][1] == xb[i][2] != ' ':
            return True
        if xb[0][i] == xb[1][i] == xb[2][i] != ' ':
            return True
    if xb[0][0] == xb[1][1] == xb[2][2] != ' ':
        return True
    if xb[0][2] == xb[1][1] == xb[2][0] != ' ':
        return True
    return False


def do_computer_move():
    global xb
    import random
    # This function randomly selects an empty cell and places 'O' (computer's move)
    empty_cells = [(i, j) for i in range(3) for j in range(3) if xb[i][j] == ' ']
    if empty_cells:
        x, y = random.choice(empty_cells)
        xb[y][x] = 'O'
        print("Computer's move:")
        print_board()
        if check_win():
            print("Computer wins!")


# You need to define print_board() function which you haven't provided.
# Assuming it prints the current state of the board.
def print_board():
    global xb
    for row in xb:
        print(' | '.join(row))
        print('---------')
    print()


# You need to define xb as a global variable before calling new_game()
xb = [[' ']*3 for _ in range(3)]


def get_input():
    x = input("Enter a column: ")
    try:
        x = int(x)
    except ValueError:
        print("Invalid input")
        return get_input()
    x -= 1
    if x > 2 or x < 0:
        print("Invalid input")
        return get_input()
    y = input("Enter a row: ")
    try:
        y = int(y)
    except ValueError:
        print("Invalid input")
        return get_input()
    y -= 1
    if y > 2 or y < 0:
        print("Invalid input")
        return get_input()
    return (x, y)


def new_game():
    global xb
    player_char = "X"
    computer_char = "O"
    print_board()
    run = True
    while run:
        print("Player's turn")
        x, y = get_input()
        if xb[y][x] == " ":
            xb[y][x] = player_char
            print_board()
            if check_win():
                print("Player wins!")
                break
        else:
            print("Invalid move")
        do_computer_move()


# Start the game
new_game()
