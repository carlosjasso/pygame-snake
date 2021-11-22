from models.configuration import Configuration
from modules.game import Game

if __name__ == "__main__": # entry point
    config = Configuration()
    game = Game(config)
    game.run()
