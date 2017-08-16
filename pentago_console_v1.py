import random
import sys
import os
import time


def clear_screen():
    os.system('cls')

def new_board():
    return [(["-"]*6) for i in range(6)]


def place_token(board, token, board_row, board_col):
    if board[board_row][board_col] == "-":
        board[board_row][board_col] = token
    else:
        return "invalid"

def print_board(board):
    for j in range(len(board)):
        if j == 3:
            print("= = = = = = = = = =")
        for i in range(len(board)):
            if i == 2:
                print(board[i][j]," ", end= '')
                print("|"," ", end='')
            else:
                print(board[i][j]," ", end= '')
        print("\n")

def define_region(board,region):
    region_1 = [board[0][0],board[0][1],board[0][2],
                board[1][0],board[1][1],board[1][2],
                board[2][0],board[2][1],board[2][2]]

    region_2 = [board[0][3],board[0][4],board[0][5],
                board[1][3],board[1][4],board[1][5],
                board[2][3],board[2][4],board[2][5]]

    region_3 = [board[3][0],board[3][1],board[3][2],
                board[4][0],board[4][1],board[4][2],
                board[5][0],board[5][1],board[5][2]]

    region_4 = [board[3][3],board[3][4],board[3][5],
                board[4][3],board[4][4],board[4][5],
                board[5][3],board[5][4],board[5][5]]



    regions = [region_1,region_2,region_3,region_4]

    return regions[int(region)-1]


def rotate_region(board, region, direction):

    current_region = define_region(board,region)

    for i in range(len(current_region)):
        print(current_region[i]+" is changing to "+current_region[new_position_after_rotation(i,direction)])
        current_region[i] = current_region[new_position_after_rotation(i,direction)]

    time.sleep(100)

    if region == 1:
        board[0][0] == current_region[0]
        board[0][1] == current_region[1]
        board[0][2] == current_region[2]

        board[1][0] == current_region[3]
        board[1][1] == current_region[4]
        board[1][2] == current_region[5]

        board[2][0] == current_region[6]
        board[2][1] == current_region[7]
        board[2][2] == current_region[8]

    if region == 2:
        board[0][3] == current_region[0]
        board[0][4] == current_region[1]
        board[0][5] == current_region[2]

        board[1][3] == current_region[3]
        board[1][4] == current_region[4]
        board[1][5] == current_region[5]

        board[2][3] == current_region[6]
        board[2][4] == current_region[7]
        board[2][5] == current_region[8]

    if region == 3:
        board[3][0] == current_region[0]
        board[3][1] == current_region[1]
        board[3][2] == current_region[2]

        board[4][0] == current_region[3]
        board[4][1] == current_region[4]
        board[4][2] == current_region[5]

        board[5][0] == current_region[6]
        board[5][1] == current_region[7]
        board[5][2] == current_region[8]

    if region == 4:
        board[3][3] == current_region[0]
        board[3][4] == current_region[1]
        board[3][5] == current_region[2]

        board[4][3] == current_region[3]
        board[4][4] == current_region[4]
        board[4][5] == current_region[5]

        board[5][3] == current_region[6]
        board[5][4] == current_region[7]
        board[5][5] == current_region[8]





def new_position_after_rotation(region_index,direction):
    right_rotation_map = [2,5,8,1,4,7,0,3,6]

    left_rotation_map = [6,3,0,7,4,1,8,5,2]

    if direction == "r":
        return right_rotation_map[region_index]
    else:
        return left_rotation_map[region_index]



def run():
    print("Welcome to Pentago! \n")

    board = new_board()
    first_player = decide_on_first_player()
    turn(board,first_player)

def decide_on_first_player():

    player_1_token = "X"
    player_2_token = "O"

    if random.randint(0,1) == 0:
        current_player = player_1_token
        print("Player 1 will go first!")
    else:
        current_player = player_2_token
        print("Player 2 will go first!")

    return current_player

def turn(board,current_player):
    print_board(board)

    print("Enter where to place your "+current_player+" token:")

    current_player_row = input("Row: ")
    current_player_col = input("Column: ")

    if place_token(board, current_player, int(current_player_row), int(current_player_col)) == "invalid":
        clear_screen()
        print("Invalid Move")
        turn(board,current_player)

    clear_screen()
    print_board(board)


    print("Select the grid to rotate")
    region_to_rotate = input("1-4: ")

    print("Select the direction")
    direction_to_rotate = input("l or r: ")


    rotate_region(board,region_to_rotate,direction_to_rotate)

    clear_screen()

    change_turn(board, current_player)


def change_turn(board, current_player):
    if current_player == "X":
        turn(board, "O")
    else:
        turn(board,"X")



run()
