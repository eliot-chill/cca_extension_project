import copy


X = 1
O = 2


def empty_board():
    return [(["-"] * 6) for i in range(6)]


class PentagoBoard:

    def __init__(self, board = None, number_to_win = 5):
        if board == None:
            board = empty_board()

        self.pentago_board = board

        self.number_to_win = number_to_win


    def copy(self):
        return PentagoBoard(
            board = copy.deepcopy(self.pentago_board),
            number_to_win = self.number_to_win
        )


    def attempt_insert(self, row, col, token):
        if self.pentago_board[row][col] != "-":

            self.pentago_board[row][col] = token

            return True

        else:
            return False


    def board_full(self):

        for i in range(len(self.pentago_board)):
            for j in range(len(self.pentago_board[0])):
                if pentago_board[i][j] == "-":
                    return False


        return True


class EmptyPentagoBoard(PentagoBoard):
    def __init__(self, number_to_win = 5):
        fresh_board = empty_board()
        PentagoBoard.__init__(self, fresh_board, number_to_win)
