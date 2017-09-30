import pygame


FONTSIZE = 24
CELL_SIZE = 48
OFFSET_CANVAS = 20
TOP_OFFSET = 24
BOTTOM_SPACING = 64

pygame.font.init()
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
RED    = (255,   0,   0)
BLUE   = (  0,   0, 255)
YELLOW = (250, 240, 190)

def setup_display(board):
    window_width = 2 * OFFSET_CANVAS + 6 * CELL_SIZE
    window_height = 2 * OFFSET_CANVAS + TOP_OFFSET + BOTTOM_SPACING + 6 * CELL_SIZE
    display = pygame.display.set_mode((window_width, window_height), 0, 32)
    pygame.display.set_caption('Pentago!')
    gamefont = pygame.font.Font(None, FONTSIZE)
    return (display, gamefont)


def draw_counter(display, column, row):
    top_point = (OFFSET_CANVAS + CELL_SIZE * -row / 2 + CELL_SIZE * column,
                 OFFSET_CANVAS)
    bottom_point = (OFFSET_CANVAS + CELL_SIZE * -row / 2 + CELL_SIZE * column,
                    OFFSET_CANVAS + TOP_OFFSET * 3 / 4)
    left_point = (OFFSET_CANVAS + 3 * CELL_SIZE * -row / 8 + CELL_SIZE * column,
                  OFFSET_CANVAS + TOP_OFFSET / 2)
    right_point = (OFFSET_CANVAS + 5 * CELL_SIZE * -row / 8 + CELL_SIZE * column,
                   OFFSET_CANVAS + TOP_OFFSET / 2)
    pygame.draw.line(display, BLACK, left_point, bottom_point, 3)
    pygame.draw.line(display, BLACK, right_point, bottom_point, 3)
    pygame.draw.line(display, BLACK, top_point, bottom_point, 3)

def new_empty_board(height, width):
    return [([0] * height) for k in range(width)]

board = new_empty_board(6,6)

display = setup_display(board)[0]

draw_counter(display, 1,1)
