import copy
import list_rotations


X = 1
O = 2


def empty_board():
    output_list = []
    for i in range(4):
        output_list.append([])


        for x in range(3):
            output_list[i].append([])
            for y in range(3):
                output_list[i][x].append(0)

    return output_list


class PentagoBoard:

    def __init__(self, board = None, number_to_win = 5):
        if board == None:
            board = empty_board()

        self.field = board

        self.number_to_win = number_to_win


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


    def attempt_insert(self, region, row, col, token):
        # print(region,row,col)
        # print(self.field)

        if row >= 3:
            row -= 3
        if col >= 3:
            col -= 3

        if self.field[region][row][col] == 0:

            self.field[region][row][col] = token

            return True

        else:
            return False


    def board_full(self):
        checking_list = self.three_d_to_two_d()

        for i in range(len(checking_list)):
            for j in range(len(checking_list[0])):
                if checking_list[i][j] == 0:
                    return False


        return True

    def win_check(self):
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
                    return X
                if o_counter == self.number_to_win:
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
                    return X
                if o_counter == self.number_to_win:
                    return O

        #Positive diagonal for X and O
        for i in range(len(checking_list)):
            if checking_list[i][i] == X:
                print("X found at",i,i)
                x_counter += 1
            if checking_list[i][i] == O:
                o_counter += 1

            if checking_list[i][i] != X:
                x_counter = 0
            if checking_list[i][i] != O:
                o_counter = 0

            if x_counter == self.number_to_win:
                print("X pos")
                return X
            if o_counter == self.number_to_win:
                return O

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
                return X
            if o_counter == self.number_to_win:
                return O

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
                return X
            if o_counter == self.number_to_win:
                return O

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
                print("X neg")
                return X
            if o_counter == self.number_to_win:
                return O

        for i in range(len(checking_list)-2,-1,-1):
                if checking_list[i][len(checking_list)-2-i] == X:
                    x_counter += 1
                if checking_list[i][len(checking_list)-2-i] == O:
                    o_counter += 1

                if checking_list[i][len(checking_list)-2-i] != X:
                    x_counter = 0
                if checking_list[i][len(checking_list)-2-i] != O:
                    o_counter = 0

                if x_counter == self.number_to_win:
                    return X
                if o_counter == self.number_to_win:
                    return O

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
                    return X
                if o_counter == self.number_to_win:
                    return O


class EmptyPentagoBoard(PentagoBoard):
    def __init__(self, number_to_win = 5):
        fresh_board = empty_board()
        PentagoBoard.__init__(self, fresh_board, number_to_win)
