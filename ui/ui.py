class UI:
    def __init__(self, service):
        self._service = service

    def player_input_ui(self):
        row = input("Enter the row that you want to make your move on:")
        column = input("Enter the column that you want to make your move on:")
        value = input("Enter the value that you want to enter:")

        is_value_placed = self._service.place_new_value(row, column, value)

        if not is_value_placed:
            print("You cannot place number", value, "there!")
        else:
            self._service.display_board()

    def run(self):
        print("Welcome to sudoku!")
        self._service.display_board()
        while not self._service.is_game_over():
            self.player_input_ui()
        print("Congrats! You have completed the game!")
        self._service.display_board()
