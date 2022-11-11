"""
Problem Statement:

Implement tic-tac-toe game using two dimensional list.

"""

import numpy as np


def tic_tac_toe():
    board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    player_1 = input("Enter your name: ")
    player_2 = input("Enter your name: ")
    print(f"\n{player_1}, your symbol is '1'")
    print(f"{player_2}, your symbol is '2'\n")
    print(f"Let's start the game!!! {player_1} will go first")
    while True:
        print(f"\n{player_1}: ")
        try:
            r1 = int(input("Row Number: "))
            c1 = int(input("Column Number: "))
        except ValueError:
            print("Invalid Input. Try again!")
            r1 = int(input("Row Number: "))
            c1 = int(input("Column Number: "))
        if (r1 < 0 or r1 > 2) or (c1 < 0 or c1 > 2):
            print("Invalid Input")
        else:
            if board[r1][c1] == 0:
                board[r1][c1] = 1
                print(board)
            else:
                print("Position Occupied!")
        if (board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1 or
                board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1 or
                board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1 or
                board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1 or
                board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1 or
                board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1 or
                board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1 or
                board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1):
            print(f"\n{player_1} has won the game!!!")
            break
        print(f"\n{player_2}: ")
        try:
            r2 = int(input("Row Number: "))
            c2 = int(input("Column Number: "))
        except ValueError:
            print("Invalid Input. Try again!")
            r2 = int(input("Row Number: "))
            c2 = int(input("Column Number: "))
        if (r2 < 0 or r2 > 2) or (c2 < 0 or c2 > 2):
            print("Invalid Input")
        else:
            if board[r2][c2] == 0:
                board[r2][c2] = 2
                print(board)
            else:
                print("Position Occupied!")
        if (board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2 or
                board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2 or
                board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2 or
                board[0][0] == 2 and board[0][1] == 2 and board[0][2] == 2 or
                board[1][0] == 2 and board[1][1] == 2 and board[1][2] == 2 or
                board[2][0] == 2 and board[2][1] == 2 and board[2][2] == 2 or
                board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2 or
                board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2):
            print(f"\n{player_2} has won the game!!!")
            break
        if (board != 0).all():
            print("Game has drawn!!!")
            break


tic_tac_toe()
