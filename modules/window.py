from collections import namedtuple
import pygame
from models.configuration import Configuration

WindowSize = namedtuple("WindowSize", ["width", "height"])
BackgroundColor = namedtuple("Background", ["Red", "Green", "Blue"])

class Window:
    def __init__(self, config : Configuration) -> None:
        self._load_props(config)
        self._init_pygame()
    
    def _load_props(self, config : Configuration) -> None:
        config_section = config.get_section("WINDOW")
        self.size = WindowSize(
            width = int(config_section["width"]),
            height =int(config_section["height"])
        )
        self.background_color = BackgroundColor(
            Red = int(config_section["red"]),
            Green = int(config_section["green"]),
            Blue = int(config_section["blue"])
        )
        
    def _init_pygame(self) -> None:
        pygame.init()
        self.surface = pygame.display.set_mode(self.size) # set windows size in px
        self.surface.fill(self.background_color)
        self.refresh()

    def refresh(self) -> None:
        pygame.display.flip() # refresh entide window

    # def _load_sprites(self) -> None:
    #     self._sprites = self._generate_sprites()
    #     self._draw_sprites(self._sprites)
    
    # def _generate_sprites(self) -> Sprites:
    #     sprites_props : set[Sprite] = self._config.get_sprites_props()
    #     for key in sprites_props:
    #         sprite : Sprite = sprites_props[key]
    #         sprite.surface = pygame.image.load(sprite.path).convert()
    #     return Sprites(block=sprites_props["block"])
    
    # def _draw_sprites(self, sprites : Sprites) -> None:
    #     self._surface.fill((110, 110, 5)) # set the window background color in RGB
    #     block : Sprite = sprites.block
    #     self._surface.blit(block.surface, block.position)
    #     self.refresh()
     
    # def _update_block_position(self, x : int, y : int) -> None:
    #     block : Sprite = self._sprites.block
    #     block.update_position(x, y)
    #     self._draw_sprites(self._sprites)
