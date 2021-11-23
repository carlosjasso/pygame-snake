from os import path
import pygame
from pygame import Surface
from pygame.locals import KEYDOWN, QUIT, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT
from models.configuration import Configuration
from models.sprite import Sprite
from models.block import Block

class Game:
    display : Surface

    @property
    def background_color(self):
        return (154, 204, 153) # HEX color #9acc99

    def __init__(self, config : Configuration) -> None:
        self._config = config

    def run(self):
        window_config = self._config.get_section("WINDOW")
        window_width = int(window_config["width"])
        window_height = int(window_config["height"])
        window_size = (window_width, window_height)

        sprites_config = self._config.get_section("SPRITES")
        block = Block(path.join(self._config.root_path, sprites_config["block"]))

        pygame.init()
        # Inits pygame display and provide window size
        self.display = pygame.display.set_mode(window_size)
        self.display.fill(self.background_color)

        block.surface = pygame.image.load(block.img_path).convert()

        self.draw_sprite(block)

        self.update_screen()

        # Event loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: running = False
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
