import pygame
from pygame import Surface
from pygame.event import event_name
from pygame.locals import KEYDOWN, QUIT, K_ESCAPE
from modules.configuration import Configuration
from models import SpriteProps, Sprites

class Window:
    def __init__(self, config : Configuration) -> None:
        self._config = config
        
    def _init_pygame(self) -> None:
        pygame.init()
        props = self._config.get_window_props()
        surface : Surface = pygame.display.set_mode(props.size) # set windows size in px
        surface.fill((110, 110, 5)) # set the window background color in RGB
        self._load_sprites()
        self.refresh()

    def _load_sprites(self) -> None:
        sprites_props : set[SpriteProps] = self._config.get_sprites_props()
        sprites = {}
        for key in sprites_props:
            props : SpriteProps = sprites_props[key]
            sprites[props.name] = pygame.image.load(props.path).convert()
        self._sprites = Sprites(block=sprites["block"])
    
    def refresh(self) -> None:
        pygame.display.flip() # refresh entide window
    
    def start(self) -> None:
        self._init_pygame()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False
