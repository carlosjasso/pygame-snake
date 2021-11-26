from time import sleep
from pygame.locals import KEYDOWN, QUIT, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT
from models.snake import Snake
from models.configuration import Configuration
from models.display import Display
from models.snake_direction import SnakeDirection

class Game:
    config : Configuration
    display : Display
    snake : Snake
    running : bool

    def __init__(self, config : Configuration) -> None:
        self.config = config
        self.display = Display(config)
        self.snake = Snake(config)
        self.running = False

    def run(self):
        self.running = True
        
        sprites = [sprite for name, sprite in self.snake.body]
        self.display.draw_sprites(sprites)
        sleep(100)

        # Event loop
        block_direction = SnakeDirection.RIGHT
        while self.running:
            for event in self.display.event:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                        continue
                    
                    if event.key == K_UP:
                        block_direction = SnakeDirection.UP
                    elif event.key == K_DOWN:
                        block_direction = SnakeDirection.DOWN
                    elif event.key == K_LEFT:
                        block_direction = SnakeDirection.LEFT
                    elif event.key == K_RIGHT:
                        block_direction = SnakeDirection.RIGHT
                elif event.type == QUIT:
                    self.running = False
                    continue

            match block_direction:
                case SnakeDirection.UP: block.move_up()
                case SnakeDirection.DOWN: block.move_down()
                case SnakeDirection.LEFT: block.move_left()
                case SnakeDirection.RIGHT: block.move_right()

            sleep(0.2)
            self.display.draw_sprite(block)
