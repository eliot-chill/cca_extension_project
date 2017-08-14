import pygame
from pygame.locals import *
import sys
import random

def drawBoard(board):

    print('(0) ' + board[0] + '|' + board[1] + '|' + board[2] + ' | ' + board[3] + '|' + board[4] + '|' + board[5])
    print('    -+-+-' + ' | ' + '-+-+-')
    print('(6) ' + board[6] + '|' + board[7] + '|' + board[8] + ' | ' + board[9] + '|' + board[10] + '|' + board[11])
    print('    -+-+-' + ' | ' + '-+-+-')
    print('(12)' + board[12] + '|' + board[13] + '|' + board[14] + ' | ' + board[15] + '|' + board[16] + '|' + board[17])
    print('--------------')
    print('(18)' + board[18] + '|' + board[19] + '|' + board[20] + ' | ' + board[21] + '|' + board[22] + '|' + board[23])
    print('    -+-+-' + ' | ' + '-+-+-')
    print('(24)' + board[24] + '|' + board[25] + '|' + board[26] + ' | ' + board[27] + '|' + board[28] + '|' + board[29])
    print('    -+-+-' + ' | ' + '-+-+-')
    print('(30)' + board[30] + '|' + board[31] + '|' + board[32] + ' | ' + board[33] + '|' + board[34] + '|' + board[35])

def inputPlayerLetter():

    token = ''

    while not (token == 'X' or token == 'O' ):
        print('X or O?')
        token = input().upper()

    if token == 'X':
        return['X', 'O']
    else:
        return['O', 'X']

def whoGoesFirst():

    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def isWinner(board, token):

    return( #Horizontal
            (board[0] == token and board[1] == token and board[2] == token and board[3] == token and board[4] == token) or
            (board[5] == token and board[1] == token and board[2] == token and board[3] == token and board[4] == token) or
            (board[6] == token and board[7] == token and board[8] == token and board[9] == token and board[10] == token) or
            (board[11] == token and board[7] == token and board[8] == token and board[9] == token and board[10] == token) or
            (board[12] == token and board[13] == token and board[14] == token and board[15] == token and board[16] == token) or
            (board[17] == token and board[13] == token and board[14] == token and board[15] == token and board[16] == token) or
            (board[18] == token and board[19] == token and board[20] == token and board[21] == token and board[22] == token) or
            (board[23] == token and board[19] == token and board[20] == token and board[21] == token and board[22] == token) or
            (board[24] == token and board[25] == token and board[26] == token and board[27] == token and board[28] == token) or
            (board[29] == token and board[25] == token and board[26] == token and board[27] == token and board[28] == token) or
            (board[30] == token and board[31] == token and board[32] == token and board[33] == token and board[34] == token) or
            (board[35] == token and board[31] == token and board[32] == token and board[33] == token and board[34] == token) or
            #Vertical
            (board[0] == token and board[6] == token and board[12] == token and board[18] == token and board[24] == token) or
            (board[30] == token and board[6] == token and board[12] == token and board[18] == token and board[24] == token) or
            (board[1] == token and board[7] == token and board[13] == token and board[19] == token and board[25] == token) or
            (board[31] == token and board[7] == token and board[13] == token and board[19] == token and board[25] == token) or
            (board[2] == token and board[8] == token and board[14] == token and board[20] == token and board[26] == token) or
            (board[32] == token and board[8] == token and board[14] == token and board[20] == token and board[26] == token) or
            (board[3] == token and board[9] == token and board[15] == token and board[21] == token and board[27] == token) or
            (board[33] == token and board[9] == token and board[15] == token and board[21] == token and board[27] == token) or
            (board[4] == token and board[10] == token and board[16] == token and board[22] == token and board[28] == token) or
            (board[34] == token and board[10] == token and board[16] == token and board[22] == token and board[28] == token) or
            (board[5] == token and board[11] == token and board[17] == token and board[23] == token and board[29] == token) or
            (board[35] == token and board[11] == token and board[17] == token and board[23] == token and board[29] == token) or
            #Diagonal
            (board[24] == token and board[19] == token and board[14] == token and board[9] == token and board[4] == token) or
            (board[31] == token and board[26] == token and board[21] == token and board[16] == token and board[11] == token) or
            (board[30] == token and board[25] == token and board[20] == token and board[15] == token and board[10] == token) or
            (board[5] == token and board[25] == token and board[20] == token and board[15] == token and board[10] == token) or
            (board[34] == token and board[27] == token and board[20] == token and board[13] == token and board[6] == token) or
            (board[29] == token and board[22] == token and board[15] == token and board[8] == token and board[1] == token) or
            (board[35] == token and board[28] == token and board[21] == token and board[14] == token and board[7] == token) or
            (board[0] == token and board[28] == token and board[21] == token and board[14] == token and board[7] == token)
    )

def makeMove (board, token, move):
    board[move] = token

