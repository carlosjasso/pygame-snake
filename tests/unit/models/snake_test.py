from modules.window import Window
from models.configuration import Configuration
from models.snake import Snake

def test_init():
    config = Configuration()
    Window(config) # Window needs to be initted for the snake model to work
    actual = Snake(config)
    assert actual
    assert actual.block
