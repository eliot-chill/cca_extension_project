import pygame
import sys
from pygame.locals import *


import pentago_board
import pentago_graphics



class Pentago:


    def __init__(self,
         height = 6, width = 6, number_to_win = 5,
         x_player = None, o_player = None, ai_delay = 60):


         pygame.init()
         pygame.font.init()

         self.board = pentago_board.EmptyPentagoBoard(number_to_win)



         self.selected_row = -1
         self.selected_col = -1
         self.selected_region = -1
         self.selected_direction = ""

         self.selected_index = (self.selected_row,self.selected_col)

         self.display = pentago_graphics.setup_display()


         self.x_player = x_player
         self.o_player = o_player
         self.ai_delay = ai_delay

         self.winner = -1
         self.game_running = True
         self.x_turn = True

         ## draw initial board
         self.draw()


    def player_turn(self):
        if self.x_turn and self.x_player is None:
            # It's x's turn and x's human
            return True
        elif (not self.x_turn) and self.o_player is None:
            # It's x's turn and x's human
            return True
        else:
            return False


    def draw(self):
        # A wrapper around the `ConnectFourGraphics.draw_board` function that
        # picks all the right components of `self`.
        pentago_graphics.draw_board(self.display, self.board.three_d_to_two_d(),
                self.selected_index, self.game_running, self.player_turn(),
                self.x_turn, self.winner)


    def turn_token(self):
        if self.x_turn:
            return pentago_board.X
        else:
            return pentago_board.O


    def attempt_insert(self, region,row,col):
        token = self.turn_token()
        success = self.board.attempt_insert(region, row, col, token)

        if success:
            self.win_check()

            self.x_turn = not(self.x_turn)




    def game_loop(self):
        while self.game_running:

            if not self.player_turn():
                start_ai_time = pygame.time.get_ticks()

                token = self.turn_token()
                if token == pentago_board.X:
                    move = self.x_player(self.board,token)
                elif token == pentago_board.O:
                    move = self.o_player(self.board, token)
                self.attempt_insert(move)
                stop_ai_time = pygame.time.get_ticks()
                ai_time_span = stop_ai_time - start_ai_time
                if ai_time_span < self.ai_delay:
                    pygame.time.delay(self.ai_delay - ai_time_span)


            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == MOUSEMOTION:
                    self.selected_index = \
                        (pentago_graphics.hovered_col(),
                         pentago_graphics.hovered_row())
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.player_turn():
                        self.attempt_insert(
                        self.board.find_region_from_2d_coord(self.selected_index[0],
                        self.selected_index[1]),
                        self.selected_index[0],
                        self.selected_index[1])

            # Refresh the display
            pentago_graphics.draw_region_buttons(self.display[0])
            self.draw()
            pygame.time.wait(40)

            # for event in pygame.event.get():
            #     if event.type == QUIT:
            #         pygame.quit()
            #         sys.exit(0)
            #     if event.type == MOUSEBUTTONDOWN and event.button == 1:
            #         if self.player_turn():
            #             self.selected_region = pentago_graphics.hovered_region()
            #     if event.type == MOUSEBUTTONDOWN and event.button == 1:
            #         if self.player_turn():
            #             self.selected_direction = \
            #             pentago_graphics.hovered_direction()
            #
            # if self.selected_direction == "right":
            #     self.board.rotate_region_clockwise(self.selected_region)
            #
            # elif self.selected_direction == "left":
            #     self.board.rotate_region_anticlockwise(self.selected_region)
            #
            # self.selected_region = -1
            # self.selected_direction = ""
            #
            # #Refresh the display and loop back
            # self.draw()
            # pygame.time.wait(40)

        # Once the game is finish, simply wait for the `QUIT` event
        while True:
            event = pygame.event.wait()
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            pygame.time.wait(60)




        # is the game finished?
        # return True if that is the case otherwise return False
    def win_check(self):
        if self.board.win_check() == 1:
            self.winner = pentago_board.X
            self.game_running = False
        if self.board.win_check() == 2:
            self.winner = pentago_board.O
            self.game_running = False
        if self.board.board_full():
            print("Board is full")
            self.winner = 0
            self.game_running = False
