#used to import all system and pygame libraries
import pygame
import sys
from pygame.locals import *

#import other libraries I've created to assist with project
import pentago_board
import pentago_graphics


#main game class
class Pentago:

    #method called once instance of the class is initialised
    def __init__(self,
         height = 6, width = 6, number_to_win = 5,
         x_player = None, o_player = None, ai_delay = 60):

         #intialise pygame and font setup
         pygame.init()
         pygame.font.init()

         #creating an empty board from the pentago_board library
         self.board = pentago_board.EmptyPentagoBoard(number_to_win)


         #initialising interface and other required settings
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

         self.require_buttons = False

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
        #This function acts as a wrapper for the function within
        #pentago_graphics
        pentago_graphics.draw_board(self.display, self.board.three_d_to_two_d(),
                self.selected_index, self.game_running, self.player_turn(),
                self.x_turn, self.winner, self.require_buttons)

    #defines the token required for the turn
    def turn_token(self):
        if self.x_turn:
            return pentago_board.X
        else:
            return pentago_board.O

    #attemping to insert a token into the specified row, column and region
    def attempt_insert(self, region,row,col):
        token = self.turn_token()
        success = self.board.attempt_insert(region, row, col, token)

        if success:
            self.win_check()

            self.x_turn = not(self.x_turn)



    #the main game loop
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

            #Processing mouse events
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




            #Draw buttons (attempting to)
            pentago_graphics.draw_region_buttons(self.display[0])

            #Update the display
            self.draw()
            pygame.time.wait(40)


        # If the game is over, wait for the quit event to close window
        while True:
            event = pygame.event.wait()
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            pygame.time.wait(60)


    #check to see if either a winner has been decided or if the board is full

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
