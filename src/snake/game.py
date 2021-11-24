from pygame.locals import KEYDOWN, QUIT, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT
from models.block import Block
from models.configuration import Configuration
from models.display import Display

class Game:
    config : Configuration
    display : Display

    def __init__(self, config : Configuration) -> None:
        self.config = config
        self.display = Display(config)

    def run(self):
        # sprite building
        block = Block(self.config.sprites.BLOCK_PATH)

        self.display.draw_sprite(block)

        # Event loop
        running = True
        while running:
            for event in self.display.event:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: 
                        running = False
                    elif event.key == K_UP: 
                        block.move_up()
                        self.display.draw_sprite(block)
                    elif event.key == K_DOWN: 
                        block.move_down()
                        self.display.draw_sprite(block)
                    elif event.key == K_LEFT: 
                        block.move_left()
                        self.display.draw_sprite(block)
                    elif event.key == K_RIGHT: 
                        block.move_right()
                        self.display.draw_sprite(block)
                elif event.type == QUIT:
                    running = False
