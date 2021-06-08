import random


class SudokuBoard:
    def __init__(self, difficulty, board_size=9):
        self._board = [[' ' for i in range(board_size)] for j in range(board_size)]
        difficulty_dictionary = {"easy": 40, "hard": 23}
        self._gameDifficulty = difficulty_dictionary[difficulty]
        self._boardSize = board_size

    def is_on_row_or_column(self, row, column, value):
        for i in range(self._boardSize):
            if self._board[row][i] == value or self._board[i][column] == value:
                return True

        return False

    def is_square_empty(self, row, column):
        if self._board[row][column] == ' ':
            return True
        return False

    def place_numbers(self):
        placed_numbers = 0
        while placed_numbers < self._gameDifficulty:
            row = random.randint(0, self._boardSize-1)
            column = random.randint(0, self._boardSize-1)
            value = random.randint(1, self._boardSize)

            if not self.is_on_row_or_column(row, column, value) and self.is_square_empty(row, column):
                self._board[row][column] = value
                placed_numbers += 1

    def player_input(self, row, column, value):
        if self.is_on_row_or_column(row, column, value):
            return False
        self._board[row][column] = value
        return True

    def get_board(self):
        return self._board

    def display_board(self):
        print("------------------")
        for i in range(self._boardSize):
            print(*self._board[i])
            print("------------------")
        print("------------------")
