import pentago_engine

if __name__ == '__main__':
    # Initialise the game engine
    # Modify these parameters to tweak the game
    app = pentago_engine.Pentago(
            x_player = None,
            o_player = None,
            )
    # start the game engine
    app.game_loop()
