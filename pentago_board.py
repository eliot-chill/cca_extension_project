#importing necessary modules, including the list_rotations module
import copy
import list_rotations as lr #importing it as lr because "list_rotations" is long

#setting up player tokens
X = 1
O = 2

#defining an empty board, 4 regions of 3x3 grids. A 3D array (list.
def empty_board():
    output_list = []
    for i in range(4):
        output_list.append([])


        for x in range(3):
            output_list[i].append([])
            for y in range(3):
                output_list[i][x].append(0)

    return output_list

#main pentago board class
class PentagoBoard:

    def __init__(self, board = None, number_to_win = 5):
        if board == None:
            board = empty_board()

        self.field = board
        #the number "in a row" required to win
        self.number_to_win = number_to_win

    #converts the 3d coordinate (eg, region, row and column) into a
    #2d coordinate that is just a row and column. This is in reference to the
    #whole board as apposed to the relative region.
    def three_d_to_two_d(self):
        output_list = []

        region_1 = self.field[0]
        region_2 = self.field[1]
        region_3 = self.field[2]
        region_4 = self.field[3]

        for i in range(3):
            output_list.append(region_1[i]+region_2[i])

        for j in range(3):
            output_list.append(region_3[j]+ region_4[j])

        return output_list

    #rotates region clockwise, the region in question is specified by the
    #parameter
    #a wrapper for the lr function
    def rotate_region_clockwise(self, region_number):
        temp_region = self.field[region_number]
        temp_region = lr.rotate_region_clockwise(temp_region)

        self.field[region_number] = temp_region

    def rotate_region_anticlockwise(self, region_number):
        temp_region = self.field[region_number]
        temp_region = lr.rotate_region_anticlockwise(temp_region)

        self.field[region_number] = temp_region

    def copy(self):
        return PentagoBoard(
            board = copy.deepcopy(self.field),
            number_to_win = self.number_to_win
        )

    #uses the row and column coordinate to determine the region
    def find_region_from_2d_coord(self, row, col):
        region = 0
        if (row <= 2 and col <= 2):
            region = 0
        elif (row <= 2 and col >= 3):
            region = 1
        elif (row >= 3 and col <= 2):
            region = 2
        elif (row >= 3 and col >= 3):
            region = 3

        return region

    #attempts to insert the specified token into the region, row and column
    def attempt_insert(self, region, row, col, token):

        if row >= 3:
            row -= 3
        if col >= 3:
            col -= 3

        if self.field[region][row][col] == 0:

            self.field[region][row][col] = token

            return True

        else:
            return False

    #checks to see if the board is full
    def board_full(self):
        checking_list = self.three_d_to_two_d()

        for i in range(len(checking_list)):
            for j in range(len(checking_list[0])):
                if checking_list[i][j] == 0:
                    return False


        return True
    #This checks the various diections for potential "5-in-a-rows"
    def win_check(self):
        """Apologies for the long function. I did intend on seperating this up
        into smaller functions, however that never happened..."""

        checking_list = self.three_d_to_two_d()

        x_counter = 0
        o_counter = 0

        #Horizontal check for X and O
        for i in range(len(checking_list)):
            for j in range(len(checking_list[0])):
                if checking_list[i][j] == X:
                    x_counter += 1
                if checking_list[i][j] == O:
                    o_counter += 1

                if checking_list[i][j] != X:
                    x_counter = 0
                if checking_list[i][j] != O:
                    o_counter = 0

                if x_counter == self.number_to_win:
                    print("X hor")
                    return X
                if o_counter == self.number_to_win:
                    print("O hor")
                    return O

        #Vertical check for X and O
        for i in range(len(checking_list)):
            for j in range(len(checking_list[0])):
                if checking_list[j][i] == X:
                    x_counter += 1
                if checking_list[j][i] == O:
                    o_counter += 1

                if checking_list[j][i] != X:
                    x_counter = 0
                if checking_list[j][i] != O:
                    o_counter = 0

                if x_counter == self.number_to_win:
                    print("X ver")
                    return X
                if o_counter == self.number_to_win:
                    print("O ver")
                    return O

        x_counter = 0
        o_counter = 0
        #Positive diagonal for X and O
        for i in range(len(checking_list)):
            if checking_list[i][i] == X:
                x_counter += 1
            if checking_list[i][i] == O:
                o_counter += 1

            if checking_list[i][i] != X:
                x_counter = 0
            if checking_list[i][i] != O:
                o_counter = 0

            if x_counter == self.number_to_win:
                print("X pos 1")
                return X
            if o_counter == self.number_to_win:
                print("O pos 1")
                return O

        x_counter = 0
        o_counter = 0
        for i in range(len(checking_list)-1):
            if checking_list[i][i+1] == X:
                x_counter += 1
            if checking_list[i][i+1] == O:
                o_counter += 1

            if checking_list[i][i+1] != X:
                x_counter = 0
            if checking_list[i][i+1] != O:
                o_counter = 0

            if x_counter == self.number_to_win:
                print("X pos 2")
                return X
            if o_counter == self.number_to_win:
                print("O pos 2")
                return O

        x_counter = 0
        o_counter = 0
        for i in range(1,len(checking_list)):
            if checking_list[i][i-1] == X:
                x_counter += 1
            if checking_list[i][i-1] == O:
                o_counter += 1

            if checking_list[i][i-1] != X:
                x_counter = 0
            if checking_list[i][i-1] != O:
                o_counter = 0

            if x_counter == self.number_to_win:
                print("X pos 3")
                return X
            if o_counter == self.number_to_win:
                print("O pos 3")
                return O

        x_counter = 0
        o_counter = 0
        #Negative diagonal for X and O
        for i in range(len(checking_list)-1,-1,-1):
            if checking_list[i][len(checking_list)-1-i] == X:
                x_counter += 1
            if checking_list[i][len(checking_list)-1-i] == O:
                o_counter += 1

            if checking_list[i][len(checking_list)-1-i] != X:
                x_counter = 0
            if checking_list[i][len(checking_list)-1-i] != O:
                o_counter = 0

            if x_counter == self.number_to_win:
                print("X neg 1")
                return X
            if o_counter == self.number_to_win:
                print("O neg 1")
                return O

        x_counter = 0
        o_counter = 0
        for i in range(len(checking_list)-2,-1,-1):
                print("Checking:",i,(4-i))
                if checking_list[i][len(checking_list)-2-i] == X:
                    print("X found at: ",i,(4-i))
                    x_counter += 1
                if checking_list[i][len(checking_list)-2-i] == O:
                    print("O found at: ",i,(4-i))
                    o_counter += 1

                if checking_list[i][len(checking_list)-2-i] != X:
                    x_counter = 0
                if checking_list[i][len(checking_list)-2-i] != O:
                    o_counter = 0

                if x_counter == self.number_to_win:
                    print("X neg 2")
                    return X
                if o_counter == self.number_to_win:
                    print("O neg 2")
                    return O

        x_counter = 0
        o_counter = 0
        for i in range(len(checking_list)-1,0,-1):
                if checking_list[i][len(checking_list)-i] == X:
                    x_counter += 1
                if checking_list[i][len(checking_list)-i] == O:
                    o_counter += 1

                if checking_list[i][len(checking_list)-i] != X:
                    x_counter = 0
                if checking_list[i][len(checking_list)-i] != O:
                    o_counter = 0

                if x_counter == self.number_to_win:
                    print("X neg 3")
                    return X
                if o_counter == self.number_to_win:
                    print("O neg 3")
                    return O

#Defines an empty board - inherits from the main class
class EmptyPentagoBoard(PentagoBoard):
    def __init__(self, number_to_win = 5):
        fresh_board = empty_board()
        PentagoBoard.__init__(self, fresh_board, number_to_win)
