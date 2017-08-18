class Cell:

    index = 0
    contents = "-"

    def set_index(self, index):
        self.index = index

    def insert_token(self, token):
        self.contents = token




class Region:

    def __init__(self):
        self.field = [Cell() for i in range(9)]
        self.index = 0
        self.set_index_of_cells()

    def set_index(self, index):
        self.index = index

    def set_index_of_cells(self):
        for i in range(len(self.field)):
            self.field[i].index = i

    def print_field(self):
        for i in range(len(self.field)):
            if (self.field[i].index == 5) or (self.field[i].index == 2) or (self.field[i].index == 8):
                print(self.field[i].index," ")

            else:
                print(self.field[i].index," ", end = '')


class Board:

    def __init__(self):
        self.field = [Region() for i in range(4)]
        self.set_index_of_regions()

    def set_index_of_regions(self):
        for i in range(len(self.field)):
            self.field[i].index = i


    def print_regions(self):
        for i in range(len(self.field)):
            self.field[i].print_field()

myBoard = Board()

myBoard.print_regions()
