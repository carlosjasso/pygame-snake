import pygame
from pygame.event import Event
from pygame import Surface
from pygame.locals import KEYDOWN, QUIT, K_ESCAPE, K_UP, K_DOWN, K_LEFT, K_RIGHT
from typing import NamedTuple
from configuration import Configuration
from sprites import Sprite
from models.enum import DisplayEvent

class Color(NamedTuple):
    Red : int
    Green : int
    Blue : int

class Display:
    surface : Surface

    @property
    def background_color(self):
        return Color(154, 204, 153) # HEX color #9acc99
    
    @property
    def events(self) -> list[DisplayEvent]:
        result : list[DisplayEvent] = []
        for event in pygame.event.get():
            result.append(self._pygame_event_to_dosplay_event(event))
        return result
    
    def _pygame_event_to_dosplay_event(self, event : Event) -> DisplayEvent:
        if event.type == QUIT:
            return DisplayEvent.EXIT
        elif event.type == KEYDOWN:
            return self._pygame_key_to_display_event(event.key)
    
    def _pygame_key_to_display_event(self, key : int) -> DisplayEvent:
        if key == K_ESCAPE: return DisplayEvent.EXIT
        elif key == K_UP: return DisplayEvent.MOVE_UP
        elif key == K_DOWN: return DisplayEvent.MOVE_DOWN
        elif key == K_LEFT: return DisplayEvent.MOVE_LEFT
        elif key == K_RIGHT: return DisplayEvent.MOVE_RIGHT

    def __init__(self, config : Configuration) -> None:
        # Inits pygame display and setup window size
        # pygame must be initted before building the sprites
        pygame.init()
        self.surface = pygame.display.set_mode(config.window.WINDOW_SIZE)
    
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
