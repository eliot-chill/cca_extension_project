import pygame, sys
import math
from pygame.locals import *

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
    window_width = (OFFSET_CANVAS*2) + \
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
    x_turn, winner, require_buttons):

    (display,gamefont) = game_display
    display.fill(YELLOW)

    pygame.draw.rect(display, BLACK, (OFFSET_CANVAS,
            OFFSET_CANVAS + TOP_OFFSET,
            BOARD_WIDTH * CELL_SIZE,
            BOARD_HEIGHT * CELL_SIZE
            ),
            2)



    for j in range(BOARD_HEIGHT):
        for i in range(BOARD_WIDTH):
            xc = OFFSET_CANVAS + CELL_SIZE / 2 + i * CELL_SIZE
            yc = OFFSET_CANVAS + TOP_OFFSET + CELL_SIZE / 2 + \
                (BOARD_HEIGHT - j - 1) * CELL_SIZE

            if board[i][j] == 1:
                pygame.draw.circle(display, RED, (int(xc), int(yc)),
                    int(CELL_SIZE * 2 / 5), 0)
            if board[i][j] == 2:
                pygame.draw.circle(display, BLUE, (int(xc), int(yc)),
                    int(CELL_SIZE * 2 / 5), 0)
            pygame.draw.circle(display, BLACK, (int(xc), int(yc)),
                int(CELL_SIZE * 2 / 5), 1)




    if selected_index >= (0,0) and game_running and player_turn:
        draw_display_token(display, selected_index[0], selected_index[1])


    if game_running:
        if require_buttons:
            thinking_surf = gamefont.render("Select a region...", False, BLACK)

        if x_turn and not require_buttons:
            thinking_surf = gamefont.render("X playing...", False, RED)

        elif not x_turn and not require_buttons:
            thinking_surf = gamefont.render("O playing...", False, BLUE)
        display.blit(thinking_surf, (OFFSET_CANVAS + 3 * CELL_SIZE,
         2 * OFFSET_CANVAS + TOP_OFFSET + BOARD_HEIGHT * CELL_SIZE))

    if not(game_running):
        draw_winners(display, gamefont, winner)

    pygame.display.update()


def draw_winners(display, gamefont, winner):
    if winner == 0:
        win_surf = gamefont.render("DRAW!", False, BLACK)
    elif winner == 1:
        win_surf = gamefont.render("X WINS!", False, RED)
    else:
        win_surf = gamefont.render("O WINS!", False, BLUE)
    display.blit(win_surf, (OFFSET_CANVAS, OFFSET_CANVAS / 2))

def hovered_col():
    (mouse_x, mouse_y) = pygame.mouse.get_pos()
    if (mouse_x >= OFFSET_CANVAS \
       and mouse_x < OFFSET_CANVAS + BOARD_WIDTH * CELL_SIZE \
       and mouse_y >= OFFSET_CANVAS + TOP_OFFSET \
       and mouse_y <= OFFSET_CANVAS + TOP_OFFSET + BOARD_HEIGHT * CELL_SIZE):
        # The player clicked on a column, not outside
        #print("Col",int((mouse_x - OFFSET_CANVAS) / CELL_SIZE))
        return int((mouse_x - OFFSET_CANVAS) / CELL_SIZE)
    else:
        # `-1` is the indicator that nothing has been selected
        return -1

def hovered_row():
    (mouse_x, mouse_y) = pygame.mouse.get_pos()
    if (mouse_x >= OFFSET_CANVAS \
       and mouse_x < OFFSET_CANVAS + BOARD_WIDTH * CELL_SIZE \
       and mouse_y >= OFFSET_CANVAS + TOP_OFFSET \
       and mouse_y <= OFFSET_CANVAS + TOP_OFFSET + BOARD_HEIGHT * CELL_SIZE):
        # The player clicked on a row, not outside
        #print("Row",(int((mouse_y - TOP_OFFSET-20) / CELL_SIZE)))
        return int(math.fabs(6-((mouse_y - TOP_OFFSET - 20) / CELL_SIZE)))
    else:
        # `-1` is the indicator that nothing has been selected
        return -1

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def button(display,msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > int(mouse[0]) > x and y+h > int(mouse[1]) > y:
        pygame.draw.rect(display, ac,(x,y,w,h))

        if click[0] == 1:
            sys.exit(0)
    else:
        pygame.draw.rect(display, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    display.blit(textSurf, textRect)

def draw_region_buttons(display):

    button(display, "1",(OFFSET_CANVAS),
    (OFFSET_CANVAS+TOP_OFFSET+CELL_SIZE*6.5),72,48,WHITE,RED)

    button(display, "2",(OFFSET_CANVAS+CELL_SIZE*1.5),
    (OFFSET_CANVAS+TOP_OFFSET+CELL_SIZE*6.5),72,48,WHITE,RED)

    button(display, "3",(OFFSET_CANVAS+CELL_SIZE*3),
    (OFFSET_CANVAS+TOP_OFFSET+CELL_SIZE*6.5),72,48,WHITE,RED)

    button(display, "4",(OFFSET_CANVAS+CELL_SIZE*4.5),
    (OFFSET_CANVAS+TOP_OFFSET+CELL_SIZE*6.5),72,48,WHITE,RED)


def select_region(region_number):
    print("Selected: ", region_number)

def hovered_direction():
    (mouse_x, mouse_y) = pygame.mouse.get_pos()

    if (mouse_x < BOARD_WIDTH / 2):
        return "left"
    elif (mouse_x > BOARD_WIDTH / 2):
        return "right"
