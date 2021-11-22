from pygame.locals import KEYDOWN, QUIT, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT
from models.configuration import Configuration
from models.snake import Snake
from .window import Window

class Game:
    def __init__(self, config : Configuration) -> None:
        self._config = config

    def run(self) -> None:
        self.window = Window(self._config)
        self.snake = Snake(self._config)
        self.running = True
        self._listen()

    def _listen(self) -> None:
        while self.running:
            pass
    #         for event in pygame.event.get():
    #             if event.type == KEYDOWN:
    #                 if event.key == K_ESCAPE:
    #                     self._running = False
    #                 elif event.key == K_UP:
    #                     self._update_block_position(0, -10)
    #                 elif event.key == K_DOWN:
    #                     self._update_block_position(0, 10)
    #                 elif event.key == K_LEFT:
    #                     self._update_block_position(-10, 0)
    #                 elif event.key == K_RIGHT:
    #                     self._update_block_position(10, 0)
    #             elif event.type == QUIT:
    #                 self._running = False