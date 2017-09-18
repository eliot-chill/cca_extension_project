class Cell:

    row = 0
    col = 0

    board_index = 0

    token = "-"

    def __init__(self, row, col, board_index, token):

        self.row = row
        self.col = col
        self.board_index = board_index

    def insert_token(self,token):
        if self.token == "-":
            self.token = token
