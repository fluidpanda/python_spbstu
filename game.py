import os
from typing import Any
from subprocess import call

BOARD: list = [" " for item in range(0, 9)]


def print_board():
    print("-" * 13)
    print("|", BOARD[0], "|", BOARD[1], "|", BOARD[2], "|")
    print("-" * 13)
    print("|", BOARD[3], "|", BOARD[4], "|", BOARD[5], "|")
    print("-" * 13)
    print("|", BOARD[6], "|", BOARD[7], "|", BOARD[8], "|")
    print("-" * 13)


def clear_screen() -> None:
    _ = call("clear" if os.name == "posix" else "cls")


def win_logic(player: Any) -> bool:
    for item in range(0, 9, 3):
        if BOARD[item] == BOARD[item + 1] == BOARD[item + 2] == player:
            return True

    for item in range(3):
        if BOARD[item] == BOARD[item + 3] == BOARD[item + 6] == player:
            return True

    if BOARD[0] == BOARD[4] == BOARD[8] == player:
        return True

    if BOARD[2] == BOARD[4] == BOARD[6] == player:
        return True

    return False


def main() -> None:
    current_player: str = "X"
    game_over_state: bool = False

    while not game_over_state:
        print_board()

        try:
            position: int = int(input(f"Игрок {current_player}, введите позицию, цифру от 1 до 9: ")) - 1

            if BOARD[position] == " ":
                BOARD[position] = current_player

                if win_logic(current_player):
                    print_board()
                    print(f"Игрок {current_player} выиграл")
                    game_over_state = True

                elif " " not in BOARD:
                    print_board()
                    print("Ничья")
                    game_over_state = True

                else:
                    current_player = "O" if current_player == "X" else "X"

            else:
                print("Позиция занята. Введите позицию еще раз.")

        except (ValueError, IndexError):
            print("Вы ввели не цифру от 1 до 9!")

        finally:
            clear_screen()


if __name__ == "__main__":
    main()
