def print_board():
    [print(f"[ {', '.join(row)} ]") for row in board]


def place_on_the_board(col_idx: int, player_symbol: str, row_idx=-1):
    while board[row_idx][col_idx] != "0":
        row_idx -= 1
    board[row_idx][col_idx] = player_symbol

    return ROWS + row_idx


def check_for_win(row: int, col: int,):
    check_list = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    directions = ((1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1))
        # (bottom), (left), (right), (top-left), (bottom-right), (top-right), (bottom-left)

    for index, direction in enumerate(directions):
        checked_row = row + direction[0]
        checked_col = col + direction[1]

        while 0 <= checked_row < ROWS and 0 <= checked_col < COLS and \
                board[row][col] == board[checked_row][checked_col]:

            check_list[index] += 1
            checked_row += direction[0]
            checked_col += direction[1]

    if counter_for_draw == ROWS * COLS:
        print_board()
        quit(print('\033[92m' + "Draw!" + '\033[0m'))

    if check_list[0] == 3 or check_list[1] + check_list[2] >= 3 or \
        check_list[3] + check_list[4] >= 3 or check_list[5] + check_list[6] >= 3:
        print_board()
        quit(print('\033[92m' + f"Player {current_player} " + '\033[92m' +  "wins!" + '\033[0m'))


ROWS, COLS = 6, 7

counter_for_draw = 0

board = [["0"] * COLS for _ in range(ROWS)]

current_player, second_player = '\x1b[33m1\x1b[39m', '\x1b[31m2\x1b[39m'


while True:

    print_board()

    try:
        col_index = int(input(f"Player {current_player}, please chose a column: ")) - 1
        if not 0 <= col_index < COLS:
            raise ValueError
        row_index = place_on_the_board(col_index, current_player)
    except ValueError:
        print('\033[91m' + f"Select a valid number in the range (1-{COLS})" + '\033[0m')
        continue
    except IndexError:
        print('\033[91m' + "No empty spaces on that column, choose another one!" + '\033[0m')
        continue

    counter_for_draw += 1
    check_for_win(row_index, col_index)
    current_player, second_player = second_player, current_player
