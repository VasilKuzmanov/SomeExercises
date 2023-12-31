def check_if_pawn_becomes_a_queen(pawn, row, col, colour):
    if pawn == "w" and row == 0 or pawn == "b" and row == 7:
        quit(print(f"Game over! {colour} pawn is promoted to a queen at {chr(97 + col)}{8 - row}."))


def move_pawn(pawn, row, col, colour):
    one_row_forward = row - 1 if pawn == "w" else row + 1
    plus_one_minus_one = 1
    chess_board[row][col] = "-"

    for _ in range(2):
        if chess_board[one_row_forward][col + plus_one_minus_one] != "-":
            quit(print(f"Game over! {colour} win, capture on {chr(97 + col + plus_one_minus_one)}{8 - one_row_forward}."))

        plus_one_minus_one *= -1

    chess_board[one_row_forward][col] = pawn


def main(last_played="b"):
    for i in range(64):
        row, col = divmod(i, 8)

        if chess_board[row][col] in "wb" and chess_board[row][col] != last_played:
            pawn = chess_board[row][col]
            colour = "White" if pawn == "w" else "Black"
            check_if_pawn_becomes_a_queen(pawn, row, col, colour)
            move_pawn(pawn, row, col, colour)
            main(pawn)


chess_board = [[x for x in input().split() + ["-"]] for _ in range(8)]
main()
