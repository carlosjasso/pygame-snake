from threading import Thread
from time import sleep
from snake import Snake
from configuration import Configuration
from display import Display
from data.enum import SnakeDirection, DisplayEvent, SnakeEvent
from sprites import Apple

class Game:
    config : Configuration
    _running : bool
    _next_direction : SnakeDirection
    display : Display
    snake : Snake
    apple : Apple

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

    def __init__(self) -> None:
        self.config = Configuration()
        self._running = False
        self._next_direction = SnakeDirection.FORWARD
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

    def run(self):
        self._running = True
        self.display.draw_sprites([*self.snake.blocks, self.apple])
        sleep(0.2)
        Thread(target=self.snake_motion).start()
        self.listen_events()
    
    def listen_events(self):
        while self._running:
            for event in self.display.events:
                self._pipe_event(event)
    
    def _pipe_event(self, event : DisplayEvent):
        if event == DisplayEvent.EXIT: 
            self._running = False
        else: 
            self.next_direction = event
    
    def snake_motion(self):
        while self._running:
            event = self.snake.slither(self._next_direction)
            match event:
                case SnakeEvent.MOVED:
                    self._next_direction = SnakeDirection.FORWARD
                    self.display.draw_sprites([*self.snake.blocks, self.apple])
                    sleep(0.2)
                case SnakeEvent.HIT_WALL:
                    self._running = False
