from domain.SudokuBoard import SudokuBoard
from service.service import Service
from ui.ui import UI
from ui.gui import GUI

board = SudokuBoard("easy")
service = Service(board)
ui = UI(service)
gui = GUI(service)
gui.draw_board()
# ui.run()
