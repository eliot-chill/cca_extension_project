import list_rotations as lr

class Cell:

    def __init__(self, token):
        self.token = token

    def getToken(self):
        return self.token

    def setToken(self, token):
        self.token = token




class Board:

    def __init__(self):

        self.cell_list = self.create_new_board()

    def create_new_board(self):
        output_list = []
        for i in range(4):
            output_list.append([])


            for x in range(3):
                output_list[i].append([])
                for y in range(3):
                    output_list[i][x].append(Cell("-"))

        return output_list

    def three_dim_to_two_dim(self):
        output_list = []

        region_1 = self.cell_list[0]
        region_2 = self.cell_list[1]
        region_3 = self.cell_list[2]
        region_4 = self.cell_list[3]

        for i in range(3):
            output_list.append(region_1[i])
            output_list.append(region_2[i])

        for j in range(3):
            output_list.append(region_3[j])
            output_list.append(region_4[j])

        return output_list

    def print_2d_list(self):
        output_list = self.three_dim_to_two_dim()


        for i in range(len(output_list)):

            if i % 2 == 0:
                print(" ")


            for j in range(len(output_list[0])):
                print(output_list[i][j].getToken(), end = '')
            if i % 2 == 0:
                print("|", end = '')






    def getCellValue(self, region, row, col):
        return self.cell_list[region][row][col].getToken()

    def setCellValue(self, region, row, col, token):
        self.cell_list[region][row][col].setToken(token)

    def rotate_region_clockwise(self, region_number):

        temp_region = self.cell_list[region_number]

        temp_region = lr.rotate_region_clockwise(temp_region)

        self.cell_list[region_number] = temp_region

    def rotate_region_anticlockwise(self, region_number):

        temp_region = self.cell_list[region_number]

        temp_region = lr.rotate_region_anticlockwise(temp_region)

        self.cell_list[region_number] = temp_region



myBoard = Board()
region = int(input("Enter region: "))-1
row = int(input("Enter col: "))-1
col = int(input("Enter row: "))-1

myBoard.setCellValue(region, row, col, "X")

myBoard.print_2d_list()

myBoard.rotate_region_clockwise(region)
print("\n")

myBoard.print_2d_list()

myBoard.rotate_region_anticlockwise(region)
myBoard.rotate_region_anticlockwise(region)
print("\n")
myBoard.print_2d_list()


# myList = [["0","1","2"],
#           ["3","4","5"],
#           ["6","7","8"]]
#
# output_list = lr.rotate_region_clockwise(myList)
#
# for i in range(len(output_list)):
#     print(output_list[i])
