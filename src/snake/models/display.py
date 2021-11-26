import pygame
from pygame import Surface
from .configuration import Configuration
from .sprite import Sprite

class Display:
    surface : Surface

    @property
    def background_color(self):
        return (154, 204, 153) # HEX color #9acc99
    
    @property
    def event(self):
        return pygame.event.get()

    def __init__(self, config : Configuration) -> None:
        # Inits pygame display and setup window size
        # pygame must be initted before building the sprites
        pygame.init()
        self.surface = pygame.display.set_mode(config.window.WindowSize)
    
    def draw_sprite(self, sprite : Sprite):
        self.surface.fill(self.background_color) # clears screen
        self.surface.blit(sprite.surface, sprite.position)
        self.refresh()

    def draw_sprites(self, sprites : list[Sprite]):
        self.surface.fill(self.background_color) # clears screen
        for sprite in sprites:
            self.surface.blit(sprite.surface, sprite.position)
        self.refresh()
    
    def refresh(self):
        # Update screen after a change
        #   display.flip() will update the contents of the entire display
        #   display.update() allows to update a portion of the screen, instead of the entire area of the screen. Passing no arguments, updates the entire display
        pygame.display.flip()