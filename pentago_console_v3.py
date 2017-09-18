import random
import sys

class Cell:

    def __init__(self, index, value):
        self.index = index
        self.value = value





class Board:

    field = []
    region_1 = []
    region_2 = []
    region_3 = []
    region_4 = []

    def __init__(self):
        self.create_board()

    def create_board(self):

        for i in range(6):
            self.field.append([])
            for j in range(6):
                self.field[i].append(Cell(((i*6)+j),"-"))

    def print_board(self):
        for i in range(len(self.field)):
            if i == 3:
                print("=============")
            for j in range(len(self.field)):
                if j == 3:
                    print("| ", end='')
                if j != 5:
                    print(self.field[i][j].value, end = ' ')
                else:
                    print(self.field[i][j].value)


    def insert_token(self, token, row, col):
        if self.field[int(row)][int(col)].value == "-":
            self.field[int(row)][int(col)].value = token




    def index_of_row_and_col(self,row,col):
        print(self.field[int(row)-1][int(col)-1].index+1)

    def checkWin(self, token):

        #check horizontal wins
        for i in range(len(self.field)):
            for j in range(len(self.field)-4):
                if((self.field[i][j].value == token) and (self.field[i][j+1].value == token) and (self.field[i][j+2].value == token) and
                   (self.field[i][j+3].value == token) and (self.field[i][j+4].value == token)):
                    return True

        #check vertical wins
        for i in range(len(self.field)-4):
            for j in range(len(self.field)):
                if((self.field[i][j].value == token) and (self.field[i+1][j].value == token) and (self.field[i+2][j].value == token) and
                   (self.field[i+3][j].value == token) and (self.field[i+4][j].value == token)):
                    return True


        #check \ diagonal wins
        for i in range(len(self.field)-4):
            for j in range(len(self.field)-4):
                if((self.field[i][j].value == token) and (self.field[i+1][j+1].value == token) and (self.field[i+2][j+2].value == token) and
                   (self.field[i+3][j+3].value == token) and (self.field[i+4][j+4].value == token)):
                    return True

        #check / diagonal wins
        for i in range(len(self.field)-4):
            for j in range(len(self.field)-4,len(self.field)):
                if((self.field[i][j].value == token) and (self.field[i+1][j-1].value == token) and (self.field[i+2][j-2].value == token) and
                   (self.field[i+3][j-3].value == token) and (self.field[i+4][j-4].value == token)):
                    return True



        return False


    def print_region(self,region):
        if region == 1:
            region = self.region_1
        if region == 2:
            region = self.region_2
        if region == 3:
            region = self.region_3
        if region == 4:
            region = self.region_4

        for i in range(len(region)):
            for j in range(len(region)):
                    print(self.field[i][j].value, end = ' ')






myBoard = Board()
myBoard.define_regions()
print(len(myBoard.region_1))
myBoard.print_region(1)
