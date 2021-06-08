from domain.SudokuBoard import SudokuBoard
from service.service import Service
from ui.ui import UI

board = SudokuBoard("easy")
service = Service(board)
ui = UI(service)
ui.run()
