import pygame
import numpy

pygame.init()

# display_width = 1600
# display_height = 900
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     screen.fill((0, 0, 0))
#     pygame.draw.circle(screen, (0, 255, 0), (960, 540), 100)
#     pygame.display.flip()
#
# pygame.quit()


class GUI:
    def __init__(self, service):
        pygame.display.set_caption("Welcome to Sudoku!")
        monitor_info = pygame.display.Info()
        self._screen = pygame.display.set_mode((monitor_info.current_w, monitor_info.current_h))
        self._service = service

    def draw_board(self):
        board = self._service.get_board()
        board = numpy.matrix(board)
        print(board)
        # new_array = numpy.random.randint(3, size=(100, 100))
        surface = pygame.surfarray.make_surface(board)
        surface = pygame.transform.scale(surface, (500, 500))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self._screen.fill((0, 0, 0))
            self._screen.blit(surface, (100, 100))
            pygame.display.flip()
        pygame.quit()
