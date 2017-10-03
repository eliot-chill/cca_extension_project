#import engine module
import pentago_engine

#this will run when file is compiled and run
if __name__ == '__main__':
    #intialise main class from engine
    #define player settings
    app = pentago_engine.Pentago(
            x_player = None,
            o_player = None,
            )
    # start the main loop
    app.game_loop()
