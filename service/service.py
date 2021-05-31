

class Service:
    def __init__(self, sudoku_board):
        self._sudokuBoard = sudoku_board
        self._sudokuBoard.place_numbers()

    def place_new_value(self, row_in_string, column_in_string, value_in_string):
        row = int(row_in_string)
        column = int(column_in_string)
        value = int(value_in_string)
        return self._sudokuBoard.player_input(row, column, value)

    def get_board(self):
        return self._sudokuBoard.get_board()

    def display_board(self):
        self._sudokuBoard.display_board()
