board = [" " for item in range(9)]


def print_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")


def check_winner(player):
    for item in range(0, 9, 3):
        if board[item] == board[item + 1] == board[item + 2] == player:
            return True

    for item in range(3):
        if board[item] == board[item + 3] == board[item + 6] == player:
            return True

    if board[0] == board[4] == board[8] == player:
        return True

    if board[2] == board[4] == board[6] == player:
        return True

    return False


def play_game():
    current_player = "X"
    game_over = False

    while not game_over:
        print_board()
        position = int(input("Enter a position, from 1...9: ")) - 1

        if board[position] == " ":
            board[position] = current_player
            if check_winner(current_player):
                print_board()
                print("Player", current_player, "wins")
                game_over = True
            elif " " not in board:
                print_board()
                print("It's a tie!")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("That position is already taken. Try again.")


play_game()
