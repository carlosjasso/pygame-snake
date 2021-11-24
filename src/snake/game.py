import pygame
from pygame import Surface
from pygame.locals import KEYDOWN, QUIT, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT
from models.configuration import Configuration
from models.sprite import Sprite
from models.block import Block

class Game:
    config : Configuration
    display : Surface

    @property
    def background_color(self):
        return (154, 204, 153) # HEX color #9acc99

    def __init__(self, config : Configuration) -> None:
        self.config = config

    def run(self):
        # Inits pygame display and setup window size
        # pygame must be initted before building the sprites
        pygame.init()
        self.display = pygame.display.set_mode(self.config.window.WindowSize)

        # sprite building
        block = Block(self.config.sprites.BLOCK_PATH)

        self.draw_sprite(block)

        # Event loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: 
                        running = False
                    elif event.key == K_UP: 
                        block.move_up()
                        self.draw_sprite(block)
                    elif event.key == K_DOWN: 
                        block.move_down()
                        self.draw_sprite(block)
                    elif event.key == K_LEFT: 
                        block.move_left()
                        self.draw_sprite(block)
                    elif event.key == K_RIGHT: 
                        block.move_right()
                        self.draw_sprite(block)
                elif event.type == QUIT:
                    running = False
    
    def draw_sprite(self, sprite : Sprite):
        self.display.fill(self.background_color) # clears screen
        self.display.blit(sprite.surface, sprite.position)
        self.update_screen()
    
    def update_screen(self):
        # Update screen after a change
        #   display.flip() will update the contents of the entire display
        #   display.update() allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
        pygame.display.flip()
