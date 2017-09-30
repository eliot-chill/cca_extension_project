import pygame

#Display contants
FONTSIZE = 24
CELL_SIZE = 48
OFFSET_CANVAS = 20
TOP_OFFSET = 24
BOTTOM_SPACING = 64
BOARD_WIDTH = 6
BOARD_HEIGHT = 6

# colour constants
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
RED    = (255,   0,   0)
BLUE   = (  0,   0, 255)
YELLOW = (250, 240, 190)



def setup_display():
    window_height = (OFFSET_CANVAS*2) + \
    (BOARD_WIDTH * CELL_SIZE)

    window_height = (OFFSET_CANVAS*2) + \
    TOP_OFFSET + BOTTOM_SPACING + \
    (BOARD_HEIGHT * CELL_SIZE)

    display = pygame.display.set_mode((window_width, window_height), 0, 32)

    pygame.display.set_caption("Pentago!")
    gamefont = pygame.font.Font(None, FONTSIZE)

    return (display, gamefont)

def draw_display_token(display, row, column):
    top_point = (OFFSET_CANVAS + CELL_SIZE / 2 + CELL_SIZE * column,
                 OFFSET_CANVAS * row)
    bottom_point = (OFFSET_CANVAS + CELL_SIZE / 2 + CELL_SIZE * column,
                    (OFFSET_CANVAS + TOP_OFFSET * 3 / 4) * row)
    left_point = (OFFSET_CANVAS + 3 * CELL_SIZE / 8 + CELL_SIZE * column,
                  (OFFSET_CANVAS + TOP_OFFSET / 2) * row)
    right_point = (OFFSET_CANVAS + 5 * CELL_SIZE / 8 + CELL_SIZE * column,
                   (OFFSET_CANVAS + TOP_OFFSET / 2) * row)

    pygame.draw.line(display, BLACK, left_point, bottom_point, 3)
    pygame.draw.line(display, BLACK, right_point, bottom_point, 3)
    pygame.draw.line(display, BLACK, top_point, bottom_point, 3)


def draw_board(game_display, board, selected_index, game_running, player_turn,
    x_turn, winner):

    (display,gamefont) = game_display
    display.fill(YELLOW)

    pygame.draw.rect(display, BLACK,
            (OFFSET_CANVAS,
            OFFSET_CANVAS + TOP_OFFSET,
            BOARD_WIDTH * CELL_SIZE,
            BOARD_HEIGHT * CELL_SIZE
            ),
            2)
