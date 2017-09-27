# class Game:
#     player_1 = None
#     player_2 = None



class Cell:

    row = 0
    col = 0

    #board_index = 0

    token = "-"

    def __init__(self, row, col):

        self.row = row
        self.col = col
        #self.board_index = board_index

    def insert_token(self,token):
        if self.token == "-":
            self.token = token




class Board:

    cells = []

    def create_board(self):

        for i in range(6):
            self.cells.append([])
            for j in range(6):
                self.cells[i].append(Cell(i,j))

    def print_board(self):
        for i in range(len(self.cells)):
            if i == 3:
                print("=============")
            for j in range(len(self.cells)):
                if j == 3:
                    print("| ", end='')
                if j != 5:
                    print(self.cells[i][j].token, end = ' ')
                else:
                    print(self.cells[i][j].token)


    def insert_token_to_cell(self, row, col, token):
        self.cells[row-1][col-1].insert_token(token)



    def assign_region(self, region_number):
        region = []

        for i in range(len(self.cells)):
            for j in range(len(self.cells)):

                if region_number == 1 and ((i == 0 or i == 1 or i == 2) and (j == 0 or j == 1 or j == 2)):
                    region.append(self.cells[i][j])
                if region_number == 2 and ((i == 0 or i == 1 or i == 2) and (j == 3 or j == 4 or j == 5)):
                    region.append(self.cells[i][j])
                if region_number == 3 and ((i == 3 or i == 4 or i == 5) and (j == 0 or j == 1 or j == 2)):
                    region.append(self.cells[i][j])
                if region_number == 4 and ((i == 3 or i == 4 or i == 5) and (j == 3 or j == 4 or j == 5)):
                    region.append(self.cells[i][j])

        return region


    def transpose_region(self,region):
        temp_region = list(map(list, zip(region)))
        return temp_region



    def switch_region_columns(self,region):
        temp_first_col = region[0]
        temp_last_col = region[len(region)-1]

        first_col = temp_last_col
        last_col = temp_first_col

        region[0] = first_col
        region[len(region)-1] = last_col

        return region

    def rotate_region_right(self, region_number):
        region_to_rotate = self.assign_region(region_number)

        region_to_rotate = self.switch_region_columns(region_to_rotate)
        region_to_rotate = self.transpose_region(region_to_rotate)

        self.reinsert_region_to_board(region_to_rotate)

    def rotate_region_left(self, region_number):
        region_to_rotate = self.assign_region(region_number)

        region_to_rotate = self.transpose_region(region_to_rotate)
        region_to_rotate = self.switch_region_columns(region_to_rotate)

        temp_array = []

        for i in range(len(region_to_rotate)):
            for j in range(len(region_to_rotate[0])):
                temp_array.append(region_to_rotate[i][j])

        print("- - - - - - - - - - - - - -")

        for i in range(len(temp_array)):
            print(temp_array[i].row,",",temp_array[i].col,":",temp_array[i].token)

    # def reinsert_region_to_board(self, region):
    #
    #     for i in range(len(region)):
    #         for j in range(len(region[0])):
    #
    #             for x in range(len(self.cells)):
    #                 for y in range(len(self.cells[0])):
    #                     if (region[i][j].row == self.cells[x][y].row) and (region[i][j].col == self.cells[x][y].col):
    #                         self.cells[x][y] == region[i][j]
    #                         print("Match!")


myBoard = Board()
myBoard.create_board()
myBoard.print_board()


row = int(input("Enter row"))
col = int(input("Enter col"))

myBoard.insert_token_to_cell(row,col,"X")
myBoard.print_board()

region_number = int(input("Rotate a region left: "))

region_to_print = myBoard.assign_region(region_number)

for cell in region_to_print:
    print(cell.row,",",cell.col,":",cell.token)

myBoard.rotate_region_left(region_number)
myBoard.print_board()
