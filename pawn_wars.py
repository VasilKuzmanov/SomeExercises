def check_if_pawn_becomes_a_queen(colour, row, col):
    if colour == "w" and row == 0 or colour == "b" and row == 7:
        pawn_colour = "White" if colour == "w" else "Black"
        quit(print(f"Game over! {pawn_colour} pawn is promoted to a queen at {chr(97 + col)}{8 - row}."))


def move_pawn(colour, row, col):
    def colour_is_white():
        if chess_board[row - 1][col - 1] == "b" or chess_board[row - 1][col + 1] == "b":
            quit(print(f"Game over! White win, capture on {chr(97 + chess_board[row - 1].index('b'))}{8 - row + 1}."))
        chess_board[row - 1][col], chess_board[row][col] = "w", "-"

    def colour_is_black():
        if chess_board[row + 1][col - 1] == "w" or chess_board[row + 1][col + 1] == "w":
            quit(print(f"Game over! Black win, capture on {chr(97 + chess_board[row + 1].index('w'))}{8 - row - 1}."))
        chess_board[row + 1][col], chess_board[row][col] = "b", "-"

    colour_is_white() if colour == "w" else colour_is_black()


def main(last_played="b"):
    for i in range(64):
        row, col = divmod(i, 8)
        if chess_board[row][col] in "wb" and chess_board[row][col] != last_played:
            pawn_colour = chess_board[row][col]
            check_if_pawn_becomes_a_queen(pawn_colour, row, col)
            move_pawn(pawn_colour, row, col)
            main(pawn_colour)


chess_board = [[x for x in input().split() + ["-"]] for _ in range(8)]
main()