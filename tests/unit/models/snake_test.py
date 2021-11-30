from src.snake.models.display import Display
from src.snake.models.configuration import Configuration
from src.snake.models.snake import Snake

def test_init():
    config = Configuration()
    display = Display(config)
    actual = Snake(config)
    assert len(actual.body) == 3
    assert actual.head