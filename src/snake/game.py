from threading import Thread
from time import sleep
from models.snake import Snake
from models.configuration import Configuration
from models.display import Display
from models.enums.snake_direction import SnakeDirection
from models.enums.display_events import DisplayEvent

class Game:
    config : Configuration
    display : Display
    snake : Snake
    running : bool
    _next_direction : SnakeDirection

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

    def __init__(self, config : Configuration) -> None:
        self.config = config
        self.display = Display(config)
        self.snake = Snake(config)
        self.running = False
        self._next_direction = SnakeDirection.FORWARD

    def run(self):
        self.running = True
        self.display.draw_sprites(self.snake.blocks)
        sleep(0.2)
        Thread(target=self.snake_motion).start()
        self.listen_events()
    
    def listen_events(self):
        while self.running:
            for event in self.display.events:
                self._pipe_event(event)
    
    def _pipe_event(self, event : DisplayEvent):
        if event == DisplayEvent.EXIT: 
            self.running = False
        else: 
            self.next_direction = event
    
    def snake_motion(self):
        while self.running:
            self.snake.slither(self._next_direction)
            self._next_direction = SnakeDirection.FORWARD
            self.display.draw_sprites(self.snake.blocks)
            sleep(0.2)