def rotateGrid(board, grid, way):

    if grid == 1:
        if way == 'L':
            hold1 = board[0]
            hold2 = board[1]
            board[0] = board[2]
            board[1] = board[8]
            board[2] = board[14]
            board[8] = board[13]
            board[14] = board[12]
            board[13] = board[6]
            board[12] = hold1
            board[6] = hold2
        if way == 'R':
            hold1 = board[0]
            hold2 = board[6]
            board[0] = board[12]
            board[6] = board[13]
            board[12] = board[14]
            board[13] = board[8]
            board[14] = board[2]
            board[8] = board[1]
            board[2] = hold1
            board[1] = hold2

    if grid == 2:
        if way == 'L':
            hold1 = board[3]
            hold2 = board[4]
            board[3] = board[5]
            board[4] = board[11]
            board[5] = board[17]
            board[11] = board[16]
            board[17] = board[15]
            board[16] = board[9]
            board[15] = hold1
            board[9] = hold2
        if way == 'R':
            hold1 = board[3]
            hold2 = board[9]
            board[3] = board[15]
            board[9] = board[16]
            board[15] = board[17]
            board[16] = board[11]
            board[17] = board[5]
            board[11] = board[4]
            board[5] = hold1
            board[4] = hold2

    if grid == 3:
        if way == 'L':
            hold1 = board[18]
            hold2 = board[19]
            board[18] = board[20]
            board[19] = board[26]
            board[20] = board[32]
            board[26] = board[31]
            board[32] = board[30]
            board[31] = board[24]
            board[30] = hold1
            board[24] = hold2
        if way == 'R':
            hold1 = board[18]
            hold2 = board[24]
            board[18] = board[30]
            board[24] = board[31]
            board[30] = board[32]
            board[31] = board[26]
            board[32] = board[20]
            board[26] = board[19]
            board[20] = hold1
            board[19] = hold2

    if grid == 4:
        if way == 'L':
            hold1 = board[21]
            hold2 = board[22]
            board[21] = board[23]
            board[22] = board[29]
            board[23] = board[35]
            board[29] = board[34]
            board[35] = board[33]
            board[34] = board[27]
            board[33] = hold1
            board[27] = hold2
        if way == 'R':
            hold1 = board[21]
            hold2 = board[27]
            board[21] = board[33]
            board[27] = board[34]
            board[33] = board[35]
            board[34] = board[29]
            board[35] = board[23]
            board[29] = board[22]
            board[23] = hold1
            board[22] = hold2

def copyBoard(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isFree(board, move):
    return board[move] == ' '

def playerMove(board):
    move = ' '
    spaceList ='0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22 \
    23,24,25,26,27,28,29,30,31,32,33,34,35'
    while move not in spaceList.split(',') or not isFree(board, int(move)):
        print('What is your move? (0-35)')
        move = input()

    return int(move)

def playerChoose():
    grid = ' '
    gridList = '1,2,3,4'
    while grid not in gridList.split(','):
        print('Which grid would you like to rotate? (1-4)')
        grid = input()

    return int(grid)

def playerRotate():
    direction = ' '
    directionList = 'L,R'
    while direction not in directionList.split(','):
        print('Rotate in which direction? (L/R)')
        direction = input().upper()

    return direction


def chooseRandom(board):

    possibleMoves = []
    for i in range(35):
        if isFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) !=0:
        return random.choice(possibleMoves)
    else:
        return None

def computerMove(board, computerLetter):

        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        for i in range (35):
            boardCopy = copyBoard(board)
            if isFree(boardCopy, i):
                makeMove(boardCopy, playerLetter,i)

        return chooseRandom(board)

def computerChoose():

    grid = random.randint(0,3)
    print ('Grid No. ' + str(grid))
    return grid

def computerRotate():

    if random.randint(0,1) == 0:
        print('Rotated Left')
        return 'L'
    else:
        print('Rotated Right')
        return 'R'

def isFull(board):
    for i in range (35):
        if isFree(board, i):
            return False
    return True

def run():

    print('Welcome to Pentago')

    while True:
        theBoard = [' ']*36
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print('The ' + turn + ' is going first!')
        gameisPlaying = True

        while gameisPlaying:
            if turn == 'player':
                drawBoard(theBoard)
                move = playerMove(theBoard)
                makeMove(theBoard, playerLetter, move)
                drawBoard(theBoard)
                number = playerChoose()
                direction = playerRotate()
                rotateGrid(theBoard, number, direction)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('You Win!')
                    gameisPlaying = False
                else:
                    if isFull(theBoard):
                        drawBoard(theBoard)
                        print("It's a Draw!")
                        break
                    else:
                        turn = 'computer'

            else:
                move = computerMove(theBoard,computerLetter)
                makeMove(theBoard, computerLetter, move)
                number = computerChoose()
                direction = computerRotate()
                rotateGrid(theBoard, number, direction)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The Computer Wins!')
                    gameisPlaying = False
                if isFull(theBoard):
                    drawBoard(theBoard)
                    print("It's a Draw!")
                    break

                turn = 'player'

        print('Play Again? (Y/N)')
        if not input() == 'Y':
            break

run()
