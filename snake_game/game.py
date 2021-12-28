from threading import Thread
from time import sleep
from random import randrange
from snake import Snake
from configuration import Configuration
from display import Display
from data.enum import SnakeDirection, DisplayEvent, SnakeEvent
from data.types import SpritePosition
from sprites import Apple, Score

class Game:
    #region Attributes & Properties
    config : Configuration
    _running : bool
    _next_direction : SnakeDirection
    display : Display
    snake : Snake
    apple : Apple
    score : Score
    _delay : float

    @property
    def next_direction(self) -> SnakeDirection:
        return self._next_direction

    @next_direction.setter
    def next_direction(self, event : DisplayEvent) -> SnakeDirection:
        match event:
            case DisplayEvent.MOVE_UP: self._next_direction = SnakeDirection.UP
            case DisplayEvent.MOVE_DOWN: self._next_direction = SnakeDirection.DOWN
            case DisplayEvent.MOVE_LEFT: self._next_direction = SnakeDirection.LEFT
            case DisplayEvent.MOVE_RIGHT: self._next_direction = SnakeDirection.RIGHT
    #endregion

    #region Init
    def __init__(self) -> None:
        self.config = Configuration()
        self._running = False
        self._next_direction = SnakeDirection.FORWARD
        self._delay = self.config.game.DELAY
        self._load_modules()

    def _load_modules(self):
        self.display = Display(
            window_size = self.config.window.WINDOW_SIZE
        )
        self.snake = Snake(
            window_size = self.config.window.WINDOW_SIZE,
            img_path = self.config.sprites.BLOCK_PATH
        )
        self.apple = Apple(
            window_size = self.config.window.WINDOW_SIZE,
            img_path = self.config.sprites.APPLE_PATH
        )
        self.score = Score(
            window_size = self.config.window.WINDOW_SIZE
        )
        self.apple.position = self.generate_new_apple_position()
    #endregion

    def run(self):
        self._running = True
        self._spawn_sprites()
        Thread(target=self._snake_motion).start()
        self._listen_events()

    def _listen_events(self):
        while self._running:
            for event in self.display.events:
                self._pipe_event(event)

    def _pipe_event(self, event : DisplayEvent):
        if event == DisplayEvent.EXIT:
            self._running = False
        else:
            self.next_direction = event

    def _snake_motion(self):
        while self._running:
            match self.snake.slither(self.apple.position, self._next_direction):
                case SnakeEvent.MOVED: self._snake_did_move()
                case SnakeEvent.CRASHED: self._running = False
                case SnakeEvent.HIT_APPLE: self._snake_hit_apple()

    def _snake_did_move(self):
        self._next_direction = SnakeDirection.FORWARD
        self._spawn_sprites()

    def _snake_hit_apple(self):
        self.apple.position = self.generate_new_apple_position()
        self.snake.grow_node()
        self._delay *= self.config.game.DELAY_MULTIPLIER
        self.score.increase()
        self._snake_did_move()

    def _spawn_sprites(self):
        self.display.draw_sprites([self.apple, *self.snake.blocks, self.score])
        sleep(self._delay)

    def generate_new_apple_position(self) -> SpritePosition:
        x = randrange(0, self.config.window.WINDOW_SIZE.WIDTH, self.apple.surface.get_width())
        y = randrange(0, self.config.window.WINDOW_SIZE.HEIGHT, self.apple.surface.get_height())
        if len([b for b in self.snake.blocks if b.position.X == x and b.position.Y == y]) > 0:
            return self.generate_new_apple_position()
        else: return SpritePosition(x, y)
